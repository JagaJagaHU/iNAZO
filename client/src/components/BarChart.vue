<script>
import { Bar, mixins } from 'vue-chartjs';

export default {
    extends: Bar,
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
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            callback: function(value) { if (value % 1 === 0) { return value; } }
                        }
                    }]
                }
            });
    }
};
</script>