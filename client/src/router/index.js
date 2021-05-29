import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Index',
        component: () => import('../views/Index.vue'),
        meta: { title: 'ホームページ', desc: `北大の公開されている成績分布データをグラフ化しました。
        ソート検索やブックマークでカスタマイズしたあなただけのiNAZOと行きたい学部にいこう。`},
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('../views/Search.vue'),
        meta: { title: '成績検索', desc: '成績分布検索サービスを利用可能' },
    },
    {
        path: '/bookmark',
        name: 'Bookmark',
        component: () => import('../views/Bookmark.vue'),
        meta: { title: 'ブックマーク一覧', desc: 'ブックマーク一覧を表示' },
    },
    {
        path: '*',
        name: '404',
        component: () => import('../views/404.vue'),
        meta: { title: 'このページは存在しません。', desc: '404 not found.' },
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
