<template>
    <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                fab
                color="#1DA1F2"
                :href="twitterShareURL"
                class="mx-12 my-sm-6"
                small
                dark
                target="_blank"
                rel="noopener noreferrer"
                right
                absolute
                elevation="0"
                :attrs="attrs"
                v-on="on"
            >
                <v-icon size="24px">
                    mdi-twitter
                </v-icon>
            </v-btn>
        </template>
        <span>Twitterでシェアする</span>
    </v-tooltip>
</template>

<script>
const protocol = process.env.VUE_APP_PROTOCOL;
const origin = 'inazo.hu-jagajaga.com';

const content = '成績分布検索サービス - iNAZO';
const hashtags = 'iNAZO_HU';

export default {
    props: {
        id: {
            type: Number,
            required: true,
        }
    },
    data() {
        return {
            text: `${content}%0a${protocol}://${origin}/detail/${this.id}`,
        };
    },
    computed: {
        twitterShareURL() {
            return `https://twitter.com/intent/tweet?text=${this.text}&hashtags=${hashtags}`;
        }
    }
};
</script>