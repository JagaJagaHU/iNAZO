<template>
    <v-row>
        <v-col cols="12">
            <p
                class="text-h4 text-sm-h3 text-center describe-title"
            >
                <span
                    class="
                        text-h3
                        text-sm-h1
                        font-weight-medium
                        text-decoration-underline
                        blue--text"
                >iNAZO</span>の特徴
            </p>
        </v-col>

        <v-col
            cols="12"
            sm="4"
        >
            <home-describe-card title="シェア機能" contents="ボタン1つで気になる講義をグラフで共有" />
        </v-col>

        <v-col
            cols="12"
            sm="4"
        >
            <home-describe-card title="お気に入り" contents="気になる講義を登録してあなただけの一覧を" />
        </v-col>

        <v-col
            cols="12"
            sm="4"
        >
            <home-describe-card title="ソート検索" contents="表示順を変えることで知りたい情報を探しやすく" />
        </v-col>
    </v-row>
</template>

<style scoped>
.describe-title {
    margin: 2rem 0;
}

@media screen and (min-width:600px) {
    .describe-title {
        margin: 5rem 0;
    }
}
</style>
