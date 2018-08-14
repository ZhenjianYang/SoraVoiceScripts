from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7103   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        'ED6_DT29/CH14070 ._CH',             # 00
        'ED6_DT29/CH14071 ._CH',             # 01
        'ED6_DT29/CH14830 ._CH',             # 02
        'ED6_DT29/CH14831 ._CH',             # 03
        'ED6_DT29/CH14910 ._CH',             # 04
        'ED6_DT29/CH14911 ._CH',             # 05
        'ED6_DT29/CH14920 ._CH',             # 06
        'ED6_DT29/CH14921 ._CH',             # 07
        'ED6_DT29/CH14930 ._CH',             # 08
        'ED6_DT29/CH14931 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14070P._CP',             # 00
        'ED6_DT29/CH14071P._CP',             # 01
        'ED6_DT29/CH14830P._CP',             # 02
        'ED6_DT29/CH14831P._CP',             # 03
        'ED6_DT29/CH14910P._CP',             # 04
        'ED6_DT29/CH14911P._CP',             # 05
        'ED6_DT29/CH14920P._CP',             # 06
        'ED6_DT29/CH14921P._CP',             # 07
        'ED6_DT29/CH14930P._CP',             # 08
        'ED6_DT29/CH14931P._CP',             # 09
    )

    DeclMonster(
        X                   = 50,
        Z                   = -4000,
        Y                   = -28190,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36310,
        Z                   = 0,
        Y                   = -33290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x134,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34580,
        Z                   = 0,
        Y                   = -13200,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x135,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36160,
        Z                   = 0,
        Y                   = 6770,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x136,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35310,
        Z                   = 8000,
        Y                   = -3240,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x137,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37950,
        Z                   = 8000,
        Y                   = 16880,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34960,
        Z                   = 8000,
        Y                   = 36270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x134,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -50,
        TriggerZ            = 4000,
        TriggerY            = 2050,
        TriggerRange        = 1000,
        ActorX              = -50,
        ActorZ              = 5000,
        ActorY              = 2050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 12000,
        TriggerY            = 32060,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 14000,
        ActorY              = 32060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36000,
        TriggerZ            = 0,
        TriggerY            = -4330,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 1000,
        ActorY              = -4330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35990,
        TriggerZ            = 8000,
        TriggerY            = 25790,
        TriggerRange        = 1000,
        ActorX              = 35990,
        ActorZ              = 9000,
        ActorY              = 25790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36000,
        TriggerZ            = 8000,
        TriggerY            = 8000,
        TriggerRange        = 1000,
        ActorX              = 36000,
        ActorZ              = 9000,
        ActorY              = 8000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36000,
        TriggerZ            = 0,
        TriggerY            = 12000,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 1000,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_296",          # 00, 0
        "Function_1_2B6",          # 01, 1
        "Function_2_35C",          # 02, 2
        "Function_3_799",          # 03, 3
        "Function_4_8BF",          # 04, 4
        "Function_5_B5C",          # 05, 5
        "Function_6_C3A",          # 06, 6
        "Function_7_CF6",          # 07, 7
        "Function_8_E0C",          # 08, 8
        "Function_9_E5A",          # 09, 9
        "Function_10_FA7",         # 0A, 10
        "Function_11_10C7",        # 0B, 11
        "Function_12_1144",        # 0C, 12
    )


    def Function_0_296(): pass

    label("Function_0_296")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2AE"),
        (SWITCH_DEFAULT, "loc_2B5"),
    )


    label("loc_2AE")

    Event(0, 5)
    Jump("loc_2B5")

    label("loc_2B5")

    Return()

    # Function_0_296 end

    def Function_1_2B6(): pass

    label("Function_1_2B6")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230086)
    OP_1B(0x0, 0x0, 0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0x17, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0x17, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x19, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x19, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x1A, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x1A, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x1B, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x1B, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x1C, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x1C, 60)

    label("loc_35B")

    Return()

    # Function_1_2B6 end

    def Function_2_35C(): pass

    label("Function_2_35C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-240, 4000, 2620, 0)
    OP_67(-1000, 6950, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(240, 0)
    SetChrPos(0x10F, -1060, 4000, 1910, 90)
    SetChrPos(0xF3, -2810, 4000, 1800, 90)
    SetChrPos(0xF4, -3400, 4000, 600, 90)
    SetChrPos(0xF5, -3660, 4000, 2430, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x2B, 0x0, 0x64)
    OP_6F(0x17, 0)
    OP_70(0x17, 0x3C)
    OP_73(0x17)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xAF\x05\x07\x00。\x02",
    )

    Jump("loc_46D")

    label("loc_46D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5AF, 1)
    OP_A2(0x2881)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x10F,
        (
            "#1444F#6P…………咦………………\x02\x03",

            "（这东西……\x01",
            "  好像在哪儿见过的样子………）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56E")
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x102,
        "#1504F#6P……莉丝小姐？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D9")

    label("loc_56E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C7")
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x107,
        (
            "#064F#6P莉丝姐姐……\x01",
            "你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D9")

    label("loc_5C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_619")
    OP_62(0x10B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x10B,
        "#213F#6P哎呀，你怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D9")

    label("loc_619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_679")
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        (
            "#1164F#6P那个……\x01",
            "请问你发现了什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D9")

    label("loc_679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D9")
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10E,
        (
            "#173F#6P莉丝小姐……\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_6D8")

    label("loc_6D8")

    CloseMessageWindow()

    label("loc_6D9")

    OP_63(0x10F)
    Sleep(100)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        (
            "#1446F#11P……总觉得，\x01",
            "这把剑好像在哪儿见过似的，\x01",
            "会不会是错觉呢。\x02\x03",

            "#1448F难得碰上这么好的一把剑……\x01",
            "我就先用着试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2809)
    OP_28(0x31, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_791")

    label("loc_78D")

    Call(0, 3)

    label("loc_791")

    Jump("loc_798")

    label("loc_794")

    Call(0, 3)

    label("loc_798")

    Return()

    # Function_2_35C end

    def Function_3_799(): pass

    label("Function_3_799")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5AF, 1)"), scpexpr(EXPR_END)), "loc_80D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xAF\x05\x07\x00。\x02",
    )

    Jump("loc_7F2")

    label("loc_7F2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2881)
    Jump("loc_87B")

    label("loc_80D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xAF\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xAF\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_85C")

    label("loc_85C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_87B")

    Jump("loc_8B1")

    label("loc_87E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8B1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_799 end

    def Function_4_8BF(): pass

    label("Function_4_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_993")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2304)
    Sleep(500)
    OP_AA(65282)
    Jump("loc_996")

    label("loc_993")

    TalkBegin(0xFF)

    label("loc_996")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_9C0")

    label("loc_9C0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2B")

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

    Jump("loc_A25")

    label("loc_A25")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A42"),
        (1, "loc_ABD"),
        (2, "loc_AEC"),
        (SWITCH_DEFAULT, "loc_B1B"),
    )


    label("loc_A42")

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
    OP_1D(0xDE)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B28")

    label("loc_ABD")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_AE9")

    label("loc_AE9")

    Jump("loc_B28")

    label("loc_AEC")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_B18")

    label("loc_B18")

    Jump("loc_B28")

    label("loc_B1B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B28")

    label("loc_B28")

    Jump("loc_9D3")

    label("loc_B2B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B58")
    OP_A2(0x258C)
    EventEnd(0x1)
    Jump("loc_B5B")

    label("loc_B58")

    TalkEnd(0xFF)

    label("loc_B5B")

    Return()

    # Function_4_8BF end

    def Function_5_B5C(): pass

    label("Function_5_B5C")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -20, -7700, -66010, 0)
    SetChrPos(0x1, -20, -7700, -66010, 0)
    SetChrPos(0x2, -20, -7700, -66010, 0)
    SetChrPos(0x3, -20, -7700, -66010, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -7700, -66010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_5_B5C end

    def Function_6_C3A(): pass

    label("Function_6_C3A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, -20, -7700, -66010, 180)
    SetChrPos(0x1, -20, -7700, -66010, 180)
    SetChrPos(0x2, -20, -7700, -66010, 180)
    SetChrPos(0x3, -20, -7700, -66010, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -7700, -66010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 8)
    NewScene("ED6_DT21/M7101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_C3A end

    def Function_7_CF6(): pass

    label("Function_7_CF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D13)

    label("loc_D1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D48")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D3C)

    label("loc_D48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D71")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D65)

    label("loc_D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9A")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D8E)

    label("loc_D9A")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC6")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_DC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDD")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_DDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_DF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E0B")

    Return()

    # Function_7_CF6 end

    def Function_8_E0C(): pass

    label("Function_8_E0C")


    def lambda_E12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E12)

    def lambda_E24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E24)

    def lambda_E36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E36)

    def lambda_E48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E48)
    Sleep(1000)
    Return()

    # Function_8_E0C end

    def Function_9_E5A(): pass

    label("Function_9_E5A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x1E)
    OP_73(0x19)
    OP_6F(0x19, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)

    AnonymousTalk(    #14
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×５０\x01",
            "\x07\x02#57I水之耀晶片×５０\x01",
            "\x07\x02#58I火之耀晶片×５０\x01",
            "\x07\x02#59I风之耀晶片×５０\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2898)
    Jump("loc_F95")

    label("loc_F7B")


    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F95")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_E5A end

    def Function_10_FA7(): pass

    label("Function_10_FA7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1019")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_FFE")

    label("loc_FFE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2899)
    Jump("loc_1085")

    label("loc_1019")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1066")

    label("loc_1066")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_1085")

    Jump("loc_10B9")

    label("loc_1088")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_FA7 end

    def Function_11_10C7(): pass

    label("Function_11_10C7")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1118")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x1E)
    OP_73(0x1B)
    OP_6F(0x1B, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x289A)
    Jump("loc_1132")

    label("loc_1118")


    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1132")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_10C7 end

    def Function_12_1144(): pass

    label("Function_12_1144")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1225")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x260, 1)"), scpexpr(EXPR_END)), "loc_11B6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x60\x02\x07\x00。\x02",
    )

    Jump("loc_119B")

    label("loc_119B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AC)
    Jump("loc_1222")

    label("loc_11B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\x60\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x60\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1203")

    label("loc_1203")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_1222")

    Jump("loc_1256")

    label("loc_1225")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1256")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1144 end

    SaveToFile()

Try(main)
