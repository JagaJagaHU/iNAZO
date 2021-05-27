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
                        class="mt-16"
                        align="center"
                        justify="center"
                    >
                        <v-col
                            class="text-center"
                            cols="12"
                        >
                            <p class="text-h6 text-sm-h4">
                                成績分布検索システム
                            </p>
                            <p class="text-h3 text-sm-h1 font-weight-thin mb-4">
                                iNAZO
                            </p>
                        </v-col>
                    </v-row>
                    <v-row
                        class="mb-16"
                        align="center"
                        justify="center"
                    >
                        <v-col
                            cols="12"
                            sm="6"
                        >
                            <v-text-field
                                v-model="search"
                                clearable
                                solo
                                label="講義を検索する"
                                prepend-inner-icon="mdi-magnify"
                                clear-icon="mdi-close-circle"
                                autocomplete="off"
                                @keydown.enter="filterSearch"
                            />
                        </v-col>
                    </v-row>
                </v-parallax>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
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
                <v-row
                    justify="center"
                    class="mx-5 mx-sm-0"
                >
                    <v-col
                        cols="12"
                        sm="8"
                    >
                        <p class="text-h6">
                            北大が公開している成績分布データをより扱いやすくしました。<br>
                            受けたい講義の過去の成績分布が知りたい <br>
                            気になる複数の講義の成績分布を比較したい <br>
                            自分が受講した講義の成績分布を知りたい <br>
                            そんなとき、あなたをお手伝いします。 <br>
                            iNAZOを使って取りたい講義を、取りたい成績を <br>
                            あなたのものにしよう。 <br>
                        </p>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>


        <!-- cards -->
        <v-row>
            <v-col cols="12">
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
                    >iNAZO</span>の特徴
                </p>
            </v-col>
            <v-col
                cols="12"
                sm="4"
            >
                <v-card
                    class="px-10 py-10"
                    height="300"
                    color="#1F7087"
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
                    height="300"
                    color="#1F7087"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        シンプルな検索
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        簡潔で分かりやすい検索窓<br>
                    </v-card-subtitle>
                </v-card>
            </v-col>

            <v-col
                cols="12"
                sm="4"
            >
                <v-card
                    class="px-10 py-10"
                    height="300"
                    color="#1F7087"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        ブックマーク機能
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        自分だけのイナゾーに<br>
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
                <p class="text-h3 text-center my-10">
                    <v-icon
                        color="primary"
                        left
                        size="40"
                    >
                        mdi-help
                    </v-icon>Q&A
                </p>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        ・誰が作っているのですか？
                    </p>
                    <p class="text-h6">
                        北大生応援メディアの
                        <a
                            href="http://hu-jagajaga.com/"
                            target="_blank"
                            rel="noopener noreferrer"
                        >JagaJaga</a>
                        が開発・運用しています。
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
                        ・バグを見つけたらどうすればいいですか？
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
                    <v-icon
                        color="primary"
                        left
                        size="40"
                    >
                        mdi-link-variant
                    </v-icon>Link
                </p>
                <p>
                    <a
                        href="https://twitter.com/iNAZO_HU"
                        target="_blank"
                        rel="noopener noreferrer"
                    >iNAZO公式Twitter</a>
                </p>
                <p>更新や障害情報をお知らせします。お問い合わせはDMにお願いします。</p>
                <p>
                    <a
                        href="http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        北海道大学 成績分布ＷＥＢ公開システム
                    </a>
                </p>
                <p>本サービスの情報源です。</p>
                <p>
                    <a
                        href="http://hu-jagajaga.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                    >JagaJaga - 北大生応援メディア -</a>
                </p>
                <p>JagaJagaのホームページです。</p>
                <p>
                    <a
                        href="https://twitter.com/jagajagahu"
                        target="_blank"
                        rel="noopener noreferrer"
                    >JagaJaga公式Twitter</a>
                </p>
                <p>JagaJagaの公式Twitterです。</p>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

export default {
    data() {
        return {
            search: '',
        };
    },

    computed: {
        height () {
            switch (this.$vuetify.breakpoint.name) {
            case 'xs': return 300;
            case 'sm': return 400;
            case 'md': return 400;
            case 'lg': return 500;
            case 'xl': return 500;
            }
            return 0;
        },
    },

    methods: {
        filterSearch() {
            // vuetifyのclearはnullが挿入される
            const query = `?search=${this.search || ''}`;
            const fullURL = `/search${query}`;
            this.$router.push(fullURL).catch(err => { console.log(err); });
        },
    }
};

</script>

<style>

.button {
  text-align: center;
}

</style>