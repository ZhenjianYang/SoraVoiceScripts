from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06モンスターを選んでください\x02",
    )


    label("loc_C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test\x01",                          # 0
            "10000 Killer Crab\x01",             # 1
            "10260 Red Insectos\x01",            # 2
            "10180 Lily Mover\x01",              # 3
            "10010 Killer Hornet\x01",           # 4
            "10020 Flying Feline\x01",           # 5
            "10210 Mars Sparrow\x01",            # 6
            "10190 Robber Trapper\x01",          # 7
            "11050 Giant Crop Muncher\x01",      # 8
            "10280 Forest Mist\x01",             # 9
            "10230 Pine Plant\x01",              # 10
            "10240 Rhinocider\x01",              # 11
            "10050 Marsh Chupacabra\x01",        # 12
            "Cancel\x01",                        # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_214"),
        (1, "loc_224"),
        (2, "loc_234"),
        (3, "loc_244"),
        (4, "loc_254"),
        (5, "loc_264"),
        (6, "loc_274"),
        (7, "loc_284"),
        (8, "loc_294"),
        (9, "loc_2A4"),
        (10, "loc_2B4"),
        (11, "loc_2C4"),
        (12, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_214")

    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_224")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_234")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_244")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_254")

    Battle(0x7DD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_264")

    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_274")

    Battle(0x6E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_284")

    Battle(0x3C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_294")

    Battle(0x7DF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_2A4")

    Battle(0x42, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_2B4")

    Battle(0x45, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_2C4")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_2D4")

    Battle(0x7D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EE")

    label("loc_2E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8")

    label("loc_2FB")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
