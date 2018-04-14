from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2202   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2202.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        '卢安方向',                             # 10
        '街景林道',                             # 11
        '玛诺利亚村方向',                       # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH11060 ._CH',             # 0A
        'ED6_DT09/CH11061 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
        'ED6_DT29/CH12100 ._CH',             # 0E
        'ED6_DT29/CH12101 ._CH',             # 0F
        'ED6_DT29/CH12150 ._CH',             # 10
        'ED6_DT29/CH12151 ._CH',             # 11
        'ED6_DT29/CH12160 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH11060P._CP',             # 0A
        'ED6_DT09/CH11061P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
        'ED6_DT29/CH12100P._CP',             # 0E
        'ED6_DT29/CH12101P._CP',             # 0F
        'ED6_DT29/CH12150P._CP',             # 10
        'ED6_DT29/CH12151P._CP',             # 11
        'ED6_DT29/CH12160P._CP',             # 12
    )

    DeclNpc(
        X                   = 137480,
        Z                   = -2000,
        Y                   = -212630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 146110,
        Z                   = -2000,
        Y                   = -272220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 195320,
        Z                   = -2000,
        Y                   = -200020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 117860,
        Z                   = -1990,
        Y                   = -86810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 108600,
        Z                   = -2090,
        Y                   = -127120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 127020,
        Z                   = -2029,
        Y                   = -168530,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x183,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 131400,
        Z                   = -1930,
        Y                   = -226630,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 136960,
        Z                   = -2020,
        Y                   = -153050,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x183,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 123750,
        Z                   = -6120,
        Y                   = -163430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x189,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 113340,
        Z                   = -6030,
        Y                   = -111320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x189,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 107810,
        Z                   = -6150,
        Y                   = -227590,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 171570,
        Y                   = -3000,
        Z                   = -204390,
        Range               = 173310,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFD053A,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 132230,
        Y                   = -3000,
        Z                   = -209630,
        Range               = 142840,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFCB5B2,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 123800,
        TriggerZ            = -6110,
        TriggerY            = -164160,
        TriggerRange        = 1000,
        ActorX              = 123890,
        ActorZ              = -6040,
        ActorY              = -164820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 110610,
        TriggerZ            = -2050,
        TriggerY            = -169010,
        TriggerRange        = 1000,
        ActorX              = 111270,
        ActorZ              = -1960,
        ActorY              = -169020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 114670,
        TriggerZ            = -6010,
        TriggerY            = -111030,
        TriggerRange        = 1000,
        ActorX              = 115310,
        ActorZ              = -5950,
        ActorY              = -111030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 145130,
        TriggerZ            = -2029,
        TriggerY            = -194770,
        TriggerRange        = 1500,
        ActorX              = 145130,
        ActorZ              = -500,
        ActorY              = -194770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 143160,
        TriggerZ            = -1960,
        TriggerY            = -203990,
        TriggerRange        = 1500,
        ActorX              = 143160,
        ActorZ              = -550,
        ActorY              = -203990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 110290,
        TriggerZ            = -6670,
        TriggerY            = -241280,
        TriggerRange        = 1000,
        ActorX              = 109660,
        ActorZ              = -6650,
        ActorY              = -244800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_39E",          # 00, 0
        "Function_1_39F",          # 01, 1
        "Function_2_450",          # 02, 2
        "Function_3_466",          # 03, 3
        "Function_4_57D",          # 04, 4
        "Function_5_694",          # 05, 5
        "Function_6_7FE",          # 06, 6
        "Function_7_957",          # 07, 7
        "Function_8_9AA",          # 08, 8
        "Function_9_A08",          # 09, 9
        "Function_10_D2C",         # 0A, 10
    )


    def Function_0_39E(): pass

    label("Function_0_39E")

    Return()

    # Function_0_39E end

    def Function_1_39F(): pass

    label("Function_1_39F")

    OP_16(0x2, 0xFA0, 0x2710, 0xFFFB4128, 0x230028)
    OP_22(0x1C8, 0x1, 0x64)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD")
    OP_6F(0x1, 0)
    Jump("loc_3E4")

    label("loc_3DD")

    OP_6F(0x1, 60)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    OP_6F(0x2, 0)
    Jump("loc_3FD")

    label("loc_3F6")

    OP_6F(0x2, 60)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F")
    OP_6F(0x3, 0)
    Jump("loc_416")

    label("loc_40F")

    OP_6F(0x3, 60)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_445")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_430")
    OP_8C(0x8, 180, 0)

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_442")

    Jump("loc_44F")

    label("loc_445")

    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x1, 0x80)

    label("loc_44F")

    Return()

    # Function_1_39F end

    def Function_2_450(): pass

    label("Function_2_450")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_465")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_450")

    label("loc_465")

    Return()

    # Function_2_450 end

    def Function_3_466(): pass

    label("Function_3_466")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_4D5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1307)
    Jump("loc_53B")

    label("loc_4D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_53B")

    Jump("loc_56F")

    label("loc_53E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_56F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_466 end

    def Function_4_57D(): pass

    label("Function_4_57D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_655")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_5EC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1308)
    Jump("loc_652")

    label("loc_5EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF5\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_652")

    Jump("loc_686")

    label("loc_655")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_686")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_57D end

    def Function_5_694(): pass

    label("Function_5_694")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E0, 1)"), scpexpr(EXPR_END)), "loc_703")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xE0\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1309)
    Jump("loc_769")

    label("loc_703")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xE0\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE0\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_769")

    Jump("loc_79D")

    label("loc_76C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_79D")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_7BC")
    Jump("loc_7F5")

    label("loc_7BC")


    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xE0\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x1F\xE0\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_7F5")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_694 end

    def Function_6_7FE(): pass

    label("Function_6_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_956")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8AE")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #11
        0x106,
        (
            "#050F这么说来\x01",
            "还有拍摄的工作没处理完啊。\x02\x03",

            "还是先做完比较好吧。\x01",
            "因为调查时间或许会拖得很长。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #12
        0x101,
        (
            "#1015F啊，嗯。\x01",
            "那样也好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93B")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_93B")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #13
        0x103,
        (
            "#020F这么说来还有\x01",
            "拍摄的工作没处理完呢。\x02\x03",

            "先做完怎么样？\x01",
            "调查时间或许会拖得很长哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #14
        0x101,
        (
            "#1015F啊，嗯。\x01",
            "那样也好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93B")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_956")

    Return()

    # Function_6_7FE end

    def Function_7_957(): pass

    label("Function_7_957")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05东　杰尼丝王立学院　２５２塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_957 end

    def Function_8_9AA(): pass

    label("Function_8_9AA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05南　卢安市\x01",
            "北　玛诺利亚村　　　３１２塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_9AA end

    def Function_9_A08(): pass

    label("Function_9_A08")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_A1C"),
        (101, "loc_A1C"),
        (102, "loc_B6E"),
        (SWITCH_DEFAULT, "loc_CC0"),
    )


    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 2)), scpexpr(EXPR_END)), "loc_A24")
    Return()

    label("loc_A24")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_B09"),
        (SWITCH_DEFAULT, "loc_B2C"),
    )


    label("loc_B09")

    Fade(500)
    OP_89(0x0, 137640, -2000, -205720, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_B2C")

    Battle(0xEF1, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 137640, -2000, -205720, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_B65"),
        (1, "loc_B68"),
        (SWITCH_DEFAULT, "loc_B6B"),
    )


    label("loc_B65")

    EventEnd(0x0)
    Return()

    label("loc_B68")

    OP_B4(0x0)
    Return()

    label("loc_B6B")

    Jump("loc_CC0")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 2)), scpexpr(EXPR_END)), "loc_B76")
    Return()

    label("loc_B76")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_C5B"),
        (SWITCH_DEFAULT, "loc_C7E"),
    )


    label("loc_C5B")

    Fade(500)
    OP_89(0x0, 137360, -2000, -219630, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_C7E")

    Battle(0xEF9, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 137360, -2000, -219630, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_CB7"),
        (1, "loc_CBA"),
        (SWITCH_DEFAULT, "loc_CBD"),
    )


    label("loc_CB7")

    EventEnd(0x0)
    Return()

    label("loc_CBA")

    OP_B4(0x0)
    Return()

    label("loc_CBD")

    Jump("loc_CC0")

    label("loc_CC0")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20FA)
    OP_28(0xB9, 0x4, 0x10)
    OP_28(0xB9, 0x4, 0x2)
    OP_28(0xB9, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_9_A08 end

    def Function_10_D2C(): pass

    label("Function_10_D2C")

    EventBegin(0x1)

    ChrTalk(    #20
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_D58():
        OP_6D(109750, -6680, -243120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D58)

    def lambda_D70():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D70)

    def lambda_D80():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_D80)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")
    OP_C0(0xE, 0x17, 0x1AED2, 0xFFFFE5F2, 0xFFFC5180, 0xB4, 0x1AC16, 0xFFFFE958, 0xFFFC406E)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_E16")

    label("loc_E07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E16")
    EventEnd(0x1)

    label("loc_E16")

    Return()

    # Function_10_D2C end

    SaveToFile()

Try(main)
