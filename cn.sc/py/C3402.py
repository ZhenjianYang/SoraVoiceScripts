from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3402   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        ' ',                                    # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12110 ._CH',             # 00
        'ED6_DT29/CH12111 ._CH',             # 01
        'ED6_DT29/CH12410 ._CH',             # 02
        'ED6_DT29/CH12411 ._CH',             # 03
        'ED6_DT29/CH12250 ._CH',             # 04
        'ED6_DT29/CH12251 ._CH',             # 05
        'ED6_DT29/CH12130 ._CH',             # 06
        'ED6_DT29/CH12131 ._CH',             # 07
        'ED6_DT09/CH10130 ._CH',             # 08
        'ED6_DT09/CH10131 ._CH',             # 09
        'ED6_DT09/CH10750 ._CH',             # 0A
        'ED6_DT09/CH10751 ._CH',             # 0B
        'ED6_DT29/CH12270 ._CH',             # 0C
        'ED6_DT29/CH12271 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12110P._CP',             # 00
        'ED6_DT29/CH12111P._CP',             # 01
        'ED6_DT29/CH12410P._CP',             # 02
        'ED6_DT29/CH12411P._CP',             # 03
        'ED6_DT29/CH12250P._CP',             # 04
        'ED6_DT29/CH12251P._CP',             # 05
        'ED6_DT29/CH12130P._CP',             # 06
        'ED6_DT29/CH12131P._CP',             # 07
        'ED6_DT09/CH10130P._CP',             # 08
        'ED6_DT09/CH10131P._CP',             # 09
        'ED6_DT09/CH10750P._CP',             # 0A
        'ED6_DT09/CH10751P._CP',             # 0B
        'ED6_DT29/CH12270P._CP',             # 0C
        'ED6_DT29/CH12271P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x49,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -21480,
        Z                   = 0,
        Y                   = 22770,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3360,
        Z                   = 0,
        Y                   = 13070,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6390,
        Z                   = 0,
        Y                   = -12560,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34010,
        Z                   = 0,
        Y                   = -19450,
        Unknown_0C          = 45,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 57480,
        Z                   = 0,
        Y                   = -19510,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28530,
        Z                   = 0,
        Y                   = 43350,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35840,
        Z                   = 0,
        Y                   = 38570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -59190,
        TriggerZ            = 0,
        TriggerY            = 15820,
        TriggerRange        = 1000,
        ActorX              = -59910,
        ActorZ              = 0,
        ActorY              = 16200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37640,
        TriggerZ            = 0,
        TriggerY            = 45540,
        TriggerRange        = 1000,
        ActorX              = 37820,
        ActorZ              = 0,
        ActorY              = 46220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60380,
        TriggerZ            = 0,
        TriggerY            = -16890,
        TriggerRange        = 1000,
        ActorX              = 61110,
        ActorZ              = 0,
        ActorY              = -16820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11940,
        TriggerZ            = 0,
        TriggerY            = -15660,
        TriggerRange        = 1000,
        ActorX              = -11860,
        ActorZ              = 0,
        ActorY              = -16490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28E",          # 00, 0
        "Function_1_28F",          # 01, 1
        "Function_2_335",          # 02, 2
        "Function_3_44C",          # 03, 3
        "Function_4_563",          # 04, 4
        "Function_5_6CD",          # 05, 5
        "Function_6_7E4",          # 06, 6
        "Function_7_96C",          # 07, 7
        "Function_8_9BE",          # 08, 8
    )


    def Function_0_28E(): pass

    label("Function_0_28E")

    Return()

    # Function_0_28E end

    def Function_1_28F(): pass

    label("Function_1_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1")
    OP_6F(0x0, 0)
    Jump("loc_2A8")

    label("loc_2A1")

    OP_6F(0x0, 60)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA")
    OP_6F(0x1, 0)
    Jump("loc_2C1")

    label("loc_2BA")

    OP_6F(0x1, 60)

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3")
    OP_6F(0x2, 0)
    Jump("loc_2DA")

    label("loc_2D3")

    OP_6F(0x2, 60)

    label("loc_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x3, 0)
    Jump("loc_2F3")

    label("loc_2EC")

    OP_6F(0x3, 60)

    label("loc_2F3")

    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_328")
    OP_82(0x80, 0x2)
    OP_82(0x81, 0x2)
    OP_82(0x82, 0x2)
    OP_82(0x83, 0x2)
    OP_82(0x84, 0x2)
    OP_82(0x85, 0x2)
    OP_82(0x86, 0x2)
    OP_82(0x87, 0x2)
    OP_82(0x88, 0x2)
    OP_22(0x1C7, 0x0, 0x64)
    Jump("loc_334")

    label("loc_328")

    OP_43(0x8, 0x0, 0x0, 0x6)
    OP_22(0x10B, 0x0, 0x64)

    label("loc_334")

    Return()

    # Function_1_28F end

    def Function_2_335(): pass

    label("Function_2_335")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x169, 1)"), scpexpr(EXPR_END)), "loc_3A4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x69\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1562)
    Jump("loc_40A")

    label("loc_3A4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x69\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x69\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_40A")

    Jump("loc_43E")

    label("loc_40D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_43E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_335 end

    def Function_3_44C(): pass

    label("Function_3_44C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x182, 1)"), scpexpr(EXPR_END)), "loc_4BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x82\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1564)
    Jump("loc_521")

    label("loc_4BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x82\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x82\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_521")

    Jump("loc_555")

    label("loc_524")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_555")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_44C end

    def Function_4_563(): pass

    label("Function_4_563")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E3, 1)"), scpexpr(EXPR_END)), "loc_5D2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xE3\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1566)
    Jump("loc_638")

    label("loc_5D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xE3\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE3\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_638")

    Jump("loc_66C")

    label("loc_63B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_66C")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6C4")

    label("loc_68B")


    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xE3\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x1F\xE3\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_6C4")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_563 end

    def Function_5_6CD(): pass

    label("Function_5_6CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_73C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1567)
    Jump("loc_7A2")

    label("loc_73C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_7A2")

    Jump("loc_7D6")

    label("loc_7A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7D6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6CD end

    def Function_6_7E4(): pass

    label("Function_6_7E4")

    Call(0, 7)
    OP_43(0x8, 0x3, 0x0, 0x8)
    PlayEffect(0x9A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9A, 0x1, 0x6E)
    Call(0, 7)
    PlayEffect(0x9B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9B, 0x1, 0x6E)
    Call(0, 7)
    PlayEffect(0x9C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9C, 0x1, 0x6E)
    Call(0, 7)
    PlayEffect(0x9D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9D, 0x1, 0x6E)
    Call(0, 7)
    PlayEffect(0x9E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9E, 0x1, 0x6E)
    Call(0, 7)
    PlayEffect(0x9F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9F, 0x1, 0x6E)
    Return()

    # Function_6_7E4 end

    def Function_7_96C(): pass

    label("Function_7_96C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_98D"),
        (1, "loc_995"),
        (2, "loc_99D"),
        (3, "loc_9A5"),
        (4, "loc_9AD"),
        (SWITCH_DEFAULT, "loc_9B5"),
    )


    label("loc_98D")

    Sleep(500)
    Jump("loc_9BD")

    label("loc_995")

    Sleep(1000)
    Jump("loc_9BD")

    label("loc_99D")

    Sleep(1500)
    Jump("loc_9BD")

    label("loc_9A5")

    Sleep(2000)
    Jump("loc_9BD")

    label("loc_9AD")

    Sleep(2500)
    Jump("loc_9BD")

    label("loc_9B5")

    Sleep(3000)
    Jump("loc_9BD")

    label("loc_9BD")

    Return()

    # Function_7_96C end

    def Function_8_9BE(): pass

    label("Function_8_9BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D4")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_8_9BE")

    label("loc_9D4")

    Return()

    # Function_8_9BE end

    SaveToFile()

Try(main)
