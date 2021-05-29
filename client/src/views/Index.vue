<template>
    <v-container>
        <!-- top -->
        <v-row>
            <v-col>
                <v-parallax
                    class="mb-5 mb-sm-10"
                    src="@/assets/background-title.jpg"
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
                            sm="6"
                        >
                            <v-img
                                max-height="200"
                                max-width="500"
                                src="../assets/iNAZO_logo.png"
                            />
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
                                label="講義・教授・学部で検索する"
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
                        <p class="text-h6 text-center">
                            北大が公開している成績分布データをより扱いやすくしました。<br><br>
                            受けたい講義の過去の成績分布が知りたい <br>
                            気になる複数の講義の成績分布を比較したい <br>
                            自分が受講した講義の成績分布を知りたい <br>
                            そんなとき、あなたをお手伝いします。 <br><br>
                            iNAZOを使って取りたい成績をあなたのものにしよう。 <br>
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
                    color="#1976D2"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        シンプルな検索
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        簡潔で分かりやすい検索窓で講義を検索<br>
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
                    color="#1976D2"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        ブックマーク登録
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        気になる講義を登録してあなただけの一覧を<br>
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
                    color="#1976D2"
                    dark
                >
                    <p class="text-center text-h4 py-5">
                        ソート検索
                    </p>
                    <v-card-subtitle class="text-h6 pb-5">
                        表示順を変えることで知りたい情報を探しやすく
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
                    Q&A
                </p>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        Q. 誰が作っているのですか？
                    </p>
                    <p class="text-h6">
                        A. 北大生応援メディアの
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
                        Q. このサービスは大学公認ですか？
                    </p>
                    <p class="text-h6">
                        A. 非公認です。
                        <a
                            href="http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            データ参照先
                        </a>
                        の併用をお勧めします。
                    </p>
                </div>

                <div class="my-16">
                    <p class="text-h6 font-weight-bold">
                        Q. バグを見つけました。どうすればいいですか？
                    </p>
                    <p class="text-h6">
                        A. 見つけたバグを
                        <a
                            href="#"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            こちら
                        </a>
                        のGoogle Formで教えて下さると幸いです。
                        機能追加等の要望もお待ちしています。
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
                <p class="text-h6">
                    <a
                        href="https://twitter.com/iNAZO_HU"
                        target="_blank"
                        rel="noopener noreferrer"
                    >iNAZO公式Twitter</a>
                </p>
                <p>更新情報や障害情報をお知らせします。フォロー推薦です。お問い合わせはDMにお願いします。</p>
                <p>
                    <a
                        href="http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        北海道大学 成績分布ＷＥＢ公開システム
                    </a>
                </p>
                <p>データ参照先である北海道大学公式のサイトです。本サービスとの併用をお勧めします。</p>
                <p>
                    <a
                        href="http://hu-jagajaga.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                    >JagaJaga - 北大生応援メディア -</a>
                </p>
                <p>北大生目線の記事を掲載しています。ぜひご覧ください。</p>
                <p>
                    <a
                        href="https://twitter.com/jagajagahu"
                        target="_blank"
                        rel="noopener noreferrer"
                    >JagaJaga公式Twitter</a>
                </p>
                <p>北大生に届けたい情報を配信・いいね&RTしています。フォローお待ちしています。</p>
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