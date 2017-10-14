from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_2 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1F8",          # 01, 1
        "Function_2_2CB",          # 02, 2
        "Function_3_3C0",          # 03, 3
        "Function_4_4D2",          # 04, 4
        "Function_5_60F",          # 05, 5
        "Function_6_825",          # 06, 6
        "Function_7_9A2",          # 07, 7
        "Function_8_AAF",          # 08, 8
        "Function_9_B4E",          # 09, 9
        "Function_10_DB2",         # 0A, 10
        "Function_11_1175",        # 0B, 11
        "Function_12_1176",        # 0C, 12
        "Function_13_121E",        # 0D, 13
        "Function_14_1321",        # 0E, 14
        "Function_15_1410",        # 0F, 15
        "Function_16_14F2",        # 10, 16
        "Function_17_1500",        # 11, 17
        "Function_18_15E2",        # 12, 18
        "Function_19_16C4",        # 13, 19
        "Function_20_17A6",        # 14, 20
        "Function_21_1888",        # 15, 21
        "Function_22_196A",        # 16, 22
        "Function_23_1A4C",        # 17, 23
        "Function_24_1B2E",        # 18, 24
        "Function_25_1C10",        # 19, 25
        "Function_26_1CF2",        # 1A, 26
        "Function_27_1CF3",        # 1B, 27
        "Function_28_1DD5",        # 1C, 28
        "Function_29_1DD6",        # 1D, 29
        "Function_30_1EB8",        # 1E, 30
        "Function_31_201B",        # 1F, 31
        "Function_32_21C0",        # 20, 32
        "Function_33_22A2",        # 21, 33
        "Function_34_22A3",        # 22, 34
        "Function_35_239D",        # 23, 35
        "Function_36_24CE",        # 24, 36
        "Function_37_2593",        # 25, 37
        "Function_38_26D0",        # 26, 38
        "Function_39_27B2",        # 27, 39
        "Function_40_2925",        # 28, 40
        "Function_41_2A07",        # 29, 41
        "Function_42_2AE9",        # 2A, 42
        "Function_43_2BF2",        # 2B, 43
        "Function_44_2D1D",        # 2C, 44
        "Function_45_2DFF",        # 2D, 45
        "Function_46_2F55",        # 2E, 46
        "Function_47_30C8",        # 2F, 47
        "Function_48_31AA",        # 30, 48
        "Function_49_328C",        # 31, 49
        "Function_50_336E",        # 32, 50
        "Function_51_3450",        # 33, 51
        "Function_52_3532",        # 34, 52
        "Function_53_3614",        # 35, 53
        "Function_54_3844",        # 36, 54
        "Function_55_3A45",        # 37, 55
        "Function_56_3B09",        # 38, 56
        "Function_57_3C37",        # 39, 57
        "Function_58_3C38",        # 3A, 58
        "Function_59_3EB5",        # 3B, 59
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test\x01",                 # 0
            "Flying Feline\x01",        # 1
            "Helmet Crab\x01",          # 2
            "Flying Feline 3\x01",      # 3
            "Human Boss\x01",           # 4
            "Big Boss\x01",             # 5
            "Other Boss\x01",           # 6
            "Auto Battle\x01",          # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_146"),
        (1, "loc_156"),
        (2, "loc_166"),
        (3, "loc_176"),
        (4, "loc_186"),
        (5, "loc_18D"),
        (6, "loc_194"),
        (7, "loc_19B"),
        (SWITCH_DEFAULT, "loc_1A2"),
    )


    label("loc_146")

    Battle(0x466, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A5")

    label("loc_156")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A5")

    label("loc_166")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A5")

    label("loc_176")

    Battle(0x7D7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A5")

    label("loc_186")

    Call(2, 53)
    Jump("loc_1A5")

    label("loc_18D")

    Call(2, 54)
    Jump("loc_1A5")

    label("loc_194")

    Call(2, 55)
    Jump("loc_1A5")

    label("loc_19B")

    Call(2, 56)
    Jump("loc_1A5")

    label("loc_1A2")

    Jump("loc_1A5")

    label("loc_1A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1BC"),
        (SWITCH_DEFAULT, "loc_1E7"),
    )


    label("loc_1BC")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_1E7")

    label("loc_1E7")

    Jump("Function_0_AA")

    label("loc_1EA")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_1F8(): pass

    label("Function_1_1F8")


    AnonymousTalk(    #0
        "\x06Select a section.\x02",
    )


    label("loc_20D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BB")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test\x01",         # 0
            "Rolent\x01",       # 1
            "Bose\x01",         # 2
            "Ruan\x01",         # 3
            "Zeiss\x01",        # 4
            "Grancel\x01",      # 5
            "Others\x01",       # 6
            "Cancel\x01",       # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27D"),
        (1, "loc_284"),
        (2, "loc_28B"),
        (3, "loc_292"),
        (4, "loc_299"),
        (5, "loc_2A0"),
        (6, "loc_2A7"),
        (SWITCH_DEFAULT, "loc_2AE"),
    )


    label("loc_27D")

    Call(2, 2)
    Jump("loc_2B8")

    label("loc_284")

    Call(2, 3)
    Jump("loc_2B8")

    label("loc_28B")

    Call(2, 4)
    Jump("loc_2B8")

    label("loc_292")

    Call(2, 5)
    Jump("loc_2B8")

    label("loc_299")

    Call(2, 6)
    Jump("loc_2B8")

    label("loc_2A0")

    Call(2, 7)
    Jump("loc_2B8")

    label("loc_2A7")

    Call(2, 8)
    Jump("loc_2B8")

    label("loc_2AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B8")

    Jump("loc_20D")

    label("loc_2BB")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_1F8 end

    def Function_2_2CB(): pass

    label("Function_2_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B0")

    Menu(
        2,
        10,
        100,
        1,
        (
            "Map 1 BTTEST01\x01",      # 0
            "Map 2 BTTEST02\x01",      # 1
            "Map 3 BTTEST03\x01",      # 2
            "Map 4 BTTEST04\x01",      # 3
            "Map 5 BTTEST05\x01",      # 4
            "Cancel\x01",              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_353"),
        (1, "loc_363"),
        (2, "loc_373"),
        (3, "loc_383"),
        (4, "loc_393"),
        (SWITCH_DEFAULT, "loc_3A3"),
    )


    label("loc_353")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AD")

    label("loc_363")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AD")

    label("loc_373")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AD")

    label("loc_383")

    Battle(0x7DD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AD")

    label("loc_393")

    Battle(0x7DE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AD")

    label("loc_3A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AD")

    Jump("Function_2_2CB")

    label("loc_3B0")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_2CB end

    def Function_3_3C0(): pass

    label("Function_3_3C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4")

    AnonymousTalk(    #1
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC0700 Tower Altered Space\x01",           # 0
            "BC0701 Tower Altered Space Roof\x01",      # 1
            "BT0400 Perzel Farm (Fog)\x01",             # 2
            "BC0403 Tower\x01",                         # 3
            "Cancel\x01",                               # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46B"),
        (1, "loc_47B"),
        (2, "loc_48B"),
        (3, "loc_4A7"),
        (SWITCH_DEFAULT, "loc_4B7"),
    )


    label("loc_46B")

    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4C1")

    label("loc_47B")

    Battle(0x456, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4C1")

    label("loc_48B")

    OP_C4(0x0, 0x4)
    Battle(0x799, 0x0, 0x0, 0x0, 0xFF)
    OP_C4(0x1, 0x4)
    Jump("loc_4C1")

    label("loc_4A7")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4C1")

    label("loc_4B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C1")

    Jump("Function_3_3C0")

    label("loc_4C4")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_3C0 end

    def Function_4_4D2(): pass

    label("Function_4_4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")

    AnonymousTalk(    #2
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC1601 Dragon's Dwelling\x01",             # 0
            "BC1603 Dragon's Dwelling Boss\x01",        # 1
            "BC1700 Tower Altered Space\x01",           # 2
            "BC1701 Tower Altered Space Boss\x01",      # 3
            "BC1203 Tower Boss\x01",                    # 4
            "Cancel\x01",                               # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B4"),
        (2, "loc_5C4"),
        (3, "loc_5D4"),
        (4, "loc_5E4"),
        (SWITCH_DEFAULT, "loc_5F4"),
    )


    label("loc_5A4")

    Battle(0x3C7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5FE")

    label("loc_5B4")

    Battle(0x44F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5FE")

    label("loc_5C4")

    Battle(0x3F4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5FE")

    label("loc_5D4")

    Battle(0x457, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5FE")

    label("loc_5E4")

    Battle(0x93, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5FE")

    label("loc_5F4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FE")

    Jump("Function_4_4D2")

    label("loc_601")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_4D2 end

    def Function_5_60F(): pass

    label("Function_5_60F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_817")

    AnonymousTalk(    #3
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC2300 Tower Altered Space\x01",                # 0
            "BC2301 Tower Altered Space Boss\x01",           # 1
            "BC2400 Old Schoolhouse Basement\x01",           # 2
            "BC2401 Old Schoolhouse Basement Boss\x01",      # 3
            "BC2500 Schoolyard\x01",                         # 4
            "BC2510 Schoolhouse Hall\x01",                   # 5
            "BC2511 Boys' Dorm\x01",                         # 6
            "BC2512 Girls' Dorm\x01",                        # 7
            "BT2611 Old Schoolhouse (Day)\x01",              # 8
            "BC2102 Tower\x01",                              # 9
            "Cancel\x01",                                    # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76A"),
        (1, "loc_77A"),
        (2, "loc_78A"),
        (3, "loc_79A"),
        (4, "loc_7AA"),
        (5, "loc_7BA"),
        (6, "loc_7CA"),
        (7, "loc_7DA"),
        (8, "loc_7EA"),
        (9, "loc_7FA"),
        (SWITCH_DEFAULT, "loc_80A"),
    )


    label("loc_76A")

    Battle(0x407, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_77A")

    Battle(0x454, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_78A")

    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_79A")

    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7AA")

    Battle(0xF3C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7BA")

    Battle(0x79C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7CA")

    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7DA")

    Battle(0x79F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7EA")

    Battle(0xF40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7FA")

    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_80A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_814")

    Jump("Function_5_60F")

    label("loc_817")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_60F end

    def Function_6_825(): pass

    label("Function_6_825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_994")

    AnonymousTalk(    #4
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC3600 Tower Altered Space\x01",           # 0
            "BC3601 Tower Altered Space Boss\x01",      # 1
            "BC3400 Hot Spring\x01",                    # 2
            "BC3401 Hot Spring Boss\x01",               # 3
            "BT0600 Gurune Gate\x01",                   # 4
            "BC3101 Leiston Fortress\x01",              # 5
            "BC3503 Tower\x01",                         # 6
            "Cancel\x01",                               # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_917"),
        (1, "loc_927"),
        (2, "loc_937"),
        (3, "loc_947"),
        (4, "loc_957"),
        (5, "loc_967"),
        (6, "loc_977"),
        (SWITCH_DEFAULT, "loc_987"),
    )


    label("loc_917")

    Battle(0x412, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_927")

    Battle(0x455, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_937")

    Battle(0x3B0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_947")

    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_957")

    Battle(0x45A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_967")

    Battle(0xC80, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_977")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_991")

    label("loc_987")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_991")

    Jump("Function_6_825")

    label("loc_994")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_825 end

    def Function_7_9A2(): pass

    label("Function_7_9A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA1")

    AnonymousTalk(    #5
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BT4403 Wharf Boss\x01",           # 0
            "BT4404 Wharf\x01",                # 1
            "BT4405 Wharf Warehouse\x01",      # 2
            "BT4100 Town\x01",                 # 3
            "BT4200 Drawbridge\x01",           # 4
            "Cancel\x01",                      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A44"),
        (1, "loc_A54"),
        (2, "loc_A64"),
        (3, "loc_A74"),
        (4, "loc_A84"),
        (SWITCH_DEFAULT, "loc_A94"),
    )


    label("loc_A44")

    Battle(0x45E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9E")

    label("loc_A54")

    Battle(0x45D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9E")

    label("loc_A64")

    Battle(0x45C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9E")

    label("loc_A74")

    Battle(0x79E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9E")

    label("loc_A84")

    Battle(0x550, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9E")

    label("loc_A94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9E")

    Jump("Function_7_9A2")

    label("loc_AA1")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_9A2 end

    def Function_8_AAF(): pass

    label("Function_8_AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")

    AnonymousTalk(    #6
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Le-Locle, Laboratory, Glorious\x01",      # 0
            "Axis Pillar, Aureole\x01",                # 1
            "Cancel\x01",                              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B25"),
        (1, "loc_B2C"),
        (SWITCH_DEFAULT, "loc_B33"),
    )


    label("loc_B25")

    Call(2, 9)
    Jump("loc_B3D")

    label("loc_B2C")

    Call(2, 10)
    Jump("loc_B3D")

    label("loc_B33")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B3D")

    Jump("Function_8_AAF")

    label("loc_B40")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_AAF end

    def Function_9_B4E(): pass

    label("Function_9_B4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA4")

    AnonymousTalk(    #7
        "\x06Select a map.\x02",
    )


    Menu(
        3,
        10,
        80,
        1,
        (
            "BT5110 Le-Locle Lodge\x01",               # 0
            "BC5500 Balstar Channel\x01",              # 1
            "BC5501 Balstar Channel Boss\x01",         # 2
            "BC5502 Saint-Croix Forest\x01",           # 3
            "BC5503 Saint-Croix Forest Boss\x01",      # 4
            "BC5504 Grimsel Fortress\x01",             # 5
            "BC5505 Grimsel Fortress Boss\x01",        # 6
            "BC5610 Laboratory\x01",                   # 7
            "BC5611 Laboratory Hall\x01",              # 8
            "BC5400 Glorious Hall\x01",                # 9
            "BC5408 Glorious Deck\x01",                # 10
            "BC5406 Glorious Boss\x01",                # 11
            "Cancel\x01",                              # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CD7"),
        (1, "loc_CE7"),
        (2, "loc_CF7"),
        (3, "loc_D07"),
        (4, "loc_D17"),
        (5, "loc_D27"),
        (6, "loc_D37"),
        (7, "loc_D47"),
        (8, "loc_D57"),
        (9, "loc_D67"),
        (10, "loc_D77"),
        (11, "loc_D87"),
        (SWITCH_DEFAULT, "loc_D97"),
    )


    label("loc_CD7")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_CE7")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_CF7")

    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D07")

    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D17")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D27")

    Battle(0x38D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D37")

    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D47")

    Battle(0x41A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D57")

    Battle(0x41C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D67")

    Battle(0x427, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D77")

    Battle(0x428, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D87")

    Battle(0x429, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_DA1")

    label("loc_D97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA1")

    Jump("Function_9_B4E")

    label("loc_DA4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_B4E end

    def Function_10_DB2(): pass

    label("Function_10_DB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1167")

    AnonymousTalk(    #8
        "\x06Select a map.\x02",
    )


    Menu(
        3,
        10,
        80,
        1,
        (
            "BC5800 Aureole Residential Block (Event)\x01",               # 0
            "BC5702 Aureole Industrial Block (Event)\x01",                # 1
            "BC5200 Aureole Tunnels 1 to Residential Block\x01",          # 2
            "BC5201 Aureole Tunnels 2 to Industrial Block\x01",           # 3
            "BC5202 Aureole Tunnels 3 to Axis Pillar\x01",                # 4
            "BC5203 Aureole Tunnels 4 to Park Block\x01",                 # 5
            "BC5300 Axis Pillar\x01",                                     # 6
            "BC5301 Axis Pillar Midboss 1\x01",                           # 7
            "BC5302 Axis Pillar Midboss 2\x01",                           # 8
            "BC5303 Axis Pillar Loewe\x01",                               # 9
            "BC5304 Axis Pillar Elevator\x01",                            # 10
            "BC5305 Axis Pillar Boss Weissmann\x01",                      # 11
            "BC5306 Axis Pillar Boss Weissmann (Altered Space)\x01",      # 12
            "BC5100 Axis Pillar Exterior\x01",                            # 13
            "BC5801 Aureole Residential Block\x01",                       # 14
            "BC5700 Aureole Industrial Block\x01",                        # 15
            "Cancel\x01",                                                 # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_105A"),
        (1, "loc_106A"),
        (2, "loc_107A"),
        (3, "loc_108A"),
        (4, "loc_109A"),
        (5, "loc_10AA"),
        (6, "loc_10BA"),
        (7, "loc_10CA"),
        (8, "loc_10DA"),
        (9, "loc_10EA"),
        (10, "loc_10FA"),
        (11, "loc_110A"),
        (12, "loc_111A"),
        (13, "loc_112A"),
        (14, "loc_113A"),
        (15, "loc_114A"),
        (SWITCH_DEFAULT, "loc_115A"),
    )


    label("loc_105A")

    Battle(0x50B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_106A")

    Battle(0x518, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_107A")

    Battle(0x43A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_108A")

    Battle(0x440, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_109A")

    Battle(0x449, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10AA")

    Battle(0x43D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10BA")

    Battle(0x508, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10CA")

    Battle(0x509, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10DA")

    Battle(0x50A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10EA")

    Battle(0x458, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_10FA")

    Battle(0x450, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_110A")

    Battle(0x459, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_111A")

    Battle(0x452, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_112A")

    Battle(0x525, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_113A")

    Battle(0x50E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_114A")

    Battle(0x514, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1164")

    label("loc_115A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1164")

    Jump("Function_10_DB2")

    label("loc_1167")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_DB2 end

    def Function_11_1175(): pass

    label("Function_11_1175")

    Return()

    # Function_11_1175 end

    def Function_12_1176(): pass

    label("Function_12_1176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1210")

    AnonymousTalk(    #9
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",      # 0
            "C0100_02\x01",      # 1
            "C0100_03\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11D3"),
        (1, "loc_11E3"),
        (2, "loc_11F3"),
        (SWITCH_DEFAULT, "loc_1203"),
    )


    label("loc_11D3")

    Battle(0x56, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_120D")

    label("loc_11E3")

    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_120D")

    label("loc_11F3")

    Battle(0x58, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_120D")

    label("loc_1203")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_120D")

    Jump("Function_12_1176")

    label("loc_1210")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1176 end

    def Function_13_121E(): pass

    label("Function_13_121E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1313")

    AnonymousTalk(    #10
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",          # 0
            "C0100_02\x01",          # 1
            "C0100_03\x01",          # 2
            "C0100_20\x01",          # 3
            "C0100_11\x01",          # 4
            "BTL_EVENT001\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A6"),
        (1, "loc_12B6"),
        (2, "loc_12C6"),
        (3, "loc_12D6"),
        (4, "loc_12E6"),
        (5, "loc_12F6"),
        (SWITCH_DEFAULT, "loc_1306"),
    )


    label("loc_12A6")

    Battle(0x3E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_12B6")

    Battle(0x3F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_12C6")

    Battle(0x40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_12D6")

    Battle(0x51, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_12E6")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_12F6")

    Battle(0x76D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1310")

    label("loc_1306")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1310")

    Jump("Function_13_121E")

    label("loc_1313")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_121E end

    def Function_14_1321(): pass

    label("Function_14_1321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1402")

    AnonymousTalk(    #11
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0400_01\x01",          # 0
            "C0400_02\x01",          # 1
            "C0400_07\x01",          # 2
            "C0400_13\x01",          # 3
            "C0400_10\x01",          # 4
            "BTL_EVENT002\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13A5"),
        (1, "loc_13B5"),
        (2, "loc_13C5"),
        (3, "loc_13D5"),
        (4, "loc_13E5"),
        (SWITCH_DEFAULT, "loc_13F5"),
    )


    label("loc_13A5")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_13FF")

    label("loc_13B5")

    Battle(0x32, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_13FF")

    label("loc_13C5")

    Battle(0x37, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_13FF")

    label("loc_13D5")

    Battle(0x3D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_13FF")

    label("loc_13E5")

    Battle(0x3A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_13FF")

    label("loc_13F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13FF")

    Jump("Function_14_1321")

    label("loc_1402")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_1321 end

    def Function_15_1410(): pass

    label("Function_15_1410")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E4")

    AnonymousTalk(    #12
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0100_02\x01",      # 0
            "R0100_05\x01",      # 1
            "R0100_09\x01",      # 2
            "R0100_11\x01",      # 3
            "R0100_14\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1487"),
        (1, "loc_1497"),
        (2, "loc_14A7"),
        (3, "loc_14B7"),
        (4, "loc_14C7"),
        (SWITCH_DEFAULT, "loc_14D7"),
    )


    label("loc_1487")

    Battle(0x15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14E1")

    label("loc_1497")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14E1")

    label("loc_14A7")

    Battle(0x1C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14E1")

    label("loc_14B7")

    Battle(0x1E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14E1")

    label("loc_14C7")

    Battle(0x21, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14E1")

    label("loc_14D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14E1")

    Jump("Function_15_1410")

    label("loc_14E4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1410 end

    def Function_16_14F2(): pass

    label("Function_16_14F2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_14F2 end

    def Function_17_1500(): pass

    label("Function_17_1500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D4")

    AnonymousTalk(    #13
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0300_02\x01",      # 0
            "R0300_06\x01",      # 1
            "R0300_09\x01",      # 2
            "R0300_12\x01",      # 3
            "R0300_17\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1577"),
        (1, "loc_1587"),
        (2, "loc_1597"),
        (3, "loc_15A7"),
        (4, "loc_15B7"),
        (SWITCH_DEFAULT, "loc_15C7"),
    )


    label("loc_1577")

    Battle(0x65, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15D1")

    label("loc_1587")

    Battle(0x69, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15D1")

    label("loc_1597")

    Battle(0x6C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15D1")

    label("loc_15A7")

    Battle(0x6F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15D1")

    label("loc_15B7")

    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15D1")

    label("loc_15C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D1")

    Jump("Function_17_1500")

    label("loc_15D4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1500 end

    def Function_18_15E2(): pass

    label("Function_18_15E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B6")

    AnonymousTalk(    #14
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0500_01\x01",      # 0
            "C0500_02\x01",      # 1
            "C0500_03\x01",      # 2
            "C0500_04\x01",      # 3
            "C0500_07\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1659"),
        (1, "loc_1669"),
        (2, "loc_1679"),
        (3, "loc_1689"),
        (4, "loc_1699"),
        (SWITCH_DEFAULT, "loc_16A9"),
    )


    label("loc_1659")

    Battle(0x2A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_16B3")

    label("loc_1669")

    Battle(0x2B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_16B3")

    label("loc_1679")

    Battle(0x2C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_16B3")

    label("loc_1689")

    Battle(0x2D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_16B3")

    label("loc_1699")

    Battle(0x30, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_16B3")

    label("loc_16A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16B3")

    Jump("Function_18_15E2")

    label("loc_16B6")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_15E2 end

    def Function_19_16C4(): pass

    label("Function_19_16C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1798")

    AnonymousTalk(    #15
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1300_01\x01",      # 0
            "C1300_02\x01",      # 1
            "C1300_03\x01",      # 2
            "C1300_04\x01",      # 3
            "C1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_173B"),
        (1, "loc_174B"),
        (2, "loc_175B"),
        (3, "loc_176B"),
        (4, "loc_177B"),
        (SWITCH_DEFAULT, "loc_178B"),
    )


    label("loc_173B")

    Battle(0xA1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1795")

    label("loc_174B")

    Battle(0xA2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1795")

    label("loc_175B")

    Battle(0xA3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1795")

    label("loc_176B")

    Battle(0xA4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1795")

    label("loc_177B")

    Battle(0xA5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1795")

    label("loc_178B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1795")

    Jump("Function_19_16C4")

    label("loc_1798")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_16C4 end

    def Function_20_17A6(): pass

    label("Function_20_17A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_187A")

    AnonymousTalk(    #16
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400_01\x01",      # 0
            "C1400_02\x01",      # 1
            "C1400_03\x01",      # 2
            "C1400_04\x01",      # 3
            "C1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_181D"),
        (1, "loc_182D"),
        (2, "loc_183D"),
        (3, "loc_184D"),
        (4, "loc_185D"),
        (SWITCH_DEFAULT, "loc_186D"),
    )


    label("loc_181D")

    Battle(0xB5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1877")

    label("loc_182D")

    Battle(0xB6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1877")

    label("loc_183D")

    Battle(0xB7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1877")

    label("loc_184D")

    Battle(0xB8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1877")

    label("loc_185D")

    Battle(0xB9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1877")

    label("loc_186D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1877")

    Jump("Function_20_17A6")

    label("loc_187A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_17A6 end

    def Function_21_1888(): pass

    label("Function_21_1888")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195C")

    AnonymousTalk(    #17
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500_01\x01",      # 0
            "C1500_02\x01",      # 1
            "C1500_03\x01",      # 2
            "C1500_04\x01",      # 3
            "C1500_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18FF"),
        (1, "loc_190F"),
        (2, "loc_191F"),
        (3, "loc_192F"),
        (4, "loc_193F"),
        (SWITCH_DEFAULT, "loc_194F"),
    )


    label("loc_18FF")

    Battle(0xC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1959")

    label("loc_190F")

    Battle(0xCA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1959")

    label("loc_191F")

    Battle(0xCB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1959")

    label("loc_192F")

    Battle(0xCC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1959")

    label("loc_193F")

    Battle(0xCD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1959")

    label("loc_194F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1959")

    Jump("Function_21_1888")

    label("loc_195C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_1888 end

    def Function_22_196A(): pass

    label("Function_22_196A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3E")

    AnonymousTalk(    #18
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1100_01\x01",      # 0
            "R1100_02\x01",      # 1
            "R1100_20\x01",      # 2
            "R1100_04\x01",      # 3
            "R1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19E1"),
        (1, "loc_19F1"),
        (2, "loc_1A01"),
        (3, "loc_1A11"),
        (4, "loc_1A21"),
        (SWITCH_DEFAULT, "loc_1A31"),
    )


    label("loc_19E1")

    Battle(0xDD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A3B")

    label("loc_19F1")

    Battle(0xDE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A3B")

    label("loc_1A01")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A3B")

    label("loc_1A11")

    Battle(0xE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A3B")

    label("loc_1A21")

    Battle(0xE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A3B")

    label("loc_1A31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A3B")

    Jump("Function_22_196A")

    label("loc_1A3E")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_196A end

    def Function_23_1A4C(): pass

    label("Function_23_1A4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B20")

    AnonymousTalk(    #19
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1200_01\x01",      # 0
            "R1200_02\x01",      # 1
            "R1200_03\x01",      # 2
            "R1200_04\x01",      # 3
            "R1200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AC3"),
        (1, "loc_1AD3"),
        (2, "loc_1AE3"),
        (3, "loc_1AF3"),
        (4, "loc_1B03"),
        (SWITCH_DEFAULT, "loc_1B13"),
    )


    label("loc_1AC3")

    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B1D")

    label("loc_1AD3")

    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B1D")

    label("loc_1AE3")

    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B1D")

    label("loc_1AF3")

    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B1D")

    label("loc_1B03")

    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B1D")

    label("loc_1B13")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B1D")

    Jump("Function_23_1A4C")

    label("loc_1B20")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_1A4C end

    def Function_24_1B2E(): pass

    label("Function_24_1B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C02")

    AnonymousTalk(    #20
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1300_01\x01",      # 0
            "R1300_02\x01",      # 1
            "R1300_03\x01",      # 2
            "R1300_04\x01",      # 3
            "R1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BA5"),
        (1, "loc_1BB5"),
        (2, "loc_1BC5"),
        (3, "loc_1BD5"),
        (4, "loc_1BE5"),
        (SWITCH_DEFAULT, "loc_1BF5"),
    )


    label("loc_1BA5")

    Battle(0x105, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BFF")

    label("loc_1BB5")

    Battle(0x106, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BFF")

    label("loc_1BC5")

    Battle(0x107, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BFF")

    label("loc_1BD5")

    Battle(0x108, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BFF")

    label("loc_1BE5")

    Battle(0x109, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BFF")

    label("loc_1BF5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BFF")

    Jump("Function_24_1B2E")

    label("loc_1C02")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_1B2E end

    def Function_25_1C10(): pass

    label("Function_25_1C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE4")

    AnonymousTalk(    #21
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1400_01\x01",      # 0
            "R1400_02\x01",      # 1
            "R1400_03\x01",      # 2
            "R1400_04\x01",      # 3
            "R1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C87"),
        (1, "loc_1C97"),
        (2, "loc_1CA7"),
        (3, "loc_1CB7"),
        (4, "loc_1CC7"),
        (SWITCH_DEFAULT, "loc_1CD7"),
    )


    label("loc_1C87")

    Battle(0x119, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE1")

    label("loc_1C97")

    Battle(0x11A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE1")

    label("loc_1CA7")

    Battle(0x11B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE1")

    label("loc_1CB7")

    Battle(0x11C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE1")

    label("loc_1CC7")

    Battle(0x11D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE1")

    label("loc_1CD7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CE1")

    Jump("Function_25_1C10")

    label("loc_1CE4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_1C10 end

    def Function_26_1CF2(): pass

    label("Function_26_1CF2")

    Return()

    # Function_26_1CF2 end

    def Function_27_1CF3(): pass

    label("Function_27_1CF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC7")

    AnonymousTalk(    #22
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1100_01\x01",      # 0
            "C1100_02\x01",      # 1
            "C1100_03\x01",      # 2
            "C1100_04\x01",      # 3
            "C1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D6A"),
        (1, "loc_1D7A"),
        (2, "loc_1D8A"),
        (3, "loc_1D9A"),
        (4, "loc_1DAA"),
        (SWITCH_DEFAULT, "loc_1DBA"),
    )


    label("loc_1D6A")

    Battle(0x141, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC4")

    label("loc_1D7A")

    Battle(0x142, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC4")

    label("loc_1D8A")

    Battle(0x143, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC4")

    label("loc_1D9A")

    Battle(0x144, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC4")

    label("loc_1DAA")

    Battle(0x145, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC4")

    label("loc_1DBA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DC4")

    Jump("Function_27_1CF3")

    label("loc_1DC7")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_1CF3 end

    def Function_28_1DD5(): pass

    label("Function_28_1DD5")

    Return()

    # Function_28_1DD5 end

    def Function_29_1DD6(): pass

    label("Function_29_1DD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAA")

    AnonymousTalk(    #23
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2100_01\x01",      # 0
            "R2100_02\x01",      # 1
            "R2100_03\x01",      # 2
            "R2100_04\x01",      # 3
            "R2100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E4D"),
        (1, "loc_1E5D"),
        (2, "loc_1E6D"),
        (3, "loc_1E7D"),
        (4, "loc_1E8D"),
        (SWITCH_DEFAULT, "loc_1E9D"),
    )


    label("loc_1E4D")

    Battle(0x169, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EA7")

    label("loc_1E5D")

    Battle(0x16A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EA7")

    label("loc_1E6D")

    Battle(0x16B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EA7")

    label("loc_1E7D")

    Battle(0x16C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EA7")

    label("loc_1E8D")

    Battle(0x16D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EA7")

    label("loc_1E9D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EA7")

    Jump("Function_29_1DD6")

    label("loc_1EAA")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_1DD6 end

    def Function_30_1EB8(): pass

    label("Function_30_1EB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200D")

    AnonymousTalk(    #24
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2200_01 Main\x01",                 # 0
            "R2200_02\x01",                      # 1
            "R2201_01 Beach\x01",                # 2
            "R2201_02\x01",                      # 3
            "R2202_01 Main (Evening)\x01",       # 4
            "R2202_02\x01",                      # 5
            "R2203_01 Beach (Evening)\x01",      # 6
            "R2203_02\x01",                      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F80"),
        (1, "loc_1F90"),
        (2, "loc_1FA0"),
        (3, "loc_1FB0"),
        (4, "loc_1FC0"),
        (5, "loc_1FD0"),
        (6, "loc_1FE0"),
        (7, "loc_1FF0"),
        (SWITCH_DEFAULT, "loc_2000"),
    )


    label("loc_1F80")

    Battle(0x17D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1F90")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FA0")

    Battle(0x187, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FB0")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FC0")

    Battle(0x321, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FD0")

    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FE0")

    Battle(0x32B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_1FF0")

    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_200A")

    label("loc_2000")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_200A")

    Jump("Function_30_1EB8")

    label("loc_200D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_1EB8 end

    def Function_31_201B(): pass

    label("Function_31_201B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B2")

    AnonymousTalk(    #25
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2300_01\x01",                # 0
            "R2300_02\x01",                # 1
            "R2300_03\x01",                # 2
            "R2300_04\x01",                # 3
            "R2300_05\x01",                # 4
            "R2301_01 (Evening)\x01",      # 5
            "R2301_02 (Evening)\x01",      # 6
            "R2301_03 (Evening)\x01",      # 7
            "R2301_04 (Evening)\x01",      # 8
            "R2301_05 (Evening)\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2105"),
        (1, "loc_2115"),
        (2, "loc_2125"),
        (3, "loc_2135"),
        (4, "loc_2145"),
        (5, "loc_2155"),
        (6, "loc_2165"),
        (7, "loc_2175"),
        (8, "loc_2185"),
        (9, "loc_2195"),
        (SWITCH_DEFAULT, "loc_21A5"),
    )


    label("loc_2105")

    Battle(0x191, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2115")

    Battle(0x192, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2125")

    Battle(0x193, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2135")

    Battle(0x194, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2145")

    Battle(0x195, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2155")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2165")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2175")

    Battle(0x337, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2185")

    Battle(0x338, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_2195")

    Battle(0x339, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_21AF")

    label("loc_21A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21AF")

    Jump("Function_31_201B")

    label("loc_21B2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_201B end

    def Function_32_21C0(): pass

    label("Function_32_21C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2294")

    AnonymousTalk(    #26
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2400_01\x01",      # 0
            "R2400_02\x01",      # 1
            "R2400_03\x01",      # 2
            "R2400_04\x01",      # 3
            "R2400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2237"),
        (1, "loc_2247"),
        (2, "loc_2257"),
        (3, "loc_2267"),
        (4, "loc_2277"),
        (SWITCH_DEFAULT, "loc_2287"),
    )


    label("loc_2237")

    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2291")

    label("loc_2247")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2291")

    label("loc_2257")

    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2291")

    label("loc_2267")

    Battle(0x1A8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2291")

    label("loc_2277")

    Battle(0x1A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2291")

    label("loc_2287")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2291")

    Jump("Function_32_21C0")

    label("loc_2294")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_21C0 end

    def Function_33_22A2(): pass

    label("Function_33_22A2")

    Return()

    # Function_33_22A2 end

    def Function_34_22A3(): pass

    label("Function_34_22A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238F")

    AnonymousTalk(    #27
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "BTL_EVENT011 (Deen)\x01",              # 0
            "BTL_EVENT012 (Rais)\x01",              # 1
            "BTL_EVENT013 (Rocco)\x01",             # 2
            "BTL_EVENT014 (Man in Black)\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2342"),
        (1, "loc_2352"),
        (2, "loc_2362"),
        (3, "loc_2372"),
        (SWITCH_DEFAULT, "loc_2382"),
    )


    label("loc_2342")

    Battle(0x777, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_238C")

    label("loc_2352")

    Battle(0x778, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_238C")

    label("loc_2362")

    Battle(0x779, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_238C")

    label("loc_2372")

    Battle(0x77A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_238C")

    label("loc_2382")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_238C")

    Jump("Function_34_22A3")

    label("loc_238F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_22A3 end

    def Function_35_239D(): pass

    label("Function_35_239D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C0")

    AnonymousTalk(    #28
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Kaldia Tunnel\x01",              # 0
            "Kaldia Limestone Cave\x01",      # 1
            "Tower\x01",                      # 2
            "Tratt Plains Road\x01",          # 3
            "Ritter Roadway\x01",             # 4
            "Soldat Army Road\x01",           # 5
            "Leiston Fortress\x01",           # 6
            "Tower (Event)\x01",              # 7
            "Cancel\x01",                     # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2472"),
        (1, "loc_2479"),
        (2, "loc_2480"),
        (3, "loc_2487"),
        (4, "loc_248E"),
        (5, "loc_2495"),
        (6, "loc_249C"),
        (7, "loc_24A3"),
        (SWITCH_DEFAULT, "loc_24B3"),
    )


    label("loc_2472")

    Call(2, 36)
    Jump("loc_24BD")

    label("loc_2479")

    Call(2, 37)
    Jump("loc_24BD")

    label("loc_2480")

    Call(2, 38)
    Jump("loc_24BD")

    label("loc_2487")

    Call(2, 39)
    Jump("loc_24BD")

    label("loc_248E")

    Call(2, 40)
    Jump("loc_24BD")

    label("loc_2495")

    Call(2, 41)
    Jump("loc_24BD")

    label("loc_249C")

    Call(2, 42)
    Jump("loc_24BD")

    label("loc_24A3")

    Battle(0x788, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BD")

    label("loc_24B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24BD")

    Jump("Function_35_239D")

    label("loc_24C0")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_239D end

    def Function_36_24CE(): pass

    label("Function_36_24CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2585")

    AnonymousTalk(    #29
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3400_01\x01",      # 0
            "R3400_02\x01",      # 1
            "R3400_03\x01",      # 2
            "R3400_04\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2538"),
        (1, "loc_2548"),
        (2, "loc_2558"),
        (3, "loc_2568"),
        (SWITCH_DEFAULT, "loc_2578"),
    )


    label("loc_2538")

    Battle(0x1CD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2582")

    label("loc_2548")

    Battle(0x1CE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2582")

    label("loc_2558")

    Battle(0x1CF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2582")

    label("loc_2568")

    Battle(0x1D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2582")

    label("loc_2578")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2582")

    Jump("Function_36_24CE")

    label("loc_2585")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_24CE end

    def Function_37_2593(): pass

    label("Function_37_2593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C2")

    AnonymousTalk(    #30
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3300_01\x01",          # 0
            "C3300_02\x01",          # 1
            "C3300_03\x01",          # 2
            "C3300_04\x01",          # 3
            "C3300_05\x01",          # 4
            "C3300_06\x01",          # 5
            "C3300_07\x01",          # 6
            "BTL_EVENT020\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2635"),
        (1, "loc_2645"),
        (2, "loc_2655"),
        (3, "loc_2665"),
        (4, "loc_2675"),
        (5, "loc_2685"),
        (6, "loc_2695"),
        (7, "loc_26A5"),
        (SWITCH_DEFAULT, "loc_26B5"),
    )


    label("loc_2635")

    Battle(0x1E1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2645")

    Battle(0x1E2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2655")

    Battle(0x1E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2665")

    Battle(0x1E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2675")

    Battle(0x1E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2685")

    Battle(0x1E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_2695")

    Battle(0x1E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_26A5")

    Battle(0x780, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26BF")

    label("loc_26B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26BF")

    Jump("Function_37_2593")

    label("loc_26C2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_2593 end

    def Function_38_26D0(): pass

    label("Function_38_26D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27A4")

    AnonymousTalk(    #31
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3511_01\x01",      # 0
            "C3511_02\x01",      # 1
            "C3511_03\x01",      # 2
            "C3511_04\x01",      # 3
            "C3511_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2747"),
        (1, "loc_2757"),
        (2, "loc_2767"),
        (3, "loc_2777"),
        (4, "loc_2787"),
        (SWITCH_DEFAULT, "loc_2797"),
    )


    label("loc_2747")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27A1")

    label("loc_2757")

    Battle(0x1F6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27A1")

    label("loc_2767")

    Battle(0x1F7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27A1")

    label("loc_2777")

    Battle(0x1F8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27A1")

    label("loc_2787")

    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27A1")

    label("loc_2797")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27A1")

    Jump("Function_38_26D0")

    label("loc_27A4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_26D0 end

    def Function_39_27B2(): pass

    label("Function_39_27B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2917")

    AnonymousTalk(    #32
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3100_01\x01",      # 0
            "R3100_02\x01",      # 1
            "R3100_03\x01",      # 2
            "R3100_04\x01",      # 3
            "R3101_05\x01",      # 4
            "R3101_01\x01",      # 5
            "R3101_02\x01",      # 6
            "R3101_03\x01",      # 7
            "R3101_04\x01",      # 8
            "R3101_05\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_286A"),
        (1, "loc_287A"),
        (2, "loc_288A"),
        (3, "loc_289A"),
        (4, "loc_28AA"),
        (5, "loc_28BA"),
        (6, "loc_28CA"),
        (7, "loc_28DA"),
        (8, "loc_28EA"),
        (9, "loc_28FA"),
        (SWITCH_DEFAULT, "loc_290A"),
    )


    label("loc_286A")

    Battle(0x209, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_287A")

    Battle(0x20A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_288A")

    Battle(0x20B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_289A")

    Battle(0x20C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28AA")

    Battle(0x20D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28BA")

    Battle(0x349, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28CA")

    Battle(0x34A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28DA")

    Battle(0x34B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28EA")

    Battle(0x34C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_28FA")

    Battle(0x34D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2914")

    label("loc_290A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2914")

    Jump("Function_39_27B2")

    label("loc_2917")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_27B2 end

    def Function_40_2925(): pass

    label("Function_40_2925")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F9")

    AnonymousTalk(    #33
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3200_01\x01",      # 0
            "R3200_02\x01",      # 1
            "R3200_03\x01",      # 2
            "R3200_04\x01",      # 3
            "R3200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_299C"),
        (1, "loc_29AC"),
        (2, "loc_29BC"),
        (3, "loc_29CC"),
        (4, "loc_29DC"),
        (SWITCH_DEFAULT, "loc_29EC"),
    )


    label("loc_299C")

    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29F6")

    label("loc_29AC")

    Battle(0x21E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29F6")

    label("loc_29BC")

    Battle(0x21F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29F6")

    label("loc_29CC")

    Battle(0x220, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29F6")

    label("loc_29DC")

    Battle(0x221, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_29F6")

    label("loc_29EC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F6")

    Jump("Function_40_2925")

    label("loc_29F9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_2925 end

    def Function_41_2A07(): pass

    label("Function_41_2A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ADB")

    AnonymousTalk(    #34
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300_01\x01",      # 0
            "R3300_02\x01",      # 1
            "R3300_03\x01",      # 2
            "R3300_04\x01",      # 3
            "R3300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A7E"),
        (1, "loc_2A8E"),
        (2, "loc_2A9E"),
        (3, "loc_2AAE"),
        (4, "loc_2ABE"),
        (SWITCH_DEFAULT, "loc_2ACE"),
    )


    label("loc_2A7E")

    Battle(0x231, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AD8")

    label("loc_2A8E")

    Battle(0x232, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AD8")

    label("loc_2A9E")

    Battle(0x233, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AD8")

    label("loc_2AAE")

    Battle(0x234, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AD8")

    label("loc_2ABE")

    Battle(0x235, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AD8")

    label("loc_2ACE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AD8")

    Jump("Function_41_2A07")

    label("loc_2ADB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_2A07 end

    def Function_42_2AE9(): pass

    label("Function_42_2AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BE4")

    AnonymousTalk(    #35
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3107_01\x01",                # 0
            "C3107_02\x01",                # 1
            "C3107_10\x01",                # 2
            "C3107_11\x01",                # 3
            "C3107_12\x01",                # 4
            "C3107_14 (Agent C)\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B77"),
        (1, "loc_2B87"),
        (2, "loc_2B97"),
        (3, "loc_2BA7"),
        (4, "loc_2BB7"),
        (5, "loc_2BC7"),
        (SWITCH_DEFAULT, "loc_2BD7"),
    )


    label("loc_2B77")

    Battle(0x245, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2B87")

    Battle(0x246, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2B97")

    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2BA7")

    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2BB7")

    Battle(0x250, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2BC7")

    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE1")

    label("loc_2BD7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BE1")

    Jump("Function_42_2AE9")

    label("loc_2BE4")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_2AE9 end

    def Function_43_2BF2(): pass

    label("Function_43_2BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D0F")

    AnonymousTalk(    #36
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Erbe Scenic Route\x01",                  # 0
            "Sewers\x01",                             # 1
            "Sealed Area\x01",                        # 2
            "Royal Avenue\x01",                       # 3
            "Erbe Royal Villa (Night)\x01",           # 4
            "Erbe Royal Villa Room (Night)\x01",      # 5
            "Castle\x01",                             # 6
            "Castle Garden\x01",                      # 7
            "Cancel\x01",                             # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CCA"),
        (1, "loc_2CD1"),
        (2, "loc_2CD8"),
        (3, "loc_2CDF"),
        (4, "loc_2CE6"),
        (5, "loc_2CED"),
        (6, "loc_2CF4"),
        (7, "loc_2CFB"),
        (SWITCH_DEFAULT, "loc_2D02"),
    )


    label("loc_2CCA")

    Call(2, 44)
    Jump("loc_2D0C")

    label("loc_2CD1")

    Call(2, 45)
    Jump("loc_2D0C")

    label("loc_2CD8")

    Call(2, 46)
    Jump("loc_2D0C")

    label("loc_2CDF")

    Call(2, 47)
    Jump("loc_2D0C")

    label("loc_2CE6")

    Call(2, 48)
    Jump("loc_2D0C")

    label("loc_2CED")

    Call(2, 49)
    Jump("loc_2D0C")

    label("loc_2CF4")

    Call(2, 50)
    Jump("loc_2D0C")

    label("loc_2CFB")

    Call(2, 51)
    Jump("loc_2D0C")

    label("loc_2D02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D0C")

    Jump("Function_43_2BF2")

    label("loc_2D0F")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_43_2BF2 end

    def Function_44_2D1D(): pass

    label("Function_44_2D1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DF1")

    AnonymousTalk(    #37
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100_01\x01",      # 0
            "C4100_02\x01",      # 1
            "C4100_03\x01",      # 2
            "C4100_04\x01",      # 3
            "C4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D94"),
        (1, "loc_2DA4"),
        (2, "loc_2DB4"),
        (3, "loc_2DC4"),
        (4, "loc_2DD4"),
        (SWITCH_DEFAULT, "loc_2DE4"),
    )


    label("loc_2D94")

    Battle(0x259, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DEE")

    label("loc_2DA4")

    Battle(0x25A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DEE")

    label("loc_2DB4")

    Battle(0x25B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DEE")

    label("loc_2DC4")

    Battle(0x25C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DEE")

    label("loc_2DD4")

    Battle(0x25D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DEE")

    label("loc_2DE4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DEE")

    Jump("Function_44_2D1D")

    label("loc_2DF1")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_2D1D end

    def Function_45_2DFF(): pass

    label("Function_45_2DFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F47")

    AnonymousTalk(    #38
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200_01\x01",      # 0
            "C4200_02\x01",      # 1
            "C4200_03\x01",      # 2
            "C4200_04\x01",      # 3
            "C4200_05\x01",      # 4
            "C4200_06\x01",      # 5
            "C4200_07\x01",      # 6
            "C4200_08\x01",      # 7
            "C4200_09\x01",      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EAA"),
        (1, "loc_2EBA"),
        (2, "loc_2ECA"),
        (3, "loc_2EDA"),
        (4, "loc_2EEA"),
        (5, "loc_2EFA"),
        (6, "loc_2F0A"),
        (7, "loc_2F1A"),
        (8, "loc_2F2A"),
        (SWITCH_DEFAULT, "loc_2F3A"),
    )


    label("loc_2EAA")

    Battle(0x26D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2EBA")

    Battle(0x26E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2ECA")

    Battle(0x26F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2EDA")

    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2EEA")

    Battle(0x271, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2EFA")

    Battle(0x272, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2F0A")

    Battle(0x273, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2F1A")

    Battle(0x274, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2F2A")

    Battle(0x275, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F44")

    label("loc_2F3A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F44")

    Jump("Function_45_2DFF")

    label("loc_2F47")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_45_2DFF end

    def Function_46_2F55(): pass

    label("Function_46_2F55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30BA")

    AnonymousTalk(    #39
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4300_01\x01",      # 0
            "C4300_02\x01",      # 1
            "C4300_03\x01",      # 2
            "C4300_04\x01",      # 3
            "C4300_05\x01",      # 4
            "C4300_06\x01",      # 5
            "C4300_07\x01",      # 6
            "C4300_08\x01",      # 7
            "C4300_09\x01",      # 8
            "C4300_10\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_300D"),
        (1, "loc_301D"),
        (2, "loc_302D"),
        (3, "loc_303D"),
        (4, "loc_304D"),
        (5, "loc_305D"),
        (6, "loc_306D"),
        (7, "loc_307D"),
        (8, "loc_308D"),
        (9, "loc_309D"),
        (SWITCH_DEFAULT, "loc_30AD"),
    )


    label("loc_300D")

    Battle(0x281, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_301D")

    Battle(0x282, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_302D")

    Battle(0x283, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_303D")

    Battle(0x284, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_304D")

    Battle(0x285, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_305D")

    Battle(0x286, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_306D")

    Battle(0x287, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_307D")

    Battle(0x288, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_308D")

    Battle(0x289, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_309D")

    Battle(0x28A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30B7")

    label("loc_30AD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30B7")

    Jump("Function_46_2F55")

    label("loc_30BA")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_46_2F55 end

    def Function_47_30C8(): pass

    label("Function_47_30C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319C")

    AnonymousTalk(    #40
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_01\x01",      # 0
            "R4100_02\x01",      # 1
            "R4100_03\x01",      # 2
            "R4100_04\x01",      # 3
            "R4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_313F"),
        (1, "loc_314F"),
        (2, "loc_315F"),
        (3, "loc_316F"),
        (4, "loc_317F"),
        (SWITCH_DEFAULT, "loc_318F"),
    )


    label("loc_313F")

    Battle(0x295, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3199")

    label("loc_314F")

    Battle(0x296, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3199")

    label("loc_315F")

    Battle(0x297, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3199")

    label("loc_316F")

    Battle(0x298, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3199")

    label("loc_317F")

    Battle(0x299, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3199")

    label("loc_318F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3199")

    Jump("Function_47_30C8")

    label("loc_319C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_30C8 end

    def Function_48_31AA(): pass

    label("Function_48_31AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_327E")

    AnonymousTalk(    #41
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4301_01\x01",      # 0
            "T4301_02\x01",      # 1
            "T4301_03\x01",      # 2
            "T4301_04\x01",      # 3
            "T4301_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3221"),
        (1, "loc_3231"),
        (2, "loc_3241"),
        (3, "loc_3251"),
        (4, "loc_3261"),
        (SWITCH_DEFAULT, "loc_3271"),
    )


    label("loc_3221")

    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_327B")

    label("loc_3231")

    Battle(0x2BE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_327B")

    label("loc_3241")

    Battle(0x2BF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_327B")

    label("loc_3251")

    Battle(0x2C0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_327B")

    label("loc_3261")

    Battle(0x2C1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_327B")

    label("loc_3271")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_327B")

    Jump("Function_48_31AA")

    label("loc_327E")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_31AA end

    def Function_49_328C(): pass

    label("Function_49_328C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3360")

    AnonymousTalk(    #42
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4310_01\x01",      # 0
            "T4310_02\x01",      # 1
            "T4310_03\x01",      # 2
            "T4310_04\x01",      # 3
            "T4310_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3303"),
        (1, "loc_3313"),
        (2, "loc_3323"),
        (3, "loc_3333"),
        (4, "loc_3343"),
        (SWITCH_DEFAULT, "loc_3353"),
    )


    label("loc_3303")

    Battle(0x2D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_335D")

    label("loc_3313")

    Battle(0x2D2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_335D")

    label("loc_3323")

    Battle(0x2D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_335D")

    label("loc_3333")

    Battle(0x2D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_335D")

    label("loc_3343")

    Battle(0x2D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_335D")

    label("loc_3353")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_335D")

    Jump("Function_49_328C")

    label("loc_3360")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_49_328C end

    def Function_50_336E(): pass

    label("Function_50_336E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3442")

    AnonymousTalk(    #43
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4210_01\x01",      # 0
            "T4210_02\x01",      # 1
            "T4210_03\x01",      # 2
            "T4210_04\x01",      # 3
            "T4210_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33E5"),
        (1, "loc_33F5"),
        (2, "loc_3405"),
        (3, "loc_3415"),
        (4, "loc_3425"),
        (SWITCH_DEFAULT, "loc_3435"),
    )


    label("loc_33E5")

    Battle(0x2E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_343F")

    label("loc_33F5")

    Battle(0x2E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_343F")

    label("loc_3405")

    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_343F")

    label("loc_3415")

    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_343F")

    label("loc_3425")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_343F")

    label("loc_3435")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_343F")

    Jump("Function_50_336E")

    label("loc_3442")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_336E end

    def Function_51_3450(): pass

    label("Function_51_3450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3524")

    AnonymousTalk(    #44
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4201_01\x01",      # 0
            "T4201_02\x01",      # 1
            "T4201_03\x01",      # 2
            "T4201_04\x01",      # 3
            "T4201_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34C7"),
        (1, "loc_34D7"),
        (2, "loc_34E7"),
        (3, "loc_34F7"),
        (4, "loc_3507"),
        (SWITCH_DEFAULT, "loc_3517"),
    )


    label("loc_34C7")

    Battle(0x2F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3521")

    label("loc_34D7")

    Battle(0x2FA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3521")

    label("loc_34E7")

    Battle(0x2FB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3521")

    label("loc_34F7")

    Battle(0x2FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3521")

    label("loc_3507")

    Battle(0x2FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3521")

    label("loc_3517")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3521")

    Jump("Function_51_3450")

    label("loc_3524")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_51_3450 end

    def Function_52_3532(): pass

    label("Function_52_3532")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3606")

    AnonymousTalk(    #45
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_21\x01",      # 0
            "R4100_22\x01",      # 1
            "R4100_23\x01",      # 2
            "R4100_24\x01",      # 3
            "R4100_25\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35A9"),
        (1, "loc_35B9"),
        (2, "loc_35C9"),
        (3, "loc_35D9"),
        (4, "loc_35E9"),
        (SWITCH_DEFAULT, "loc_35F9"),
    )


    label("loc_35A9")

    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3603")

    label("loc_35B9")

    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3603")

    label("loc_35C9")

    Battle(0x2AB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3603")

    label("loc_35D9")

    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3603")

    label("loc_35E9")

    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3603")

    label("loc_35F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3603")

    Jump("Function_52_3532")

    label("loc_3606")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_52_3532 end

    def Function_53_3614(): pass

    label("Function_53_3614")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_361E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3836")

    AnonymousTalk(    #46
        "\x06Select an enemy.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "Bleublanc\x01",                # 0
            "Walter\x01",                   # 1
            "Lucciola\x01",                 # 2
            "Renne\x01",                    # 3
            "Loewe\x01",                    # 4
            "Weissmann\x01",                # 5
            "Jaeger Kurt\x01",              # 6
            "Jaeger Carna\x01",             # 7
            "Jaeger Grant\x01",             # 8
            "Brainwashed Grant\x01",        # 9
            "Brainwashed Carna\x01",        # 10
            "Brainwashed Anelace\x01",      # 11
            "Jaeger Gilbert\x01",           # 12
            "Mueller\x01",                  # 13
            "Cid\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3739"),
        (1, "loc_3749"),
        (2, "loc_3759"),
        (3, "loc_3769"),
        (4, "loc_3779"),
        (5, "loc_3789"),
        (6, "loc_3799"),
        (7, "loc_37A9"),
        (8, "loc_37B9"),
        (9, "loc_37C9"),
        (10, "loc_37D9"),
        (11, "loc_37E9"),
        (12, "loc_37F9"),
        (13, "loc_3809"),
        (14, "loc_3819"),
        (SWITCH_DEFAULT, "loc_3829"),
    )


    label("loc_3739")

    Battle(0x802, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3749")

    Battle(0x803, 0x30000D, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3759")

    Battle(0x804, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3769")

    Battle(0x805, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3779")

    Battle(0x806, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3789")

    Battle(0x807, 0x30000C, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3799")

    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37A9")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37B9")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37C9")

    Battle(0x41E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37D9")

    Battle(0x41F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37E9")

    Battle(0x420, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_37F9")

    Battle(0x42A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3809")

    Battle(0xA8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3819")

    Battle(0xC82, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3833")

    label("loc_3829")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3833")

    Jump("loc_361E")

    label("loc_3836")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_53_3614 end

    def Function_54_3844(): pass

    label("Function_54_3844")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_384E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A37")

    AnonymousTalk(    #47
        "\x06Select an enemy.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "FC Last Boss\x01",                         # 0
            "Storm Bringer\x01",                        # 1
            "Tromelais Dragon\x01",                     # 2
            "Ragnard\x01",                              # 3
            "Orgueille\x01",                            # 4
            "Pater-Mater\x01",                          # 5
            "Pater-Mater (w/Renne)\x01",                # 6
            "Angel Weissmann Form 1\x01",               # 7
            "Angel Weissmann Form 2\x01",               # 8
            "Angel Weissmann Event\x01",                # 9
            "Angel Weissmann Form 2 (Effect)\x01",      # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3974"),
        (1, "loc_3984"),
        (2, "loc_3994"),
        (3, "loc_39A4"),
        (4, "loc_39B4"),
        (5, "loc_39C4"),
        (6, "loc_39D4"),
        (7, "loc_39E4"),
        (8, "loc_39F4"),
        (9, "loc_3A04"),
        (10, "loc_3A1A"),
        (SWITCH_DEFAULT, "loc_3A2A"),
    )


    label("loc_3974")

    Battle(0x7D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_3984")

    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_3994")

    Battle(0x450, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39A4")

    Battle(0x44F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39B4")

    Battle(0x44E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39C4")

    Battle(0x463, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39D4")

    Battle(0x453, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39E4")

    Battle(0x451, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_39F4")

    Battle(0x452, 0x300017, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_3A04")

    OP_A2(0x2298)
    Battle(0x465, 0x300014, 0x0, 0x0, 0xFF)
    OP_A3(0x2298)
    Jump("loc_3A34")

    label("loc_3A1A")

    Battle(0x7D8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3A34")

    label("loc_3A2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A34")

    Jump("loc_384E")

    label("loc_3A37")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_54_3844 end

    def Function_55_3A45(): pass

    label("Function_55_3A45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AFB")

    AnonymousTalk(    #48
        "\x06Select an enemy.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "カニおやびん\x01",          # 0
            "ペングおやびん\x01",        # 1
            "ヒツジンおやびん\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3ABE"),
        (1, "loc_3ACE"),
        (2, "loc_3ADE"),
        (SWITCH_DEFAULT, "loc_3AEE"),
    )


    label("loc_3ABE")

    Battle(0x59, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AF8")

    label("loc_3ACE")

    Battle(0x1EA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AF8")

    label("loc_3ADE")

    Battle(0x1EB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AF8")

    label("loc_3AEE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AF8")

    Jump("loc_3A4F")

    label("loc_3AFB")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_3A45 end

    def Function_56_3B09(): pass

    label("Function_56_3B09")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C29")

    AnonymousTalk(    #49
        "\x06Select a battle.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "Chapter 8, Lucciola and Renne\x01",      # 0
            "Chapter 8, Bleublanc\x01",               # 1
            "Chapter 9, Joshua vs Estelle\x01",       # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BA5"),
        (1, "loc_3BF3"),
        (2, "loc_3C0C"),
        (SWITCH_DEFAULT, "loc_3C1C"),
    )


    label("loc_3BA5")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2710, 0x30000F, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2711, 0x300010, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2712, 0x300011, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C26")

    label("loc_3BF3")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2713, 0x300012, 0x0, 0x0, 0xFF)
    Jump("loc_3C26")

    label("loc_3C0C")

    Battle(0x2714, 0x300013, 0x0, 0x0, 0xFF)
    Jump("loc_3C26")

    label("loc_3C1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C26")

    Jump("loc_3B13")

    label("loc_3C29")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_56_3B09 end

    def Function_57_3C37(): pass

    label("Function_57_3C37")

    Return()

    # Function_57_3C37 end

    def Function_58_3C38(): pass

    label("Function_58_3C38")

    OP_31(0x0, 0x0, 0x55)
    OP_31(0x1, 0x0, 0x55)
    OP_31(0x2, 0x0, 0x55)
    OP_31(0x3, 0x0, 0x55)
    OP_31(0x6, 0x0, 0x55)
    OP_31(0x4, 0x0, 0x55)
    OP_31(0x5, 0x0, 0x55)
    OP_31(0x7, 0x0, 0x55)
    OP_31(0x8, 0x0, 0x55)
    OP_31(0x9, 0x0, 0x55)
    OP_31(0xA, 0x0, 0x55)
    OP_31(0xB, 0x0, 0x55)
    OP_31(0xF, 0x0, 0x55)
    OP_31(0xC, 0x0, 0x55)
    OP_31(0xD, 0x0, 0x55)
    OP_31(0xE, 0x0, 0x55)
    OP_31(0x0, 0x5, 0x64)
    OP_31(0x1, 0x5, 0x64)
    OP_31(0x2, 0x5, 0x64)
    OP_31(0x3, 0x5, 0x64)
    OP_31(0x6, 0x5, 0x64)
    OP_31(0x4, 0x5, 0x64)
    OP_31(0x5, 0x5, 0x64)
    OP_31(0x7, 0x5, 0x64)
    OP_31(0x8, 0x5, 0x64)
    OP_31(0x9, 0x5, 0x64)
    OP_31(0xA, 0x5, 0x64)
    OP_31(0xB, 0x5, 0x64)
    OP_31(0xF, 0x5, 0x64)
    OP_31(0xC, 0x5, 0x64)
    OP_31(0xD, 0x5, 0x64)
    OP_31(0xE, 0x5, 0x64)
    OP_37(0x0, 0xFF)
    OP_37(0x1, 0xFF)
    OP_37(0x2, 0xFF)
    OP_37(0x3, 0xFF)
    OP_37(0x6, 0xFF)
    OP_37(0x4, 0xFF)
    OP_37(0x5, 0xFF)
    OP_37(0x7, 0xFF)
    OP_37(0x8, 0xFF)
    OP_37(0x9, 0xFF)
    OP_37(0xA, 0xFF)
    OP_37(0xB, 0xFF)
    OP_37(0xF, 0xFF)
    OP_37(0xC, 0xFF)
    OP_37(0xD, 0xFF)
    OP_37(0xE, 0xFF)
    OP_3E(0x202, 99)
    OP_3E(0x1F7, 99)
    OP_3E(0x1FB, 99)
    OP_3E(0x1FC, 99)
    OP_3E(0x1FD, 10)
    OP_3E(0x204, 8)
    OP_3E(0x1FF, 99)
    OP_3E(0x1FF, 99)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x41)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x5F)
    OP_34(0x1, 0x60)
    OP_34(0x1, 0x69)
    OP_34(0x1, 0x6A)
    OP_34(0x0, 0x1E)
    OP_34(0x0, 0x1F)
    OP_34(0x0, 0x20)
    OP_34(0x0, 0x23)
    OP_34(0x0, 0x25)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x70)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0x77)
    OP_34(0x0, 0x78)
    OP_34(0x2, 0x32)
    OP_34(0x2, 0x33)
    OP_34(0x2, 0x34)
    OP_34(0x2, 0x36)
    OP_34(0x2, 0x37)
    OP_34(0x3, 0x64)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x4B)
    OP_34(0x3, 0x4C)
    OP_34(0x4, 0x6E)
    OP_34(0x4, 0x6F)
    OP_34(0x4, 0x70)
    OP_34(0x4, 0x72)
    OP_34(0x4, 0x73)
    OP_34(0x4, 0x76)
    OP_34(0x4, 0x77)
    OP_34(0x4, 0x78)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0x1F)
    OP_34(0x5, 0x20)
    OP_34(0x6, 0x56)
    OP_34(0x6, 0x57)
    OP_34(0x6, 0x58)
    OP_34(0x6, 0x6E)
    OP_34(0x6, 0x6F)
    OP_34(0x6, 0x76)
    OP_34(0x7, 0xB)
    OP_34(0x7, 0xD)
    OP_34(0x7, 0x10)
    OP_34(0x7, 0x4B)
    OP_34(0x7, 0x4C)
    OP_35(0x0, 0x0)
    OP_35(0x1, 0x0)
    OP_35(0x2, 0x0)
    OP_35(0x3, 0x0)
    OP_35(0x4, 0x0)
    OP_35(0x5, 0x0)
    OP_35(0x6, 0x0)
    OP_35(0x7, 0x0)
    OP_35(0x8, 0x0)
    OP_35(0xA, 0x0)
    OP_35(0xB, 0x0)
    OP_35(0xE, 0x0)
    OP_35(0xF, 0x0)
    OP_35(0xD, 0x0)
    OP_35(0x9, 0x0)
    OP_35(0xC, 0x0)
    OP_41(0x0, 0x15, 0xFF)
    OP_41(0x0, 0x108, 0xFF)
    OP_41(0x0, 0x109, 0xFF)
    OP_41(0x1, 0x2B, 0xFF)
    OP_41(0x1, 0x108, 0xFF)
    OP_41(0x1, 0x129, 0xFF)
    OP_41(0x2, 0x4C, 0xFF)
    OP_41(0x2, 0x108, 0xFF)
    OP_41(0x2, 0x129, 0xFF)
    OP_41(0x3, 0x6B, 0xFF)
    OP_41(0x3, 0x108, 0xFF)
    OP_41(0x3, 0x129, 0xFF)
    OP_41(0x4, 0x88, 0xFF)
    OP_41(0x4, 0x108, 0xFF)
    OP_41(0x4, 0x129, 0xFF)
    OP_41(0x5, 0xA6, 0xFF)
    OP_41(0x5, 0x108, 0xFF)
    OP_41(0x5, 0x129, 0xFF)
    OP_41(0x6, 0xC3, 0xFF)
    OP_41(0x6, 0x108, 0xFF)
    OP_41(0x6, 0x129, 0xFF)
    OP_41(0x7, 0xE0, 0xFF)
    OP_41(0x7, 0x108, 0xFF)
    OP_41(0x7, 0x129, 0xFF)
    Return()

    # Function_58_3C38 end

    def Function_59_3EB5(): pass

    label("Function_59_3EB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_414B")

    AnonymousTalk(    #50
        "\x06Select a minigame.\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "00 Roulette\x01",       # 0
            "01 Slots\x01",          # 1
            "02 Blackjack\x01",      # 2
            "03 Fishing\x01",        # 3
            "04 Poker\x01",          # 4
            "05 Shooting\x01",       # 5
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F4C"),
        (1, "loc_3F85"),
        (2, "loc_3FBE"),
        (3, "loc_3FF7"),
        (4, "loc_40CC"),
        (5, "loc_4105"),
        (SWITCH_DEFAULT, "loc_413E"),
    )


    label("loc_3F4C")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_413E")

    label("loc_3F85")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_413E")

    label("loc_3FBE")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_413E")

    label("loc_3FF7")

    OP_3E(0x24E, 10)
    OP_3E(0x24F, 10)
    OP_3E(0x250, 10)
    OP_3E(0x251, 10)
    OP_3E(0x252, 10)
    OP_3E(0x253, 10)
    OP_3E(0x254, 10)
    OP_3E(0x3D4, 10)
    OP_3E(0x3D5, 10)
    OP_3E(0x3D6, 10)
    OP_3E(0x3D7, 10)
    OP_3E(0x3D8, 10)
    OP_3E(0x3D9, 10)
    OP_3E(0x3DA, 10)
    OP_3E(0x3DB, 10)
    OP_3E(0x3DC, 10)
    OP_3E(0x3DD, 10)
    OP_3E(0x3DE, 10)
    OP_3E(0x3DF, 10)
    OP_3E(0x3E0, 10)
    OP_3E(0x3E1, 10)
    OP_3E(0x3E2, 10)
    OP_3E(0x3E3, 10)

    AnonymousTalk(    #51
        (
            "ブライト家へ移動しますので、\x01",
            "裏手の池のルックポイントを探して\x01",
            "釣りをしてください。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_413E")

    label("loc_40CC")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_413E")

    label("loc_4105")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_413E")

    label("loc_413E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("Function_59_3EB5")

    label("loc_414B")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_59_3EB5 end

    SaveToFile()

Try(main)
