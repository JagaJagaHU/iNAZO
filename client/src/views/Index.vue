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
                    <v-row
                        class="ml-sm-5"
                        align="center"
                        justify="center"
                    >
                        <v-col
                            class="text-center"
                            cols="12"
                        >
                            <p class="text-h6">
                                北大成績分布検索サービス
                            </p>
                            <p class="text-h3 text-sm-h1 ml-sm-5 font-weight-thin mb-4">
                                iNAZO
                            </p>
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
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <p
                    class="text-h4 text-sm-h3 text-center"
                    style="margin: 5rem 0rem 5rem"
                >
                    <span
                        class="
                        text-h3
                        text-sm-h1
                        font-weight-medium
                        text-decoration-underline
                        blue--text"
                    >iNAZO</span>とは？
                </p>
                <p class="text-h6 text-center">
                    北大が公開している成績データをより扱いやすくしたサイトです。<br>
                    成績分布のグラフは直感的に認識できるようになっています。
                </p>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <p
                    class="text-h4 text-sm-h3 text-center"
                    style="margin: 5rem 0rem 5rem"
                >
                    使う場面は？
                </p>
                <div class="text-h6 text-center">
                    <p>iNAZOは以下の場面に便利です。</p>
                    <p>・受けた講義の成績分布を知りたい。</p>
                    <p>・これから受けたい講義の過去の成績を知りたい。</p>
                    <p>・複数の気になる講義の成績を比較したい。</p>
                </div>
            </v-col>
        </v-row>

        <!-- cards -->
        <v-row style="margin: 3rem 1rem">
            <v-col cols="12">
                <p
                    class="text-h4 text-sm-h3 text-center"
                    style="margin: 5rem 0rem 5rem"
                >
                    iNAZOの機能
                </p>
            </v-col>
            <v-col
                cols="12"
                sm="4"
            >
                <v-card
                    class="px-10 py-10"
                    color="#26c6da"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        明快なグラフ
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        成績はグループごとに色分けされています。<br>
                    </v-card-subtitle>
                </v-card>
            </v-col>

            <v-col
                cols="12"
                sm="4"
            >
                <v-card
                    class="px-10 py-10"
                    color="#26c6da"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        シンプルな検索機能
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        講義名・教授・年代などの情報から検索できます。<br>
                    </v-card-subtitle>
                </v-card>
            </v-col>

            <v-col
                cols="12"
                sm="4"
            >
                <v-card
                    class="px-10 py-10"
                    color="#26c6da"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        ブックマーク機能
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        気になる講義を登録して一覧表示ができます。<br>
                    </v-card-subtitle>
                </v-card>
            </v-col>
        </v-row>

        <!-- Q&A -->
        <v-row class="my-10">
            <v-col
                class="px-10 py-10"
                style="background-color: #ECEFF1"
            >
                <p class="text-h4 text-center my-10">
                    Q&A
                </p>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        ・誰が作っているのですか？
                    </p>
                    <p class="text-h6">
                        北大生応援メディアのJagaJagaが開発・運用しています。
                    </p>
                </div>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        ・このサービスは大学公認ですか？
                    </p>
                    <p class="text-h6">
                        いいえ、非公認です。これからどうするかは検討中です。
                    </p>
                </div>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        バグを見つけたらどうすればいいですか？
                    </p>
                    <p class="text-h6">
                        見つけたバグを以下のGoogle Formに書いて送信してください。
                        機能追加や要望も受け付けます。
                    </p>
                </div>
            </v-col>
        </v-row>

        <!-- link -->
        <v-row class="my-10">
            <v-col
                class="px-10 py-10"
                style="background-color: #ECEFF1"
            >
                <p class="text-h3 text-center my-10">
                    Link
                </p>
                <p>
                    <a href="#">iNAZO公式Twitter</a>
                </p>
                <p>更新や障害情報をお知らせします。お問い合わせはDMにお願いします。</p>
                <p>
                    <a href="http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx">
                        北海道大学 成績分布ＷＥＢ公開システム
                    </a>
                </p>
                <p>本サービスの情報源です。</p>
                <p>
                    <a href="http://hu-jagajaga.com/">JagaJaga - 北大生応援メディア -</a>
                </p>
                <p>JagaJagaのホームページです。</p>
                <p>
                    <a href="https://twitter.com/jagajagahu">JagaJaga公式Twitter</a>
                </p>
                <p>JagaJagaの公式Twitterです。</p>
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
};

</script>

<style>

.button {
  text-align: center;
}

</style>