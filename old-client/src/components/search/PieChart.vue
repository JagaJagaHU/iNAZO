<script>
import { Pie, mixins } from 'vue-chartjs';

export default {
    extends: Pie,
    mixins: [mixins.reactiveProp],
    props: {
        chartData: {
            type: Object,
            required: true,
        },
    },
    mounted () {
        this.renderChart(this.chartData,
            {
                responsive: true,
                maintainAspectRatio: false,
            });
    }
};
</script>