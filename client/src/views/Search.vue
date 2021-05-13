<template>

<v-container>

    <!-- pagination -->
    <v-row>
    <v-col>
        
        <div class="text-center my-10">
            <v-pagination
            v-model="currentPage"
            :length="size"
            :total-visible="totalVisible"
            @input="setPageAndGetData"
            ></v-pagination>
        </div>

    </v-col>  
    </v-row>

    <!-- 表示・検索機能 -->
    <v-row>
    <v-col
    class="mx-5 mx-sm-0"
    cols="6"
    md="4"
    >
        <v-text-field
            :counter="100"
            v-model='search'
            @keydown.enter="filterSearch"
            label="Search"
            required
        ></v-text-field>
        
    </v-col>

    <v-col
    cols="4"
    md="4"
    >
        <v-btn color="green" elevation="2" @click='filterSearch' dark>Search</v-btn>
    </v-col>

    <v-spacer></v-spacer>

    <v-col
    class="mx-5 mx-sm-0"
    cols="6"
    sm="1">
    
        <v-select
            :items="gridItems"
            label="grid"
            v-model="chartGridCol"
        ></v-select>

    </v-col>

    <v-col
    class="mx-5 mx-sm-0"
    cols="6"
    sm="2"
    >
        <v-select
          :items="gradeItems"
          label="Sort"
          v-model="query.ordering"
          @change="sort"
        ></v-select>
    </v-col>
    </v-row>

    <!-- 検索結果 -->
    <v-row>
    <v-col>
    
    <v-alert
    type="success"
    v-if='searchResultText'
    >
    検索結果：{{searchResultText}}
    </v-alert>

    </v-col>
    </v-row>

    <!-- main cards -->
    <v-row>
    <v-col :cols="chartGridCol" v-for="item in items" :key="item.id">
    
    <v-card class="my-5" flat outlined>
        <v-card-title v-if='item.subject == " "'> {{item.lecture}} </v-card-title>
        <v-card-title v-else> {{item.subject}} &emsp; {{item.lecture}} </v-card-title>

        <v-card-text>
            <p class="card-text">{{item.year}}年度 {{item.semester}}</p>
            <p class="card-text">開講学部：{{item.faculty}}</p>
            <p class="card-text">クラス：{{item.group}}</p>
            <p class="card-text">履修者数 : {{item.numOfStudents}}人</p>
            <p>担当教員名：{{item.teacher}}</p>
            <p>GPA : {{item.gpa}}</p>
        </v-card-text>

        <v-card-text>
            <BarChart :chartData="getChartData(item)"></BarChart>  
        </v-card-text>
    </v-card>

    </v-col>
    </v-row>

    <!-- pagination -->
    <v-row>
    <v-col>
    
    <div class="text-center my-10">
        <v-pagination
        v-model="currentPage"
        :length="size"
        :total-visible="totalVisible"
        @input="setPageAndGetData"
        ></v-pagination>
    </div>

    </v-col>
    </v-row>
    
</v-container>

</template>

<script>
import BarChart from '../components/BarChart.vue'

let gradeURL = 'http://localhost:8001/api/gradeinfo/';

export default {
    components: {
        BarChart,
    },
    data() {
        return {
            items : [],
            currentPage: 1,
            totalVisible: null, 
            size: null,
            search: '',
            searchResultText: null,
            chartGridCol: 12,
            query: {
                'search': '',
                'ordering': '',
                'page': 1,
            },
            gradeItems: [
                {text:'新着順', value:''},
                {text:'A+', value:'-ap'},
                {text:'A', value:'-a'},
                {text:'A-', value:'-am'},
                {text:'B+', value:'-bp'},
                {text:'B', value:'-b'},
                {text:'B-', value:'-bm'},
                {text:'C+', value:'-cp'},
                {text:'C', value:'-c'},
                {text:'D', value:'-d'},
                {text:'D-', value:'-dm'},
                {text:'F', value:'-f'},
                {text:'GPA', value:'-gpa'},
            ],
            gridItems: [
                {text:'1列', value:12},
                {text:'２列', value:6},
            ],
        }
    },
    beforeRouteUpdate(to, from, next) {
        // クエリなしに対応
        this.query.page = to.query.page || 1;
        this.query.ordering = to.query.ordering || '';
        this.query.search = to.query.search || '';
        window.scrollTo(0,0);
        this.fetchAPIData(gradeURL);
        next();
    },
    methods: {
        filterSearch() {
            this.query['search'] = this.search;
            this.query.page = 1;

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => {}); // eslint-disable-line no-unused-vars
        },

        sort() {
            this.query.page = 1;

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => {}); // eslint-disable-line no-unused-vars
        },

        setPageAndGetData(page) {
            if (page <= 0 || page > this.size) return;
            if (page == this.query.page) return;
            this.query.page = page;
            window.scrollTo(0,0);

            const fullURL = this.joinQuery(this.$route.path);
            this.$router.push(fullURL).catch(err => {}); // eslint-disable-line no-unused-vars
        },

        fetchAPIData(url) {
            this.axios.get(this.joinQuery(url)).then(res => {
                this.items.splice(0, this.items.length);
                this.items.push(...res.data.results);
                this.size = res.data.size;
                this.currentPage = Number(this.query.page);
                this.searchResultText = this.query.search;
            });
        },

        getChartData(item) {
            return {
                labels: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'D-', 'F'],
                datasets: [
                {
                    label: '人数',
                    backgroundColor: [
                        'rgba(33, 150, 243, 1)',
                        'rgba(33, 150, 243, 1)',
                        'rgba(33, 150, 243, 1)',
                        'rgba(187, 222, 251, 1)',
                        'rgba(187, 222, 251, 1)',
                        'rgba(187, 222, 251, 1)',
                        'rgba(255, 152, 0, 1)',
                        'rgba(255, 152, 0, 1)',
                        'rgba(244, 67, 54, 1)',
                        'rgba(244, 67, 54, 1)',
                        'rgba(244, 67, 54, 1)',
                    ],
                    data: [item.ap, item.a, item.am, item.bp, item.b,
                        item.bm, item.cp, item.c, item.d, item.dm, item.f],
                }
                ]
            }
        },

        joinQuery(url) {
            let queryURL = "";
            Object.keys(this.query).forEach(key => queryURL += "&" + key + "=" + this.query[key]);
            if (url.indexOf('?') == -1){
                queryURL = queryURL.replace("&", "?"); // 先頭の&を?に置換
            }
            return url + queryURL;
        },
    },
    created() {
        // 画面サイズがxsなら表示個数を減らす
        this.totalVisible = window.innerWidth <= 600 ? 5 : 10;
    },
    mounted() {
        if (this.$route.fullpath != '/service') {
            this.query.page = this.$route.query.page || 1;
            this.query.ordering = this.$route.query.ordering || '';
            this.query.search = this.$route.query.search || '';
        }
        this.fetchAPIData(gradeURL);
    },
}

</script>