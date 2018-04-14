from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5510   ._SN',
        MapName             = 'Other',
        Location            = 'C5510.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 5,
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
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12240 ._CH',             # 00
        'ED6_DT29/CH12241 ._CH',             # 01
        'ED6_DT29/CH12370 ._CH',             # 02
        'ED6_DT29/CH12371 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12270 ._CH',             # 06
        'ED6_DT29/CH12271 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12240P._CP',             # 00
        'ED6_DT29/CH12241P._CP',             # 01
        'ED6_DT29/CH12370P._CP',             # 02
        'ED6_DT29/CH12371P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12270P._CP',             # 06
        'ED6_DT29/CH12271P._CP',             # 07
    )

    DeclNpc(
        X                   = 44500,
        Z                   = 1000,
        Y                   = -10740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 2820,
        Z                   = 0,
        Y                   = 42410,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1060,
        Z                   = 0,
        Y                   = -82420,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8210,
        Z                   = 0,
        Y                   = -23060,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4160,
        Z                   = 0,
        Y                   = -33900,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2090,
        Z                   = 0,
        Y                   = -9120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7920,
        Z                   = 0,
        Y                   = -37050,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -40430,
        TriggerZ            = 0,
        TriggerY            = -25410,
        TriggerRange        = 1000,
        ActorX              = -40520,
        ActorZ              = 0,
        ActorY              = -24710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44500,
        TriggerZ            = 0,
        TriggerY            = -11400,
        TriggerRange        = 1000,
        ActorX              = 44500,
        ActorZ              = 0,
        ActorY              = -10740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_1FB",          # 01, 1
        "Function_2_2AE",          # 02, 2
        "Function_3_2C4",          # 03, 3
        "Function_4_3DB",          # 04, 4
        "Function_5_4F2",          # 05, 5
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Return()

    # Function_0_1FA end

    def Function_1_1FB(): pass

    label("Function_1_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D")
    OP_6F(0x7, 0)
    Jump("loc_214")

    label("loc_20D")

    OP_6F(0x7, 60)

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226")
    OP_6F(0x8, 0)
    Jump("loc_22D")

    label("loc_226")

    OP_6F(0x8, 60)

    label("loc_22D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_285")
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    Jump("loc_2AD")

    label("loc_285")

    OP_78(0xDC, 0xE6, 0xFF)
    OP_7A(0x4, 0x2)
    OP_7A(0x5, 0x2)
    OP_7A(0x6, 0x2)
    OP_7A(0x7, 0x2)
    OP_7A(0x8, 0x2)
    OP_7A(0x9, 0x2)
    OP_7A(0xA, 0x2)
    OP_7A(0xB, 0x2)
    OP_7A(0xC, 0x2)

    label("loc_2AD")

    Return()

    # Function_1_1FB end

    def Function_2_2AE(): pass

    label("Function_2_2AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2AE")

    label("loc_2C3")

    Return()

    # Function_2_2AE end

    def Function_3_2C4(): pass

    label("Function_3_2C4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_333")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1143)
    Jump("loc_399")

    label("loc_333")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_399")

    Jump("loc_3CD")

    label("loc_39C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2C4 end

    def Function_4_3DB(): pass

    label("Function_4_3DB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x150, 1)"), scpexpr(EXPR_END)), "loc_44A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x50\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1144)
    Jump("loc_4B0")

    label("loc_44A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x50\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x50\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_4B0")

    Jump("loc_4E4")

    label("loc_4B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3DB end

    def Function_5_4F2(): pass

    label("Function_5_4F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x416), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FF")
    Return()

    label("loc_4FF")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_595")
    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "\x07\x05认证组件已经启动了……\x01",
            "但好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_813")

    label("loc_595")

    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x05认证单元已经启动了……\x01",
            "但这个地方好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_644")

    ChrTalk(    #8
        0x10A,
        (
            "#814F艾丝蒂尔。\x01",
            "好像不是这里哦。\x02\x03",

            "先往前走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    Jump("loc_810")

    label("loc_644")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(    #9
        0x10A,
        (
            "#812F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_68A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")

    ChrTalk(    #10
        0x10A,
        (
            "#813F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_6C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FC")

    ChrTalk(    #11
        0x10A,
        (
            "#814F这里好像\x01",
            "没什么可用的东西吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_6FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_736")

    ChrTalk(    #12
        0x10A,
        (
            "#817F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_736")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770")

    ChrTalk(    #13
        0x10A,
        (
            "#818F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_770")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")

    ChrTalk(    #14
        0x10A,
        (
            "#819F嗯～看来\x01",
            "没找对地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_7A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(    #15
        0x10A,
        (
            "#1315F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_7D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80D")

    ChrTalk(    #16
        0x10A,
        (
            "#1316F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    OP_A2(0x0)

    label("loc_810")

    TalkEnd(0xFF)

    label("loc_813")

    ClearMapFlags(0x80)
    Return()

    # Function_5_4F2 end

    SaveToFile()

Try(main)
