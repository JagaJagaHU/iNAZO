import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Index',
        component: () => import('../views/Index.vue'),
        meta: { title: 'ホーム', desc: 'ホームページ' },
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('../views/Search.vue'),
        meta: { title: '成績分布検索システム', desc: '績分布検索システムを利用可能' },
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
