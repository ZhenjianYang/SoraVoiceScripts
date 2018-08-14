from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4280   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4280.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        '',                                     # 9
        '',                                     # 10
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


    AddCharChip(
        'ED6_DT29/CH14510 ._CH',             # 00
        'ED6_DT29/CH14511 ._CH',             # 01
        'ED6_DT29/CH14790 ._CH',             # 02
        'ED6_DT29/CH14790 ._CH',             # 03
        'ED6_DT29/CH14450 ._CH',             # 04
        'ED6_DT29/CH14451 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14510P._CP',             # 00
        'ED6_DT29/CH14511P._CP',             # 01
        'ED6_DT29/CH14790P._CP',             # 02
        'ED6_DT29/CH14790P._CP',             # 03
        'ED6_DT29/CH14450P._CP',             # 04
        'ED6_DT29/CH14451P._CP',             # 05
    )

    DeclMonster(
        X                   = -40,
        Z                   = 0,
        Y                   = -123960,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40,
        Z                   = 0,
        Y                   = -139910,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 60,
        TriggerZ            = 0,
        TriggerY            = -101930,
        TriggerRange        = 1000,
        ActorX              = 60,
        ActorZ              = 600,
        ActorY              = -101930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6950,
        TriggerZ            = -1000,
        TriggerY            = -120800,
        TriggerRange        = 1000,
        ActorX              = 6950,
        ActorZ              = 0,
        ActorY              = -120800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4360,
        TriggerZ            = -1000,
        TriggerY            = -131740,
        TriggerRange        = 1000,
        ActorX              = -4360,
        ActorZ              = 0,
        ActorY              = -131740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_17F",          # 01, 1
        "Function_2_1D3",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_417",          # 04, 4
        "Function_5_423",          # 05, 5
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Return()

    # Function_0_17E end

    def Function_1_17F(): pass

    label("Function_1_17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    OP_72(0x1001, 0x0)
    ExitThread()
    Jump("loc_194")

    label("loc_190")

    OP_64(0x0, 0x1)

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 3)), scpexpr(EXPR_END)), "loc_1A0")
    OP_1C(0x1, 0x0, 0x4)

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2")
    OP_6F(0xF, 0)
    Jump("loc_1B9")

    label("loc_1B2")

    OP_6F(0xF, 60)

    label("loc_1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB")
    OP_6F(0x10, 0)
    Jump("loc_1D2")

    label("loc_1CB")

    OP_6F(0x10, 60)

    label("loc_1D2")

    Return()

    # Function_1_17F end

    def Function_2_1D3(): pass

    label("Function_2_1D3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x194, 1)"), scpexpr(EXPR_END)), "loc_247")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x94\x01\x07\x00。\x02",
    )

    Jump("loc_22C")

    label("loc_22C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A6)
    Jump("loc_2B5")

    label("loc_247")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x94\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x94\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_296")

    label("loc_296")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_2B5")

    Jump("loc_2E9")

    label("loc_2B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1D3 end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_369")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_34E")

    label("loc_34E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A7)
    Jump("loc_3D5")

    label("loc_369")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3B6")

    label("loc_3B6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_3D5")

    Jump("loc_409")

    label("loc_3D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_409")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2F7 end

    def Function_4_417(): pass

    label("Function_4_417")

    TalkBegin(0xFF)
    Sleep(1500)
    TalkEnd(0xFF)
    Return()

    # Function_4_417 end

    def Function_5_423(): pass

    label("Function_5_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 2)), scpexpr(EXPR_END)), "loc_48A")
    TalkBegin(0xFF)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05门上的锁打开了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x271B)
    OP_64(0x0, 0x1)
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_1C(0x1, 0x0, 0x4)
    TalkEnd(0xFF)
    Jump("loc_4DC")

    label("loc_48A")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝物库的门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_4DC")

    Return()

    # Function_5_423 end

    SaveToFile()

Try(main)
