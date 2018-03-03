from ED63RDScenarioHelper import *

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
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_3EF",          # 02, 2
        "Function_3_4E4",          # 03, 3
        "Function_4_569",          # 04, 4
        "Function_5_5E1",          # 05, 5
        "Function_6_70E",          # 06, 6
        "Function_7_7BD",          # 07, 7
        "Function_8_96F",          # 08, 8
        "Function_9_9EB",          # 09, 9
        "Function_10_E89",         # 0A, 10
        "Function_11_13A2",        # 0B, 11
        "Function_12_1509",        # 0C, 12
        "Function_13_162B",        # 0D, 13
        "Function_14_186E",        # 0E, 14
        "Function_15_186F",        # 0F, 15
        "Function_16_1870",        # 10, 16
        "Function_17_1871",        # 11, 17
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test\x01",                      # 0
            "Flying Feline\x01",             # 1
            "Helmet Crab\x01",               # 2
            "Flying Feline 3\x01",           # 3
            "Human Boss\x01",                # 4
            "Big Boss\x01",                  # 5
            "Other Boss\x01",                # 6
            "Choose Monster\x01",            # 7
            "Fight Chosen Monster\x01",      # 8
            "Demonstration 1\x01",           # 9
            "Demonstration 2\x01",           # 10
            "Demonstration 3\x01",           # 11
            "Auto Battle\x01",               # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AE"),
        (1, "loc_1BE"),
        (2, "loc_1CE"),
        (3, "loc_1DE"),
        (4, "loc_1EE"),
        (5, "loc_1F5"),
        (6, "loc_1FC"),
        (7, "loc_203"),
        (8, "loc_23A"),
        (9, "loc_24A"),
        (10, "loc_25A"),
        (11, "loc_26A"),
        (12, "loc_27A"),
        (SWITCH_DEFAULT, "loc_28A"),
    )


    label("loc_1AE")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_1BE")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_1CE")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_1DE")

    Battle(0x7D7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_1EE")

    Call(2, 12)
    Jump("loc_28D")

    label("loc_1F5")

    Call(2, 13)
    Jump("loc_28D")

    label("loc_1FC")

    Call(2, 14)
    Jump("loc_28D")

    label("loc_203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x21, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_237")
    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)

    label("loc_237")

    Jump("loc_28D")

    label("loc_23A")

    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_24A")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_25A")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_26A")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_27A")

    Battle(0x2710, 0x30000B, 0x0, 0x0, 0xFF)
    Jump("loc_28D")

    label("loc_28A")

    Jump("loc_28D")

    label("loc_28D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2CF"),
    )


    label("loc_2A4")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_2CF")

    label("loc_2CF")

    Jump("Function_0_AA")

    label("loc_2D2")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_2E0(): pass

    label("Function_1_2E0")


    AnonymousTalk(    #0
        "\x06Select a section.\x02",
    )


    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test\x01",          # 0
            "Rolent\x01",        # 1
            "Bose\x01",          # 2
            "Ruan\x01",          # 3
            "Zeiss\x01",         # 4
            "Grancel\x01",       # 5
            "Others\x01",        # 6
            "Gaiden 1\x01",      # 7
            "Gaiden 2\x01",      # 8
            "Gaiden 3\x01",      # 9
            "Cancel\x01",        # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_393"),
        (2, "loc_39A"),
        (3, "loc_3A1"),
        (4, "loc_3A8"),
        (5, "loc_3AF"),
        (6, "loc_3B6"),
        (7, "loc_3BD"),
        (8, "loc_3C4"),
        (9, "loc_3CB"),
        (SWITCH_DEFAULT, "loc_3D2"),
    )


    label("loc_38C")

    Call(2, 2)
    Jump("loc_3DC")

    label("loc_393")

    Call(2, 3)
    Jump("loc_3DC")

    label("loc_39A")

    Call(2, 4)
    Jump("loc_3DC")

    label("loc_3A1")

    Call(2, 5)
    Jump("loc_3DC")

    label("loc_3A8")

    Call(2, 6)
    Jump("loc_3DC")

    label("loc_3AF")

    Call(2, 7)
    Jump("loc_3DC")

    label("loc_3B6")

    Call(2, 8)
    Jump("loc_3DC")

    label("loc_3BD")

    Call(2, 9)
    Jump("loc_3DC")

    label("loc_3C4")

    Call(2, 10)
    Jump("loc_3DC")

    label("loc_3CB")

    Call(2, 11)
    Jump("loc_3DC")

    label("loc_3D2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DC")

    Jump("loc_2F5")

    label("loc_3DF")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2E0 end

    def Function_2_3EF(): pass

    label("Function_2_3EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D4")

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
        (0, "loc_477"),
        (1, "loc_487"),
        (2, "loc_497"),
        (3, "loc_4A7"),
        (4, "loc_4B7"),
        (SWITCH_DEFAULT, "loc_4C7"),
    )


    label("loc_477")

    Battle(0x82B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4D1")

    label("loc_487")

    Battle(0x82C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4D1")

    label("loc_497")

    Battle(0x82D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4D1")

    label("loc_4A7")

    Battle(0x82E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4D1")

    label("loc_4B7")

    Battle(0x82F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4D1")

    label("loc_4C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D1")

    Jump("Function_2_3EF")

    label("loc_4D4")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_3EF end

    def Function_3_4E4(): pass

    label("Function_3_4E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55B")

    AnonymousTalk(    #1
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC0300 Mistwald\x01",      # 0
            "Cancel\x01",               # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_532"),
        (SWITCH_DEFAULT, "loc_54E"),
    )


    label("loc_532")

    OP_C4(0x0, 0x4)
    Battle(0x834, 0x0, 0x0, 0x0, 0xFF)
    OP_C4(0x1, 0x4)
    Jump("loc_558")

    label("loc_54E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_558")

    Jump("Function_3_4E4")

    label("loc_55B")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_4E4 end

    def Function_4_569(): pass

    label("Function_4_569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3")

    AnonymousTalk(    #2
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC1300 Airship\x01",      # 0
            "Cancel\x01",              # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B6"),
        (SWITCH_DEFAULT, "loc_5C6"),
    )


    label("loc_5B6")

    Battle(0x898, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5D0")

    label("loc_5C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D0")

    Jump("Function_4_569")

    label("loc_5D3")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_569 end

    def Function_5_5E1(): pass

    label("Function_5_5E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_700")

    AnonymousTalk(    #3
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC2401 Old Schoolhouse Basement Boss\x01",      # 0
            "BT2500 Schoolyard\x01",                         # 1
            "BT2510 Schoolhouse Hall\x01",                   # 2
            "BT2511 Boys' Dorm\x01",                         # 3
            "BT2512 Girls' Dorm\x01",                        # 4
            "Cancel\x01",                                    # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A3"),
        (1, "loc_6B3"),
        (2, "loc_6C3"),
        (3, "loc_6D3"),
        (4, "loc_6E3"),
        (SWITCH_DEFAULT, "loc_6F3"),
    )


    label("loc_6A3")

    Battle(0x8FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6FD")

    label("loc_6B3")

    Battle(0x8FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6FD")

    label("loc_6C3")

    Battle(0x8FE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6FD")

    label("loc_6D3")

    Battle(0x8FF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6FD")

    label("loc_6E3")

    Battle(0x900, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6FD")

    label("loc_6F3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FD")

    Jump("Function_5_5E1")

    label("loc_700")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_5E1 end

    def Function_6_70E(): pass

    label("Function_6_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AF")

    AnonymousTalk(    #4
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BR3400 Kaldia Tunnel\x01",              # 0
            "BC3300 Kaldia Limestone Cave\x01",      # 1
            "Cancel\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_782"),
        (1, "loc_792"),
        (SWITCH_DEFAULT, "loc_7A2"),
    )


    label("loc_782")

    Battle(0x960, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7AC")

    label("loc_792")

    Battle(0x961, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7AC")

    label("loc_7A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AC")

    Jump("Function_6_70E")

    label("loc_7AF")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_70E end

    def Function_7_7BD(): pass

    label("Function_7_7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_961")

    AnonymousTalk(    #5
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BT4100 Town (Evening)\x01",             # 0
            "BT4404 Wharf (Evening)\x01",            # 1
            "BT4105 Grand Arena (Evening)\x01",      # 2
            "BT4210 Castle Halls\x01",               # 3
            "BC4100 Erbe Scenic Route\x01",          # 4
            "BC4303 Sealed Area\x01",                # 5
            "BT4138 Erebonian Embassy\x01",          # 6
            "BT4139 Calvardian Embassy\x01",         # 7
            "Cancel\x01",                            # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8D4"),
        (1, "loc_8E4"),
        (2, "loc_8F4"),
        (3, "loc_904"),
        (4, "loc_914"),
        (5, "loc_924"),
        (6, "loc_934"),
        (7, "loc_944"),
        (SWITCH_DEFAULT, "loc_954"),
    )


    label("loc_8D4")

    Battle(0x9C4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_8E4")

    Battle(0x9C5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_8F4")

    Battle(0x9C6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_904")

    Battle(0x9C7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_914")

    Battle(0x9C8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_924")

    Battle(0x9C9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_934")

    Battle(0x9CA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_944")

    Battle(0x9CB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_95E")

    label("loc_954")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95E")

    Jump("Function_7_7BD")

    label("loc_961")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_7BD end

    def Function_8_96F(): pass

    label("Function_8_96F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DD")

    AnonymousTalk(    #6
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC5303 Axis Pillar\x01",      # 0
            "Cancel\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9C0"),
        (SWITCH_DEFAULT, "loc_9D0"),
    )


    label("loc_9C0")

    Battle(0xA28, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9DA")

    label("loc_9D0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DA")

    Jump("Function_8_96F")

    label("loc_9DD")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_96F end

    def Function_9_9EB(): pass

    label("Function_9_9EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7B")

    AnonymousTalk(    #7
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BE0310 1st Plane Arseille\x01",                       # 0
            "BM7000 1st Plane Jade Corridor\x01",                  # 1
            "BM7001 1st Plane Boss\x01",                           # 2
            "BU4138 2nd Plane Erebonian Embassy\x01",              # 3
            "BU4403 2nd Plane Wharf Warehouse (Evening)\x01",      # 4
            "BU4166 2nd Plane Grand Arena (Night)\x01",            # 5
            "BU4250 2nd Plane Castle Hall (Night)\x01",            # 6
            "BU4204 2nd Plane Castle Garden (Night)\x01",          # 7
            "BM7100 3rd Plane Gold Road\x01",                      # 8
            "BM7101 3rd Plane Gold Road Boss\x01",                 # 9
            "BM7102 3rd Plane Silver Road\x01",                    # 10
            "BM7103 3rd Plane Silver Road Boss\x01",               # 11
            "BM5500 4th Plane Balstar Channel\x01",                # 12
            "BM5501 4th Plane Balstar Channel Boss\x01",           # 13
            "BM5502 4th Plane Saint-Croix Forest\x01",             # 14
            "BM5503 4th Plane Saint-Croix Forest Boss\x01",        # 15
            "BU5102 4th Plane Le-Locle Lodge (Astarte)\x01",       # 16
            "BM7200 5th Plane Labyrinth of Light\x01",             # 17
            "BM7201 5th Plane Labyrinth of Shadows\x01",           # 18
            "BM7202 5th Plane Labyrinth of Light Boss\x01",        # 19
            "Cancel\x01",                                          # 20
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D2E"),
        (1, "loc_D3E"),
        (2, "loc_D4E"),
        (3, "loc_D5E"),
        (4, "loc_D6E"),
        (5, "loc_D7E"),
        (6, "loc_D8E"),
        (7, "loc_D9E"),
        (8, "loc_DAE"),
        (9, "loc_DBE"),
        (10, "loc_DCE"),
        (11, "loc_DDE"),
        (12, "loc_DEE"),
        (13, "loc_DFE"),
        (14, "loc_E0E"),
        (15, "loc_E1E"),
        (16, "loc_E2E"),
        (17, "loc_E3E"),
        (18, "loc_E4E"),
        (19, "loc_E5E"),
        (SWITCH_DEFAULT, "loc_E6E"),
    )


    label("loc_D2E")

    Battle(0xA8C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D3E")

    Battle(0xA8D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D4E")

    Battle(0xA8E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D5E")

    Battle(0xA8F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D6E")

    Battle(0xA90, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D7E")

    Battle(0xA91, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D8E")

    Battle(0xA92, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_D9E")

    Battle(0xA93, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DAE")

    Battle(0xA94, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DBE")

    Battle(0xA95, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DCE")

    Battle(0xA96, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DDE")

    Battle(0xA97, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DEE")

    Battle(0xA98, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_DFE")

    Battle(0xA99, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E0E")

    Battle(0xA9A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E1E")

    Battle(0xA9B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E2E")

    Battle(0xA9C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E3E")

    Battle(0xA9C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E4E")

    Battle(0xA9D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E5E")

    Battle(0xA9E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E78")

    label("loc_E6E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E78")

    Jump("Function_9_9EB")

    label("loc_E7B")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_9EB end

    def Function_10_E89(): pass

    label("Function_10_E89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1394")

    AnonymousTalk(    #8
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BM4120 6th Plane Erbe Scenic Route\x01",                 # 0
            "BM3200 6th Plane Leiston Fortress\x01",                  # 1
            "BM3201 6th Plane Leiston Fortress Barracks\x01",         # 2
            "BM3202 6th Plane Leiston Fortress Boss 1\x01",           # 3
            "BM3203 6th Plane Leiston Fortress Boss 2\x01",           # 4
            "BM3204 6th Plane Leiston Fortress Boss 3\x01",           # 5
            "BM5400 6th Plane Glorious Hall\x01",                     # 6
            "BM5401 6th Plane Glorious Sanctuary\x01",                # 7
            "BM5406 6th Plane Glorious Hangar\x01",                   # 8
            "BM5408 6th Plane Glorious Deck\x01",                     # 9
            "BM5415 6th Plane Dimensional Road\x01",                  # 10
            "BU2501 6th Plane Old Schoolhouse Path\x01",              # 11
            "BM5600 6th Plane Laboratory Roof\x01",                   # 12
            "BM7300 7th Plane Purgatory\x01",                         # 13
            "BM7301 7th Plane Purgatory Boss\x01",                    # 14
            "BM7302 7th Plane Abyss\x01",                             # 15
            "BM7303 7th Plane Abyss (Midboss)\x01",                   # 16
            "BM7304 7th Plane Abyss (Boss)\x01",                      # 17
            "BM7400 8th Plane Phantasmagoria\x01",                    # 18
            "BM7401 8th Plane Phantasmagoria (Midboss)\x01",          # 19
            "BM7402 8th Plane Phantasmagoria (Regnamodoki)\x01",      # 20
            "BM7403 8th Plane Phantasmagoria (Last Boss)\x01",        # 21
            "Cancel\x01",                                             # 22
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1227"),
        (1, "loc_1237"),
        (2, "loc_1247"),
        (3, "loc_1257"),
        (4, "loc_1267"),
        (5, "loc_1277"),
        (6, "loc_1287"),
        (7, "loc_1297"),
        (8, "loc_12A7"),
        (9, "loc_12B7"),
        (10, "loc_12C7"),
        (11, "loc_12D7"),
        (12, "loc_12E7"),
        (13, "loc_12F7"),
        (14, "loc_1307"),
        (15, "loc_1317"),
        (16, "loc_1327"),
        (17, "loc_1337"),
        (18, "loc_1347"),
        (19, "loc_1357"),
        (20, "loc_1367"),
        (21, "loc_1377"),
        (SWITCH_DEFAULT, "loc_1387"),
    )


    label("loc_1227")

    Battle(0xABE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1237")

    Battle(0xABF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1247")

    Battle(0xAC0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1257")

    Battle(0xAC1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1267")

    Battle(0xAC2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1277")

    Battle(0xAC3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1287")

    Battle(0xAC4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1297")

    Battle(0xAC5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12A7")

    Battle(0xAC6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12B7")

    Battle(0xAC7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12C7")

    Battle(0xAC8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12D7")

    Battle(0xAC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12E7")

    Battle(0xACA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_12F7")

    Battle(0xAD2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1307")

    Battle(0xAD3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1317")

    Battle(0xAD4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1327")

    Battle(0xAD5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1337")

    Battle(0xAD6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1347")

    Battle(0xAD7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1357")

    Battle(0xAD8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1367")

    Battle(0xAD9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1377")

    Battle(0xADA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1391")

    label("loc_1387")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1391")

    Jump("Function_10_E89")

    label("loc_1394")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_E89 end

    def Function_11_13A2(): pass

    label("Function_11_13A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FB")

    AnonymousTalk(    #9
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BP9000 Moon Door\x01",            # 0
            "BP9001 Star Door\x01",            # 1
            "BP9002 Sun Door\x01",             # 2
            "BE1110 Lusitania\x01",            # 3
            "BE1111 Lusitania Room\x01",       # 4
            "BE1100 Lusitania Deck\x01",       # 5
            "BE0820 Field (Sky Map)\x01",      # 6
            "Cancel\x01",                      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_147E"),
        (1, "loc_148E"),
        (2, "loc_149E"),
        (3, "loc_14AE"),
        (4, "loc_14BE"),
        (5, "loc_14CE"),
        (6, "loc_14DE"),
        (SWITCH_DEFAULT, "loc_14EE"),
    )


    label("loc_147E")

    Battle(0xADC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_148E")

    Battle(0xADD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_149E")

    Battle(0xADE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_14AE")

    Battle(0xADF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_14BE")

    Battle(0xAE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_14CE")

    Battle(0xAE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_14DE")

    Battle(0xAE2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_14F8")

    label("loc_14EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14F8")

    Jump("Function_11_13A2")

    label("loc_14FB")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_13A2 end

    def Function_12_1509(): pass

    label("Function_12_1509")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1513")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161D")

    AnonymousTalk(    #10
        "\x06Select an enemy.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "Bleublanc\x01",      # 0
            "Walter\x01",         # 1
            "Lucciola\x01",       # 2
            "Weissmann\x01",      # 3
            "Cassius\x01",        # 4
            "Kilika\x01",         # 5
            "Phillip\x01",        # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15A0"),
        (1, "loc_15B0"),
        (2, "loc_15C0"),
        (3, "loc_15D0"),
        (4, "loc_15E0"),
        (5, "loc_15F0"),
        (6, "loc_1600"),
        (SWITCH_DEFAULT, "loc_1610"),
    )


    label("loc_15A0")

    Battle(0x802, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_15B0")

    Battle(0x803, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_15C0")

    Battle(0x804, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_15D0")

    Battle(0x807, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_15E0")

    Battle(0x808, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_15F0")

    Battle(0x809, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_1600")

    Battle(0x80A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_161A")

    label("loc_1610")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_161A")

    Jump("loc_1513")

    label("loc_161D")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1509 end

    def Function_13_162B(): pass

    label("Function_13_162B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1635")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1860")

    AnonymousTalk(    #11
        "\x06Select an enemy.\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "Tromelais II Gespenst\x01",       # 0
            "Storm Bringer\x01",               # 1
            "Tromelais Dragon\x01",            # 2
            "Ragnard\x01",                     # 3
            "Orgueille\x01",                   # 4
            "Lostrum\x01",                     # 5
            "Astarte\x01",                     # 6
            "Last Boss\x01",                   # 7
            "Last Boss (Skip Intro)\x01",      # 8
            "Last Boss Party Setup\x01",       # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1721"),
        (1, "loc_1731"),
        (2, "loc_1741"),
        (3, "loc_1751"),
        (4, "loc_1761"),
        (5, "loc_1771"),
        (6, "loc_1781"),
        (7, "loc_1791"),
        (8, "loc_17A1"),
        (9, "loc_17B6"),
        (SWITCH_DEFAULT, "loc_1853"),
    )


    label("loc_1721")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1731")

    Battle(0xE11, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1741")

    Battle(0xE15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1751")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1761")

    Battle(0xE13, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1771")

    Battle(0xF9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1781")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_1791")

    Battle(0xE16, 0x300001, 0x0, 0x0, 0xFF)
    Jump("loc_185D")

    label("loc_17A1")

    Battle(0xE16, 0x0, 0x0, 0x0, 0xFF)
    Sleep(1000)
    Jump("loc_185D")

    label("loc_17B6")

    OP_DC(0x1, 0x0, 0x8)
    OP_DC(0x1, 0x0, 0xE)
    OP_DC(0x1, 0x0, 0x5)
    OP_DC(0x1, 0x0, 0x4)
    OP_DC(0x0, 0x0)
    OP_31(0x8, 0x0, 0x88)
    OP_31(0xE, 0x0, 0x88)
    OP_31(0x5, 0x0, 0x88)
    OP_31(0x4, 0x0, 0x88)
    OP_35(0x8, 0x0)
    OP_35(0xE, 0x0)
    OP_35(0x5, 0x0)
    OP_35(0x4, 0x0)
    OP_41(0x8, 0x55B, 0xFF)
    OP_41(0x8, 0x618, 0xFF)
    OP_41(0x8, 0x6E, 0xFF)
    OP_41(0xE, 0x5B5, 0xFF)
    OP_41(0xE, 0x618, 0xFF)
    OP_41(0xE, 0x6E, 0xFF)
    OP_41(0x5, 0x4D3, 0xFF)
    OP_41(0x5, 0x618, 0xFF)
    OP_41(0x5, 0x6E, 0xFF)
    OP_41(0x4, 0x4A7, 0xFF)
    OP_41(0x4, 0x618, 0xFF)
    OP_41(0x4, 0x6E, 0xFF)
    OP_37(0x8, 0x7F, 0x3)
    OP_37(0xE, 0x7F, 0x3)
    OP_37(0x5, 0x7F, 0x3)
    OP_37(0x4, 0x7F, 0x3)
    OP_31(0x8, 0x5, 0x96)
    OP_31(0xE, 0x5, 0x96)
    OP_31(0x5, 0x5, 0x96)
    OP_31(0x4, 0x5, 0x96)
    OP_DB(0x2, 0xFF)
    Jump("loc_185D")

    label("loc_1853")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185D")

    Jump("loc_1635")

    label("loc_1860")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_162B end

    def Function_14_186E(): pass

    label("Function_14_186E")

    Return()

    # Function_14_186E end

    def Function_15_186F(): pass

    label("Function_15_186F")

    Return()

    # Function_15_186F end

    def Function_16_1870(): pass

    label("Function_16_1870")

    Return()

    # Function_16_1870 end

    def Function_17_1871(): pass

    label("Function_17_1871")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D72")

    AnonymousTalk(    #12
        (
            "\x06This is a debug testing jump.\x01",
            "To check the minigames within context,\x01",
            "please use the Episode List instead.\x02",
        )
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "00 Roulette\x01",          # 0
            "01 Slots\x01",             # 1
            "02 Blackjack\x01",         # 2
            "03 Fishing\x01",           # 3
            "04 Poker\x01",             # 4
            "05 Shooting\x01",          # 5
            "06 Bug Catching\x01",      # 6
            "07 Sugoroku\x01",          # 7
            "08 Quiz\x01",              # 8
            "09 Vs Fishing\x01",        # 9
            "10 Vs Poker\x01",          # 10
            "11 Vs Blackjack\x01",      # 11
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19C5"),
        (1, "loc_19FE"),
        (2, "loc_1A37"),
        (3, "loc_1A70"),
        (4, "loc_1B45"),
        (5, "loc_1B7E"),
        (6, "loc_1C3C"),
        (7, "loc_1C75"),
        (8, "loc_1CB7"),
        (9, "loc_1CCB"),
        (10, "loc_1CF3"),
        (11, "loc_1D2C"),
        (SWITCH_DEFAULT, "loc_1D65"),
    )


    label("loc_19C5")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_19FE")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1A37")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1A70")

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

    AnonymousTalk(    #13
        (
            "ブライト家へ移動しますので、\x01",
            "裏手の池のルックポイントを探して\x01",
            "釣りをしてください。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D65")

    label("loc_1B45")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1B7E")


    Menu(
        1,
        10,
        100,
        1,
        (
            "Basic Enemies\x01",      # 0
            "Boss\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEE")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x0, 0x1, 1024, 0x0)
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1C39")

    label("loc_1BEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C39")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x0, 0x1, 1024, 0x0)
    OP_C0(0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)

    label("loc_1C39")

    Jump("loc_1D65")

    label("loc_1C3C")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1C75")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    NewScene("ED6_DT21/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1CB7")

    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D65")

    label("loc_1CCB")

    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1D, 0x4, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D65")

    label("loc_1CF3")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x1C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1D2C")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x1D, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1D65")

    label("loc_1D65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("Function_17_1871")

    label("loc_1D72")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1871 end

    SaveToFile()

Try(main)
