module.exports = {
    root: true,
    env: {
        browser: true,
        node: true
    },
    parserOptions: {
        parser: '@babel/eslint-parser',
        requireConfigFile: false
    },
    extends: [
        '@nuxtjs',
        'plugin:nuxt/recommended'
    ],
    plugins: [
    ],
    // add your custom rules here
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-extra-semi': 'warn',
        quotes: ['warn', 'single'],
        'space-before-blocks': ['warn', { functions: 'always' }],
        indent: ['error', 4],
        'vue/html-indent': ['error', 4],
        semi: ['error', 'always']
    }
};
