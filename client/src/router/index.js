import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('../views/Index.vue'),
    meta: { title: 'ホーム', desc: 'ホームページ' },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    meta: { title: 'About', desc: 'HUsearchについて' },
  },
  {
    path: '/service',
    name: 'service',
    component: () => import('../views/Service.vue'),
    meta: { title: '成績分布検索システム', desc: '績分布検索システムを利用可能' },
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
