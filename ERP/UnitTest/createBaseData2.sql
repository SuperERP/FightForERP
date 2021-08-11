INSERT INTO Power VALUES (1,'ManageStock');
INSERT INTO Power VALUES (2,'ManageStock');
INSERT INTO Power VALUES (3,'ManageStock');
INSERT INTO Power VALUES (1,'CreateBPRelationship'),(1,'CreateInquiry'),(2,'CreateCustomer'),(2,'CreateContactPerson'),(2,'CreateQuotation'),(2,'CreateSalesOrder'),(2,'ManageBusinessPartner'),(2,'ManageSDDocument'),(3,'CreateOutboundDeliveries'),(3,'OutboundDeliveries'),(3,'PickingOutboundDelivery');
INSERT INTO User VALUES ('SuperManager', 'FightForERP', 10),('SalesMember', 'salesmember', 1), ('SalesManager', 'salesmanager', 2),('WarehouseKeeper', 'warehousekeeper', 3);
INSERT INTO RelationshipDic VALUES ('BUR001','Has Contact Person'),('BUR002','Has Activity Partner'),('BUR003','Has Shared Living Arrangement Member');

SELECT * FROM User;
SELECT * FROM Power;
SELECT * FROM RelationshipDic;
SELECT * FROM MaterialDic;
SELECT * FROM DiscountDic;
SELECT * FROM Warehouse;
SELECT * FROM Inventory;