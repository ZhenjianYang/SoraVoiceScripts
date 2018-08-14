from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4133   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4133.x',
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
        TriggerX            = 67050,
        TriggerZ            = 0,
        TriggerY            = -2510,
        TriggerRange        = 1000,
        ActorX              = 67000,
        ActorZ              = 1000,
        ActorY              = -3250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24840,
        TriggerZ            = 0,
        TriggerY            = 52550,
        TriggerRange        = 1000,
        ActorX              = -24950,
        ActorZ              = 1000,
        ActorY              = 53250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34990,
        TriggerZ            = 0,
        TriggerY            = 114350,
        TriggerRange        = 1000,
        ActorX              = 34900,
        ActorZ              = 1000,
        ActorY              = 115070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 99160,
        TriggerZ            = 0,
        TriggerY            = 114590,
        TriggerRange        = 1000,
        ActorX              = 99120,
        ActorZ              = 1000,
        ActorY              = 115300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_1A0",          # 02, 2
        "Function_3_2C6",          # 03, 3
        "Function_4_360",          # 04, 4
        "Function_5_3FA",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    OP_6F(0x19, 0)
    Jump("loc_154")

    label("loc_14D")

    OP_6F(0x19, 60)

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166")
    OP_6F(0x1A, 0)
    Jump("loc_16D")

    label("loc_166")

    OP_6F(0x1A, 60)

    label("loc_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F")
    OP_6F(0x1B, 0)
    Jump("loc_186")

    label("loc_17F")

    OP_6F(0x1B, 60)

    label("loc_186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198")
    OP_6F(0x1C, 0)
    Jump("loc_19F")

    label("loc_198")

    OP_6F(0x1C, 60)

    label("loc_19F")

    Return()

    # Function_1_13B end

    def Function_2_1A0(): pass

    label("Function_2_1A0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x168, 1)"), scpexpr(EXPR_END)), "loc_214")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x68\x01\x07\x00。\x02",
    )

    Jump("loc_1F9")

    label("loc_1F9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278E)
    Jump("loc_282")

    label("loc_214")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x68\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x68\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_263")

    label("loc_263")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_282")

    Jump("loc_2B8")

    label("loc_285")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1A0 end

    def Function_3_2C6(): pass

    label("Function_3_2C6")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_6F(0x1A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(500)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02５００米拉\x07\x00。\x02",
    )

    Jump("loc_322")

    label("loc_322")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x278F)
    Jump("loc_34E")

    label("loc_334")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_34E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2C6 end

    def Function_4_360(): pass

    label("Function_4_360")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x1E)
    OP_73(0x1B)
    OP_6F(0x1B, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(500)

    AnonymousTalk(    #5
        "\x07\x00得到了\x07\x02５００米拉\x07\x00。\x02",
    )

    Jump("loc_3BC")

    label("loc_3BC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2790)
    Jump("loc_3E8")

    label("loc_3CE")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3E8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_360 end

    def Function_5_3FA(): pass

    label("Function_5_3FA")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x1E)
    OP_73(0x1C)
    OP_6F(0x1C, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(500)

    AnonymousTalk(    #7
        "\x07\x00得到了\x07\x02５００米拉\x07\x00。\x02",
    )

    Jump("loc_456")

    label("loc_456")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2791)
    Jump("loc_482")

    label("loc_468")


    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_482")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_3FA end

    SaveToFile()

Try(main)
