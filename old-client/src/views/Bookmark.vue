<template>
    <v-container>
        <!-- 表示・検索機能 -->
        <v-row>
            <v-spacer />

            <v-col
                class="d-none d-sm-flex mx-5 mx-sm-0"
                cols="6"
                sm="2"
            >
                <v-select
                    v-model="chartGridCol"
                    prepend-icon="mdi-grid-large"
                    label="grid"
                    :items="gridItems"
                />
            </v-col>

            <v-col
                class="mx-5 mx-sm-0"
                cols="6"
                sm="2"
            >
                <v-select
                    v-model="query.ordering"
                    prepend-icon="mdi-sort-descending"
                    :items="sortItems"
                    label="Sort"
                    @change="sort"
                />
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-alert
                    color="blue"
                    type="info"
                >
                    あなたのブックマーク一覧
                </v-alert>
            </v-col>
        </v-row>

        <!-- main cards -->
        <v-row>
            <template v-if="!isVisible">
                <v-col
                    v-for="i in 10"
                    :key="i"
                    :cols="chartGridCol"
                >
                    <SkeletonCard />
                </v-col>
            </template>
            <template v-else>
                <v-col
                    v-for="(item, index) in items"
                    :key="item.id"
                    :cols="chartGridCol"
                >
                    <MainCard
                        :item="item"
                        :index="index"
                        @starClick="postBookMark(index)"
                    />
                </v-col>
            </template>
        </v-row>
    </v-container>
</template>

<script>
import MainCard from '../components/search/Card.vue';
import SkeletonCard from '../components/search/SkeletonCard.vue';

const protocol = process.env.VUE_APP_PROTOCOL;
const origin = process.env.VUE_APP_ORIGIN;
const bookmarkURL = `${protocol}://${origin}/api/bookmark/`;

const HTTP_201_CREATED = 201;
const HTTP_204_NO_CONTENT = 204;

export default {
    components: {
        MainCard,
        SkeletonCard
    },
    data() {
        return {
            // Main Card
            items: [],
            bookMarkIDs: [],
            isVisible: false,

            chartGridCol: 12,
            chartHight: 300,
            sortItems: [
                { text: '新着順', value: '' },
                { text: 'GPA (降順)', value: '-gpa' },
                { text: 'GPA (昇順)', value: 'gpa' },
                { text: '単位取得', value: 'failure' },
                { text: '落単', value: '-failure' },
                { text: 'A帯 (降順)', value: '-a_band'},
                { text: 'A帯 (昇順)', value: 'a_band'},
                { text: 'F (降順)', value: '-f' },
            ],
            gridItems: [
                {text: '１列', value: 12},
                {text: '２列', value: 6},
            ],
            query: {
                'ordering': '',
            },
        };
    },
    created() {
        this.chartGridCol = window.innerWidth <= 600 ? 12 : 6;
    },
    async mounted() {
        if (this.$route.fullpath != '/service') {
            this.query.ordering = this.$route.query.ordering || '';
        }
        await this.fetchBookmarkAPIData();
    },
    beforeRouteUpdate(to, from, next) {
        // クエリなしに対応
        this.query.ordering = to.query.ordering || '';
        window.scrollTo(0, 0);
        this.fetchBookmarkAPIData();
        next();
    },
    methods: {
        sort() {
            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => { console.log(err); });
        },

        joinQuery(url) {
            let queryURL = '';
            Object.keys(this.query).forEach(key => queryURL += '&' + key + '=' + this.query[key]);
            if (url.indexOf('?') == -1) {
                queryURL = queryURL.replace('&', '?'); // 先頭の&を?に置換
            }
            return url + queryURL;
        },

        async postBookMark(index) {
            // Objectをコピーする必要がある。
            const item = Object.assign({}, this.items[index]);
            const bookMarkID = item.id;

            if (item.isBookMark) {
                // ブックマーク解除
                const res = await this.axios.delete(`${bookmarkURL}${bookMarkID}/`, {
                    withCredentials: true,
                });
                if (res.status == HTTP_204_NO_CONTENT) {
                    this.bookMarkIDs = this.bookMarkIDs.filter((id) => id != bookMarkID);
                    item.isBookMark = !item.isBookMark;
                    this.$set(this.items, index, item);
                }
            } else {
                // 登録
                const res = await this.axios.post(
                    bookmarkURL,
                    { bookMarkID: bookMarkID },
                    {
                        withCredentials: true,
                    }
                );

                if (res.status == HTTP_201_CREATED) {
                    this.bookMarkIDs = res.data.bookMarkIDs;
                    item.isBookMark = !item.isBookMark;
                    this.$set(this.items, index, item);
                }
            }
        },

        async fetchBookmarkAPIData() {
            this.isVisible = false;

            const res = await this.axios.get(this.joinQuery(bookmarkURL), {
                withCredentials: true
            });

            this.items.splice(0, this.items.length);
            this.items.push(...res.data);

            // 取得したデータがブックマーク
            this.bookMarkIDs = res.data.map(item => item.id);
            this.items.map(item => {
                item.isBookMark = this.bookMarkIDs.includes(item.id);
            });
            
            this.isVisible = true;
        },
    }
};
</script>
