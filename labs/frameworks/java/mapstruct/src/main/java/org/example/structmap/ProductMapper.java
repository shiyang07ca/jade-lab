package org.example.structmap;

import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.factory.Mappers;

import static java.lang.System.out;

@Mapper
public interface ProductMapper {
    ProductMapper INSTANCE = Mappers.getMapper(ProductMapper.class);

    @Mapping(source = "price", target = "formattedPrice")
    ProductDto toDto(Product product);

    public static void main(String[] args) {
        Product product = new Product();
        out.println(product);
        ProductDto productDto = ProductMapper.INSTANCE.toDto(product);
        out.println(productDto);
    }
}
