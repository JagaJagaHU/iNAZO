module.exports = {
    root: true,
    env: {
        node: true
    },
    'extends': [
        'plugin:vue/essential',
        'plugin:vue/strongly-recommended',
        'plugin:vue/recommended',
        'eslint:recommended',
    ],
    parserOptions: {
        parser: 'babel-eslint'
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-extra-semi': 'warn',
        'quotes': ['warn', 'single'],
        'space-before-blocks': ['warn', { 'functions': 'always' }],
        'indent': ['error', 4],
        'vue/html-indent': ['error', 4],
        'semi': ['error', 'always'],
    }
};
