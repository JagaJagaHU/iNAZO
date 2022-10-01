<template>
    <v-container>
        <search-pagination
            :size="size"
            :total-visible="totalVisible"
            :current-page="currentPage"
            :count="count"
            @updatePage="setPageAndGetData"
            @input="(page) => (currentPage = page)"
        />

        <search-input-list
            :chart-grid-col.sync="chartGridCol"
            :search.sync="query.search"
            :ordering.sync="query.ordering"
            @sortChange="sort"
            @filterSearch="filterSearch"
        />

        <!-- Alert-->
        <search-success-alart v-if="searchResultText" :search-result-text="searchResultText" />

        <!-- main cards -->
        <search-main-container :is-visible="isVisible" :items="items" :chart-grid-col="chartGridCol" @starClick="postBookMark($event)" />

        <search-pagination
            :size="size"
            :total-visible="totalVisible"
            :current-page="currentPage"
            :count="count"
            @updatePage="setPageAndGetData"
            @input="(page) => (currentPage = page)"
        />
    </v-container>
</template>

<script>
import axios from 'axios';
import MobileDetect from 'mobile-detect';
import chartMixin from '@/mixins/chart-mixin';

const protocol = process.env.PROTOCOL;
const origin = process.env.ORIGIN;
const gradeURL = `${protocol}://${origin}/api/gradeinfo/`;
const bookmarkURL = `${protocol}://${origin}/api/bookmark/`;

export default {
    mixins: [chartMixin],
    beforeRouteUpdate (to, from, next) {
    // クエリなしに対応
        this.query.page = to.query.page || 1;
        this.query.ordering = to.query.ordering || '';
        this.query.search = to.query.search || '';
        window.scrollTo(0, 0);
        this.fetchGradeAPIData();
        next();
    },
    data () {
        return {
            // Pagination
            currentPage: 1,
            totalVisible: 0,
            size: 0,
            count: null,

            searchResultText: null
        };
    },
    async fetch () {
        if (this.$route.fullpath !== '/service') {
            this.query.page = this.$route.query.page || 1;
            this.query.ordering = this.$route.query.ordering || '';
            this.query.search = this.$route.query.search || '';
        }

        await this.fetchGradeAPIData();

        if (process.server) {
            const headers = this.$nuxt.context.req.headers;
            await this.fetchBookmarkAPIData(headers);
            const md = new MobileDetect(headers['user-agent']);
            this.chartGridCol = md.mobile() ? 12 : 6;
            this.totalVisible = md.mobile() ? 5 : 10;
        } else {
            await this.fetchBookmarkAPIData();
        }
    },
    head () {
        return {
            title: `${this.query.search ? this.query.search + ' - ' : ''}成績検索`
        };
    },
    mounted () {
        // 画面サイズがxsなら表示個数を減らす
        this.totalVisible = window.innerWidth <= 600 ? 5 : 10;
        this.chartGridCol = window.innerWidth <= 600 ? 12 : 6;
    },
    methods: {
        filterSearch () {
            // vuetifyのclearはnullが挿入される
            this.query.search = this.query.search || '';
            this.query.page = 1;

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL);
        },

        setPageAndGetData (page) {
            if (page <= 0 || page > this.size) { return; }
            if (page === this.query.page) { return; }
            this.query.page = page;
            window.scrollTo(0, 0);

            const fullURL = this.joinQuery(this.$route.path);
            if (this.$route.path !== fullURL) {
                this.$router.push(fullURL);
            }
        },

        async fetchGradeAPIData () {
            this.isVisible = false;

            let res;
            try {
                res = await axios.get(this.joinQuery(gradeURL), {
                    withCredentials: true
                });
            } catch (error) {
                if (error.response) {
                    this.$nuxt.error({
                        status: error.response.status,
                        message: 'サーバーでエラーが発生しました'
                    });
                } else if (error.request) {
                    this.$nuxt.error({
                        message: 'サーバーからレスポンスがありません'
                    });
                } else {
                    this.$nuxt.error({
                        message: error.message
                    });
                }
                return;
            }

            // 取得したデータがブックマークされているか確認
            res.data.results.forEach((item) => {
                item.isBookMark = this.bookMarkIDs.includes(item.id);
            });
            // chartを更新
            this.items.splice(0, this.items.length);
            this.items.push(...res.data.results);
            this.size = res.data.size;
            this.count = res.data.count;
            this.currentPage = Number(this.query.page);
            this.searchResultText = this.query.search;

            // 取得したデータがブックマークされているか確認

            this.isVisible = true;
        },

        // ページに訪れた時のみに使用
        async fetchBookmarkAPIData (headers) {
            const options = {
                withCredentials: true
            };
            if (headers) { options.headers = { cookie: headers.cookie }; }
            let res;
            try {
                res = await axios.get(bookmarkURL, options);
            } catch (error) {
                if (error.response) {
                    this.$nuxt.error({
                        status: error.response.status,
                        message: 'サーバーでエラーが発生しました'
                    });
                } else if (error.request) {
                    this.$nuxt.error({
                        message: 'サーバーからレスポンスがありません'
                    });
                } else {
                    this.$nuxt.error({
                        message: error.message
                    });
                }
                return;
            }
            this.bookMarkIDs = res.data.map(item => item.id);
            this.items.forEach((item) => {
                this.$set(item, 'isBookMark', this.bookMarkIDs.includes(item.id));
            });
        }
    }
};
</script>
