# Generated by Django 3.0.7 on 2020-06-20 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200619_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdefinition',
            name='create_appctx',
        ),
        migrations.RemoveField(
            model_name='itemdefinition',
            name='updt_appctx',
        ),
        migrations.RemoveField(
            model_name='itemidentifier',
            name='updt_appctx',
        ),
        migrations.RemoveField(
            model_name='itemprice',
            name='create_appctx',
        ),
        migrations.RemoveField(
            model_name='itemprice',
            name='updt_appctx',
        ),
        migrations.AddField(
            model_name='itemdefinition',
            name='create_applabel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='itemdefinition',
            name='updt_applabel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='itemidentifier',
            name='updt_applabel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='itemprice',
            name='create_applabel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='itemprice',
            name='updt_applabel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='item_type_cd',
            field=models.CharField(choices=[('01', 'Instance'), ('02', 'Equipment Instance'), ('03', 'Equipment Master'), ('04', 'Equipment Group'), ('05', 'Manufacturer Item'), ('06', 'Item Master'), ('07', 'Vendor Item'), ('08', 'Lot Info'), ('09', 'Medication Definition'), ('10', 'Purchase Order'), ('11', 'Requisition'), ('12', 'General'), ('13', 'Produce')], default='12', max_length=2),
        ),
        migrations.CreateModel(
            name='ItemPriceHist',
            fields=[
                ('item_price_hist_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('active_ind', models.BooleanField(default=True, verbose_name='Active')),
                ('active_status_cd', models.CharField(choices=[('01', 'Active'), ('02', 'Combined'), ('03', 'Historical value - combined'), ('04', 'Deleted'), ('05', 'Draft'), ('06', 'Inactive'), ('07', 'Recall'), ('08', 'Review'), ('09', 'Suspended'), ('10', 'Unknown')], default='01', max_length=2)),
                ('active_status_dt_tm', models.DateTimeField(blank=True, null=True)),
                ('active_status_prsnl_id', models.BigIntegerField(blank=True, null=True)),
                ('contract_description', models.CharField(max_length=100)),
                ('contract_id', models.BigIntegerField(default=0)),
                ('contract_line_id', models.BigIntegerField(default=0)),
                ('contract_nbr', models.CharField(blank=True, max_length=40)),
                ('contract_type', models.CharField(blank=True, max_length=100)),
                ('contributor_system_cd', models.BigIntegerField(default=0)),
                ('create_applabel', models.CharField(blank=True, max_length=20)),
                ('create_dt_tm', models.DateTimeField(auto_now_add=True)),
                ('create_id', models.BigIntegerField(default=0)),
                ('create_task', models.BigIntegerField(default=0)),
                ('effective_dt_tm', models.DateTimeField(auto_now_add=True)),
                ('expiration_dt_tm', models.DateTimeField(blank=True, null=True)),
                ('fixed_price_ind', models.BooleanField(default=True, verbose_name='Price Fixed')),
                ('min_order_quantity', models.BigIntegerField(default=0)),
                ('order_qty_multiple', models.IntegerField(default=0)),
                ('organization_id', models.BigIntegerField(default=0)),
                ('package_type_id', models.BigIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_quote_source', models.CharField(blank=True, max_length=100)),
                ('price_type_cd', models.CharField(choices=[('01', 'Contract'), ('02', 'List'), ('03', 'Quote')], default='03', max_length=2)),
                ('updt_cnt', models.IntegerField(default=0)),
                ('updt_dt_tm', models.DateTimeField(auto_now_add=True)),
                ('updt_id', models.BigIntegerField(default=0)),
                ('updt_task', models.BigIntegerField(default=0)),
                ('updt_applabel', models.CharField(blank=True, max_length=20)),
                ('vendor_price_schedule_id', models.BigIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.ItemDefinition')),
                ('item_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.ItemPrice')),
            ],
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['item'], name='core_itempr_item_id_9826a8_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['item_price'], name='core_itempr_item_pr_6f68ed_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['contract_line_id'], name='core_itempr_contrac_da1781_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['organization_id'], name='core_itempr_organiz_eb5695_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['package_type_id'], name='core_itempr_package_6eca66_idx'),
        ),
    ]
