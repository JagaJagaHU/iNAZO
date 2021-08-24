require('dotenv').config();

const envFileName = process.env.NODE_ENV !== 'production' ? '.env.local' : '.env.prod';

export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        titleTemplate: '%s | 成績分布検索サービス iNAZO',
        htmlAttrs: {
            lang: 'ja'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { name: 'format-detection', content: 'telephone=no' },
            { hid: 'og:title', name: 'og:title', content: '成績分布検索サービス - iNAZO' },
            { hid: 'og:url', name: 'og:url', content: 'https://inazo.hu-jagajaga.com/' },
            { hid: 'og:type', name: 'og:type', content: 'website' },
            { hid: 'og:description', name: 'og:description', content: '北大の成績分布をグラフにしました。ソート検索やブックマークでカスタマイズして、行きたい学部に行こう！' },
            { hid: 'og:site_name', name: 'og:site_name', content: '成績分布検索サービス - iNAZO' },
            { hid: 'og:image', name: 'og:image', content: '/logo.png' },
            { hid: 'twitter:card', name: 'twitter:card', content: 'summary' },
            { hid: 'twitter:image', name: 'twitter:image', content: 'https://inazo.hu-jagajaga.com/logo.png' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
            { rel: 'apple-touch-icon', type: 'image/png', href: '/apple-touch-icon-180x180.png' },
            { rel: 'icon', type: 'image/png', href: '/icon-192x192.png' },
            { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900' },
            { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css' }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        'ant-design-vue/dist/antd.css'
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '@/plugins/antd-ui',
        '@/plugins/axios.js'
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: {
        dirs: [
            '~/components',
            '~/components/search'
        ]
    },

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
    // https://go.nuxtjs.dev/eslint
        '@nuxtjs/eslint-module',
        '@nuxtjs/vuetify',
        '@nuxtjs/google-analytics',
        ['@nuxtjs/dotenv', { filename: envFileName }]
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
    // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios'
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {},

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
    },

    googleAnalytics: {
        id: 'G-16QBC0CFGJ'
    }
};
