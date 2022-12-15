# Here are the explanation to insert the real data in the database.

## 1. connect to db

to connect to the database you will want to enter the following commands.
```
sudo mysql
```
Enter your password, and finally choose the stib database.
```
use stib;
```

## 2. create the new table

we will want to create the new table by running 
```
CREATE TABLE IF NOT EXISTS real_data (
date INT NOT NULL,
time VARCHAR(32) NOT NULL,
lineID TINYINT NOT NULL,
pointID SMALLINT NOT NULL,
distanceFromPoint SMALLINT NOT NULL,
directionID SMALLINT NOT NULL,
duplicates TINYINT NOT NULL,
PRIMARY KEY (date, time, lineID, pointID, distanceFromPoint, directionID, duplicates));
```
Once created check that the table has been properly added, run
```
show tables;
```
It should look something like this:

![show tables](../images/showtables.png "show tables")
## 3. insert data

Once the table is created, first make sure the file real_data.csv that you have downloaded from https://drive.google.com/file/d/1oQcW4CblZJnH2Ve86IrEqdZDCVIMc-6v/view?usp=sharing is in the mysql-files folder. 

His relative path should be : /var/lib/mysql-files/real_data.csv

we will now inster its data to fill the table by running :
```
LOAD DATA INFILE '/var/lib/mysql-files/real_data.csv'
INTO TABLE real_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

This should be the final input 

![data inserted](../images/data_inserted.png "data inserted")

```
with stop_sequence as  (select trip_id, GROUP_CONCAT(DISTINCT stop_id SEPARATOR ',') AS sequence from stop_times group by  trip_id ;)
```

stop_times_df = stop_times_df.groupby('trip_id')['stop_id'].apply(lambda x: x.tolist()).reset_index(name='stop_sequence')

route_stop_sequence_df = pd.merge(route_df, trips_df)

route_stop_sequence_df = pd.merge(route_stop_sequence_df, stop_times_df)

route_stop_sequence_df['route_name'] = route_stop_sequence_df['route_short_name'] + ' ' + route_stop_sequence_df['route_long_name']

route_stop_sequence_df['stop_sequence'] = route_stop_sequence_df['stop_sequence'].apply(lambda x: tuple(x))

route_stop_sequence_df = route_stop_sequence_df.groupby(['stop_sequence', 'route_id', 'route_short_name', 'route_name', 'route_type', 'route_color', 'shape_id'])['trip_id'].count().reset_index(name='count')

route_stop_sequence_df['stop_sequence'] = route_stop_sequence_df['stop_sequence'].apply(lambda x: list(x))

route_stop_sequence_df['route_short_name'] = route_stop_sequence_df['route_short_name'].apply(lambda x: int(x))

route_stop_sequence_df = route_stop_sequence_df.sort_values(by=['route_short_name', 'count'], ascending=[True, False])

route_stop_sequence_df = route_stop_sequence_df.groupby('route_short_name').head(1)