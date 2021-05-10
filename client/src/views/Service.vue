<template>

<v-container>
    <nav class="my-10">
        <v-row>
        
        <v-col
          cols="6"
          md="4"
        >
        <v-text-field
            :counter="30"
            v-model='search'
            @keydown.enter="filterSearch"
            label="Search"
            required
        ></v-text-field>
        
        </v-col>
        <v-col
          cols="6"
          md="4"
        >
        <v-btn color="green" elevation="2" @click='filterSearch' dark>Search</v-btn>
        </v-col>

        <v-spacer></v-spacer>

        <v-col
          cols="3"
          md="2"
        >
        <v-select
          :items="gradeItems"
          label="Sort"
          v-model="query.ordering"
          @change="filterSort"
        ></v-select>
        </v-col>

        </v-row>
        
    </nav>

    <v-alert
    type="success"
    v-if='searchResultText'
    >
    検索結果：{{searchResultText}}
    </v-alert>

    <v-card class="my-5" v-for="item in items" :key="item.id" flat outlined>
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
            size: null,
            search: '',
            searchResultText: null,
            query: {
                'search': '',
                'ordering': '',
                'page': '1',
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
            ]
        }
    },

    methods: {
        filterSearch() {
            this.query['search'] = this.search;

            this.query.page = 1;
            this.getAPIData(gradeURL);
        },

        filterSort() {
            
            this.query.page = 1;
            this.getAPIData(gradeURL);
        },

        fromChild(page) {
            if (page <= 0 || page > this.size) return;
            
            this.query.page = page;
            this.getAPIData(gradeURL);
        },

        _joinQuery(url) {
            let queryURL = "";
            Object.keys(this.query).forEach(key => queryURL += "&" + key + "=" + this.query[key]);
            if (url.indexOf('?') == -1){
                queryURL = queryURL.replace("&", "?"); // 先頭の&を?に置換
            }
            return url + queryURL;
        },

        getAPIData(url) {
            this.axios.get(this._joinQuery(url)).then(res => {
                this.items.splice(0, this.items.length);
                this.items.push(...res.data.results);
                this.size = res.data.size;
                this.currentPage = this.query.page;
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
        }
    },
    mounted() {
        this.axios.get(gradeURL).then(res => {
            this.items = res.data.results;
            this.size = res.data.size;
        });
    },
}

</script>