-- SELECT * from Customer;
-- DROP TABLE Customer;
-- SELECT * FROM ContactPerson;
-- DROP TABLE ContactPerson;
-- SELECT * FROM InquiryItem;
-- INSERT INTO RelationshipDic VALUES ('zhtest','Test0');
-- SELECT * FROM RelationshipDic;
-- SELECT * FROM CustomerAndContactPerson;
-- DROP TABLE CustomerAndContactPerson;
-- SELECT * FROM Inquiry;
-- DROP TABLE Quotation;
-- SELECT * FROM InquiryItem;
-- INSERT INTO InquiryItem VALUES ('IN20210728150059682420','sb102','mat2',1,'EA',100);
-- SELECT * FROM MaterialDic;
-- INSERT INTO DiscountDic VALUES ('2','K004','A');
-- SELECT * FROM Quotation;
-- SELECT * FROM Quotationitem;
-- INSERT INTO Quotation VALUES ('QU112', 1000000, 'lz101', 123,'2021-07-21', '2021-07-21','2021-07-21', 'K004', '13','2021-07-21');
-- INSERT INTO Quotationitem VALUES ('QU000', 'sb102', 'mat2', 1, 'EA', 'K004', 10);
-- DROP TABLE DeliveryOrder;
-- SELECT * FROM SalesOrder;
-- SELECT * FROM SalesOrderItem;
-- SELECT * FROM Inventory;
-- INSERT INTO Inventory VALUES ('lz102', 'sb104', 1, 10, 10);
-- SELECT * FROM DeliveryOrderItem;
INSERT INTO Power VALUES (1,'ManageStock');
INSERT INTO Power VALUES (2,'ManageStock');
INSERT INTO Power VALUES (3,'ManageStock');
INSERT INTO Power VALUES (1,'CreateBPRelationship'),(1,'CreateInquiry'),(2,'CreateCustomer'),(2,'CreateContactPerson'),(2,'CreateQuotation'),(2,'CreateSalesOrder'),(2,'ManageBusinessPartner'),(2,'ManageSDDocument'),(3,'CreateOutboundDeliveries'),(3,'OutboundDeliveries'),(3,'PickingOutboundDelivery');
INSERT INTO User VALUES ('SuperManager', 'FightForERP', 10);
INSERT INTO RelationshipDic VALUES ('normal','Normal');
-- SELECT * FROM user;
-- SELECT * FROM SalesOrderItem;
-- SELECT * FROM SalesOrder;
-- DROP TABLE DeliveryOrderItem;
-- INSERT INTO DiscountDic VALUES ("DIs",'K004',"A");