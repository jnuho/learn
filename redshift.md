

### Pricing


- Configurations
  - Subnet Groups > Choose VPC (subnet-2a,2c)
- Create IAM Role
  - Type: AWS Service
  - Use Case: Redshift customizable
  - Add Policy : AmazonRedshiftAllCommandsFullAccess
- Create Cluster
  - Endpoint: 
  - Database name: dev
  - Database port: 5439
  - User/Pw: krms/Kaon.1234
  - Security Group
    - outbound: all
    - inbound: 5439
  - Associate IAM Role



```sh
aws redshift modify-cluster-iam-roles \
--cluster-identifier redshift-cluster-1 \
--add-iam-roles arn:aws:iam::088356671508:role/amazonredshiftfullaccessbigdata

```


```sql
copy dev.public.part from 's3://krms-big-data/load/part-csv.tbl' credentials 'aws_iam_role=arn:aws:iam::088356671508:role/role-s3-to-redshift-and-vice-versa';

copy dev.public.part from 's3://krms-big-data/load/part-csv.tbl' credentials 'aws_iam_role=arn:aws:iam::088356671508:role/amazonredshiftfullaccessbigdata';
```


`jj`kj
[XX000] ERROR: exception name : UnauthorizedException, error type : 135, message: Not authorized to get credentials of role arn:aws:iam::088356671508:role/amazonredshiftfullaccessbigdata, should retry : 0 Detail: ----------------------------------------------- error: exception name : UnauthorizedException, error type : 135, message: Not authorized to get credentials of role arn:aws:iam::088356671508:role/amazonredshiftfullaccessbigdata, should retry : 0 code: 30



aws iam get-role --role-name ROLE_NAME
aws redshift describe-clusters redshift-cluster-1
aws redshift 
`
