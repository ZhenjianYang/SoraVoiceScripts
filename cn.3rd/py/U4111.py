from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4111   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 124330,
        TriggerZ            = 0,
        TriggerY            = 67840,
        TriggerRange        = 1000,
        ActorX              = 124330,
        ActorZ              = 1000,
        ActorY              = 67840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6220,
        TriggerZ            = 0,
        TriggerY            = 61170,
        TriggerRange        = 1000,
        ActorX              = -6220,
        ActorZ              = 1000,
        ActorY              = 61170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_142",          # 02, 2
        "Function_3_23A",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_106")
    OP_B1("U4111_y")
    Jump("loc_10F")

    label("loc_106")

    OP_B1("U4111_n")

    label("loc_10F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121")
    OP_6F(0x2, 0)
    Jump("loc_128")

    label("loc_121")

    OP_6F(0x2, 60)

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A")
    OP_6F(0x3, 0)
    Jump("loc_141")

    label("loc_13A")

    OP_6F(0x3, 60)

    label("loc_141")

    Return()

    # Function_1_F3 end

    def Function_2_142(): pass

    label("Function_2_142")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×５０\x01",
            "\x07\x02#57I水之耀晶片×５０\x01",
            "\x07\x02#58I火之耀晶片×５０\x01",
            "\x07\x02#59I风之耀晶片×５０\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27BC)
    Jump("loc_228")

    label("loc_20C")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_228")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_142 end

    def Function_3_23A(): pass

    label("Function_3_23A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)

    AnonymousTalk(    #2
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×５０\x01",
            "\x07\x02#57I水之耀晶片×５０\x01",
            "\x07\x02#58I火之耀晶片×５０\x01",
            "\x07\x02#59I风之耀晶片×５０\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27BD)
    Jump("loc_31C")

    label("loc_302")


    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_31C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_23A end

    SaveToFile()

Try(main)
