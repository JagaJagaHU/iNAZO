<template>

<v-container>

<!-- top -->
<v-row>
<v-col>
    <v-parallax
        class="mb-5 mb-sm-10"
        src="@/assets/title-background.jpg"
        :height="height"
    >
    <v-row class="ml-sm-5" align="center" justify="center">
    <v-col class="text-center" cols="12">
        <p class="text-h6">北大成績分布公開サービス</p>
        <p class="text-h3 text-sm-h1 ml-sm-5 font-weight-thin mb-4">HUsearch</p>
        <v-btn
            class="px-sm-10 py-sm-10 mt-5"
            x-large
            color="success"
            dark
            to="/search"
        >
            今すぐはじめよう！
        </v-btn>
    </v-col>
    </v-row>
    
    </v-parallax>

    <p class="text-h4 text-sm-h3 text-center" style="margin: 10rem 0rem 5rem">HUsearchとは？</p>
    <p class="text-h6 text-center">北海道大学が公開している成績データをグラフで明解に表示します。</p>
    
</v-col>
</v-row>

<!-- cards -->
<v-row style="margin: 10rem 1rem">
<v-col cols="12" sm="4">
    <v-card
    class="px-10 py-10"
    color="#26c6da"
    dark>
    <p class="text-center text-h4 py-5">講義の検索機能</p>
    <v-card-subtitle class="text-h6 pb-5">
            調べたい講義の情報をすぐ見つけられます<br>
    </v-card-subtitle>
    </v-card>
</v-col>

<v-col cols="12" sm="4">
    <v-card
    class="px-10 py-10"
    color="#26c6da"
    dark>
    <p class="text-center text-h4 py-5">明快なグラフ</p>
    <v-card-subtitle class="text-h6 pb-5">
            成績はグループごとに色分けされています<br>
    </v-card-subtitle>
    </v-card>
</v-col>

<v-col cols="12" sm="4">
    <v-card
    class="px-10 py-10"
    color="#26c6da"
    dark>
    <p class="text-center text-h4 py-5">組織で運用</p>
    <v-card-subtitle class="text-h6 pb-5">
            本サービスはJagaJagaで開発・運用されています<br>
    </v-card-subtitle>
    </v-card>
</v-col>
</v-row>

<!-- Q&A -->
<v-row class="my-10">
<v-col class="px-10 py-10" style="background-color: #ECEFF1">

    <p class="text-h3 text-center my-10">Q&A</p>

    <div class="my-16">
    <p class="text-h6 font-weight-bold">・大学公認ですか？</p>
    <p class="text-h6">いいえ、非公認です。今後大学側に確認を取るかもしれません。</p>
    </div>

    <div class="my-16">
    <p class="text-h6 font-weight-bold">・ソート機能は楽単探しの助長になるのでは？</p>
    <p class="text-h6">
    総合文系・理系は行きたい学部に行くために高い移行点が必要になるかもしれません。
    もちろん、楽単探しを積極的お勧めするわけではありません。しかし複数の受けたい講義
    があり、かつ成績も必要であればそのうち比較的gpaが高い講義を選ぶ可能性が高いと思われます。
    ソート機能はそのような選択の助けになることを望んでいます。
    </p>
    </div>

    <div class="my-16">
    <p class="text-h6 font-weight-bold">・誰が作ってるの？</p>
    <p class="text-h6">
    北大初オンラインメディアのJagaJagaが開発・運用しています。
    </p>
    </div>

</v-col>
</v-row>

<!-- link -->
<v-row class="my-10">
<v-col class="px-10 py-10" style="background-color: #ECEFF1">

    <p class="text-h3 text-center my-10">Link</p>
    <p>
    <a href="http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx">
    北海道大学 成績分布ＷＥＢ公開システム
    </a>
    </p>
    <p>本サービスの情報源です。</p>
    <p>
    <a href="http://hu-jagajaga.com/">JagaJaga</a>
    </p>
    <p>JagaJagaのホームページです。</p>
</v-col>
</v-row>

</v-container>

</template>

<script>

export default {
    computed: {
        height () {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 220;
                case 'sm': return 400;
                case 'md': return 400;
                case 'lg': return 500;
                case 'xl': return 500;
            }
            return 0;
        },
    },
}

</script>

<style>

.button {
  text-align: center;
}

</style>