from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5506   ._SN',
        MapName             = 'Other',
        Location            = 'C5506.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'ED6_DT29/CH12180 ._CH',             # 00
        'ED6_DT29/CH12181 ._CH',             # 01
        'ED6_DT29/CH12230 ._CH',             # 02
        'ED6_DT29/CH12231 ._CH',             # 03
        'ED6_DT29/CH12270 ._CH',             # 04
        'ED6_DT29/CH12271 ._CH',             # 05
        'ED6_DT29/CH12360 ._CH',             # 06
        'ED6_DT29/CH12361 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12180P._CP',             # 00
        'ED6_DT29/CH12181P._CP',             # 01
        'ED6_DT29/CH12230P._CP',             # 02
        'ED6_DT29/CH12231P._CP',             # 03
        'ED6_DT29/CH12270P._CP',             # 04
        'ED6_DT29/CH12271P._CP',             # 05
        'ED6_DT29/CH12360P._CP',             # 06
        'ED6_DT29/CH12361P._CP',             # 07
    )

    DeclNpc(
        X                   = 44320,
        Z                   = 1000,
        Y                   = -17010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 8170,
        Z                   = 0,
        Y                   = -15930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16960,
        Z                   = 0,
        Y                   = 5750,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36290,
        Z                   = 0,
        Y                   = 35730,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 48370,
        Z                   = 0,
        Y                   = 5530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19010,
        Z                   = -4000,
        Y                   = -840,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25740,
        Z                   = -4000,
        Y                   = -9090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29330,
        Z                   = 0,
        Y                   = 13340,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40750,
        Z                   = 0,
        Y                   = -9890,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -57380,
        Z                   = 0,
        Y                   = 9430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 44320,
        TriggerZ            = 0,
        TriggerY            = -16350,
        TriggerRange        = 1000,
        ActorX              = 44320,
        ActorZ              = 0,
        ActorY              = -17010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54110,
        TriggerZ            = 0,
        TriggerY            = 4910,
        TriggerRange        = 1000,
        ActorX              = 54770,
        ActorZ              = 0,
        ActorY              = 4960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45550,
        TriggerZ            = 0,
        TriggerY            = 37990,
        TriggerRange        = 1000,
        ActorX              = 46210,
        ActorZ              = 0,
        ActorY              = 37990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -57310,
        TriggerZ            = 0,
        TriggerY            = -9280,
        TriggerRange        = 1000,
        ActorX              = -57940,
        ActorZ              = 0,
        ActorY              = -9480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22600,
        TriggerZ            = -4000,
        TriggerY            = 15420,
        TriggerRange        = 1000,
        ActorX              = -23170,
        ActorZ              = -4000,
        ActorY              = 15420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_2BB",          # 01, 1
        "Function_2_35B",          # 02, 2
        "Function_3_371",          # 03, 3
        "Function_4_48C",          # 04, 4
        "Function_5_5A7",          # 05, 5
        "Function_6_6C2",          # 06, 6
        "Function_7_7D9",          # 07, 7
        "Function_8_8F0",          # 08, 8
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Return()

    # Function_0_2BA end

    def Function_1_2BB(): pass

    label("Function_1_2BB")

    OP_BE(0x0, 0x1, 0x2, 0x28, 0x0, 0x2, -34850, -4400, -21210, -7610, -3350, 18110)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF")
    OP_6F(0x0, 0)
    Jump("loc_2F6")

    label("loc_2EF")

    OP_6F(0x0, 60)

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308")
    OP_6F(0x1, 0)
    Jump("loc_30F")

    label("loc_308")

    OP_6F(0x1, 60)

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321")
    OP_6F(0x2, 0)
    Jump("loc_328")

    label("loc_321")

    OP_6F(0x2, 60)

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A")
    OP_6F(0x3, 0)
    Jump("loc_341")

    label("loc_33A")

    OP_6F(0x3, 60)

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353")
    OP_6F(0x4, 0)
    Jump("loc_35A")

    label("loc_353")

    OP_6F(0x4, 60)

    label("loc_35A")

    Return()

    # Function_1_2BB end

    def Function_2_35B(): pass

    label("Function_2_35B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_370")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_35B")

    label("loc_370")

    Return()

    # Function_2_35B end

    def Function_3_371(): pass

    label("Function_3_371")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x9, 1)"), scpexpr(EXPR_END)), "loc_3E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x09\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1130)
    Jump("loc_446")

    label("loc_3E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x09\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x09\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_446")

    Jump("loc_47A")

    label("loc_449")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_47A")

    Sleep(30)
    Call(0, 8)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_371 end

    def Function_4_48C(): pass

    label("Function_4_48C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xCF, 1)"), scpexpr(EXPR_END)), "loc_4FB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xCF\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1132)
    Jump("loc_561")

    label("loc_4FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xCF\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xCF\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_561")

    Jump("loc_595")

    label("loc_564")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_595")

    Sleep(30)
    Call(0, 8)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_48C end

    def Function_5_5A7(): pass

    label("Function_5_5A7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x125, 1)"), scpexpr(EXPR_END)), "loc_616")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x25\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1133)
    Jump("loc_67C")

    label("loc_616")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x25\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x25\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_67C")

    Jump("loc_6B0")

    label("loc_67F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6B0")

    Sleep(30)
    Call(0, 8)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5A7 end

    def Function_6_6C2(): pass

    label("Function_6_6C2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_731")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1134)
    Jump("loc_797")

    label("loc_731")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_797")

    Jump("loc_7CB")

    label("loc_79A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_6C2 end

    def Function_7_7D9(): pass

    label("Function_7_7D9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_848")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1135)
    Jump("loc_8AE")

    label("loc_848")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_8AE")

    Jump("loc_8E2")

    label("loc_8B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8E2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_7D9 end

    def Function_8_8F0(): pass

    label("Function_8_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B2")

    ChrTalk(    #15
        0x101,
        (
            "#1004F啊……！\x02\x03",

            "难不成，这个\x01",
            "就是我们的装备？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        (
            "#811F嗯，似乎是呢⊙\x02\x03",

            "#1310F说不定其它装备\x01",
            "也被藏在什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1006F嗯～\x01",
            "虽然想避开和魔兽的战斗，\x01",
            "但似乎值得探索一下呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    label("loc_9B2")

    Return()

    # Function_8_8F0 end

    SaveToFile()

Try(main)
