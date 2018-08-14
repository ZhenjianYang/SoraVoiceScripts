from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7415   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7415.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH14040 ._CH',             # 00
        'ED6_DT29/CH14040 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14880 ._CH',             # 03
        'ED6_DT29/CH14890 ._CH',             # 04
        'ED6_DT29/CH14890 ._CH',             # 05
        'ED6_DT29/CH14870 ._CH',             # 06
        'ED6_DT29/CH14870 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
        'ED6_DT29/CH14610 ._CH',             # 0A
        'ED6_DT29/CH14610 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14040P._CP',             # 00
        'ED6_DT29/CH14040P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14880P._CP',             # 03
        'ED6_DT29/CH14890P._CP',             # 04
        'ED6_DT29/CH14890P._CP',             # 05
        'ED6_DT29/CH14870P._CP',             # 06
        'ED6_DT29/CH14870P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
        'ED6_DT29/CH14610P._CP',             # 0A
        'ED6_DT29/CH14610P._CP',             # 0B
    )

    DeclMonster(
        X                   = -6210,
        Z                   = -2000,
        Y                   = 35300,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 87300,
        Z                   = 0,
        Y                   = 41010,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 91110,
        Z                   = 0,
        Y                   = 44730,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 94880,
        Z                   = 0,
        Y                   = 41000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 91010,
        Z                   = 0,
        Y                   = 37270,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -96810,
        Z                   = -6000,
        Y                   = 154910,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -3000,
        TriggerZ            = 0,
        TriggerY            = 148500,
        TriggerRange        = 1000,
        ActorX              = -3000,
        ActorZ              = 1000,
        ActorY              = 148500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 91040,
        TriggerZ            = 0,
        TriggerY            = 40970,
        TriggerRange        = 1000,
        ActorX              = 91040,
        ActorZ              = 1000,
        ActorY              = 40970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -97000,
        TriggerZ            = -6000,
        TriggerY            = 158260,
        TriggerRange        = 1000,
        ActorX              = -97000,
        ActorZ              = -5000,
        ActorY              = 158260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30,
        TriggerZ            = 0,
        TriggerY            = 31910,
        TriggerRange        = 1000,
        ActorX              = 30,
        ActorZ              = 2000,
        ActorY              = 31910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_243",          # 01, 1
        "Function_2_2E7",          # 02, 2
        "Function_3_40D",          # 03, 3
        "Function_4_48C",          # 04, 4
        "Function_5_5B2",          # 05, 5
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Return()

    # Function_0_242 end

    def Function_1_243(): pass

    label("Function_1_243")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_6F(0x0, 0)
    Jump("loc_2B4")

    label("loc_2AD")

    OP_6F(0x0, 60)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_6F(0x1, 0)
    Jump("loc_2CD")

    label("loc_2C6")

    OP_6F(0x1, 60)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF")
    OP_6F(0x2, 0)
    Jump("loc_2E6")

    label("loc_2DF")

    OP_6F(0x2, 60)

    label("loc_2E6")

    Return()

    # Function_1_243 end

    def Function_2_2E7(): pass

    label("Function_2_2E7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_35B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_340")

    label("loc_340")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA0)
    Jump("loc_3C9")

    label("loc_35B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3AA")

    label("loc_3AA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3C9")

    Jump("loc_3FF")

    label("loc_3CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3FF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2E7 end

    def Function_3_40D(): pass

    label("Function_3_40D")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CA1)
    Jump("loc_47A")

    label("loc_45E")


    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_47A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_40D end

    def Function_4_48C(): pass

    label("Function_4_48C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_500")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_4E5")

    label("loc_4E5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA2)
    Jump("loc_56E")

    label("loc_500")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_54F")

    label("loc_54F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_56E")

    Jump("loc_5A4")

    label("loc_571")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_48C end

    def Function_5_5B2(): pass

    label("Function_5_5B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #7
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_5DF")

    label("loc_5DF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74A")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_644")

    label("loc_644")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_661"),
        (1, "loc_6DC"),
        (2, "loc_70B"),
        (SWITCH_DEFAULT, "loc_73A"),
    )


    label("loc_661")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_747")

    label("loc_6DC")

    OP_A9(0x32)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #8
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_708")

    label("loc_708")

    Jump("loc_747")

    label("loc_70B")

    OP_A9(0xE)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #9
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_737")

    label("loc_737")

    Jump("loc_747")

    label("loc_73A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_747")

    label("loc_747")

    Jump("loc_5F2")

    label("loc_74A")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_5_5B2 end

    SaveToFile()

Try(main)
