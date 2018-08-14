from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7104   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7104.x',
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
        'ED6_DT29/CH14460 ._CH',             # 00
        'ED6_DT29/CH14461 ._CH',             # 01
        'ED6_DT29/CH14910 ._CH',             # 02
        'ED6_DT29/CH14911 ._CH',             # 03
        'ED6_DT29/CH14920 ._CH',             # 04
        'ED6_DT29/CH14921 ._CH',             # 05
        'ED6_DT29/CH14930 ._CH',             # 06
        'ED6_DT29/CH14931 ._CH',             # 07
        'ED6_DT29/CH15040 ._CH',             # 08
        'ED6_DT29/CH15040 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14460P._CP',             # 00
        'ED6_DT29/CH14461P._CP',             # 01
        'ED6_DT29/CH14910P._CP',             # 02
        'ED6_DT29/CH14911P._CP',             # 03
        'ED6_DT29/CH14920P._CP',             # 04
        'ED6_DT29/CH14921P._CP',             # 05
        'ED6_DT29/CH14930P._CP',             # 06
        'ED6_DT29/CH14931P._CP',             # 07
        'ED6_DT29/CH15040P._CP',             # 08
        'ED6_DT29/CH15040P._CP',             # 09
    )

    DeclMonster(
        X                   = -150,
        Z                   = -4000,
        Y                   = -28070,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36030,
        Z                   = 0,
        Y                   = -33160,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35860,
        Z                   = 0,
        Y                   = -12590,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35750,
        Z                   = 0,
        Y                   = 7680,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36710,
        Z                   = 8000,
        Y                   = -3330,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36110,
        Z                   = 8000,
        Y                   = 17240,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36110,
        Z                   = 8000,
        Y                   = 37800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
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
        TriggerY            = 32000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 14000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36050,
        TriggerZ            = 0,
        TriggerY            = -4240,
        TriggerRange        = 1000,
        ActorX              = -36050,
        ActorZ              = 1000,
        ActorY              = -4240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36000,
        TriggerZ            = 8000,
        TriggerY            = 25870,
        TriggerRange        = 1000,
        ActorX              = 36000,
        ActorZ              = 9000,
        ActorY              = 25870,
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
        "Function_2_372",          # 02, 2
        "Function_3_82C",          # 03, 3
        "Function_4_952",          # 04, 4
        "Function_5_BEF",          # 05, 5
        "Function_6_CCD",          # 06, 6
        "Function_7_D89",          # 07, 7
        "Function_8_E9F",          # 08, 8
        "Function_9_EED",          # 09, 9
        "Function_10_1013",        # 0A, 10
        "Function_11_1162",        # 0B, 11
        "Function_12_1282",        # 0C, 12
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

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230087)
    OP_1B(0x0, 0x0, 0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0x17, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0x17, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x19, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x19, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x1A, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x1A, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x1B, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x1B, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x1C, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x1C, 60)

    label("loc_35B")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B6 end

    def Function_2_372(): pass

    label("Function_2_372")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_820")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-240, 4000, 2620, 0)
    OP_67(-1000, 6950, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(240, 0)
    SetChrPos(0x109, -1060, 4000, 1910, 90)
    SetChrPos(0xEF, -2810, 4000, 1800, 90)
    SetChrPos(0xF0, -3400, 4000, 600, 90)
    SetChrPos(0xF1, -3660, 4000, 2430, 90)
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
        "\x07\x00得到了\x1F\x55\x05\x07\x00。\x02",
    )

    Jump("loc_483")

    label("loc_483")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x555, 1)
    OP_A2(0x2880)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x109,
        (
            "#1079F#6P……什么……！？\x02\x03",

            "#1063F（……这、这是………）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57A")
    OP_A2(0x0)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x107,
        (
            "#064F#6P凯文哥哥……\x01",
            "你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E9")

    label("loc_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    OP_A2(0x3)
    OP_62(0x10B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x10B,
        "#213F#6P哎呀，你怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E9")

    label("loc_5CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_623")
    OP_A2(0x4)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x102,
        "#1504F#6P……凯文先生？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E9")

    label("loc_623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_686")
    OP_A2(0x5)
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
    Jump("loc_6E9")

    label("loc_686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E9")
    OP_A2(0x1)
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10E,
        (
            "#173F#6P凯文神父……\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_6E8")

    label("loc_6E8")

    CloseMessageWindow()

    label("loc_6E9")

    OP_63(0x109)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78C")

    ChrTalk(    #7
        0x109,
        (
            "#1075F#11P没什么……\x01",
            "只是发现了一把很漂亮的弩枪，\x01",
            "看得入神罢了。\x02\x03",

            "#1840F难得这么好的机会……\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_78C")


    ChrTalk(    #8
        0x109,
        (
            "#1075F#11P没什么……\x01",
            "只是发现了一把很漂亮的弩枪，\x01",
            "看得入神罢了。\x02\x03",

            "#1840F难得这么好的机会……\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    OP_A2(0x2806)
    OP_28(0x30, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_824")

    label("loc_820")

    Call(0, 3)

    label("loc_824")

    Jump("loc_82B")

    label("loc_827")

    Call(0, 3)

    label("loc_82B")

    Return()

    # Function_2_372 end

    def Function_3_82C(): pass

    label("Function_3_82C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x555, 1)"), scpexpr(EXPR_END)), "loc_8A0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x55\x05\x07\x00。\x02",
    )

    Jump("loc_885")

    label("loc_885")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2880)
    Jump("loc_90E")

    label("loc_8A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x55\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x55\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8EF")

    label("loc_8EF")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_90E")

    Jump("loc_944")

    label("loc_911")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_944")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_82C end

    def Function_4_952(): pass

    label("Function_4_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A26")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2048)
    Sleep(500)
    OP_AA(65282)
    Jump("loc_A29")

    label("loc_A26")

    TalkBegin(0xFF)

    label("loc_A29")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A53")

    label("loc_A53")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBE")

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

    Jump("loc_AB8")

    label("loc_AB8")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AD5"),
        (1, "loc_B50"),
        (2, "loc_B7F"),
        (SWITCH_DEFAULT, "loc_BAE"),
    )


    label("loc_AD5")

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
    Jump("loc_BBB")

    label("loc_B50")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_B7C")

    label("loc_B7C")

    Jump("loc_BBB")

    label("loc_B7F")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_BAB")

    label("loc_BAB")

    Jump("loc_BBB")

    label("loc_BAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBB")

    label("loc_BBB")

    Jump("loc_A66")

    label("loc_BBE")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEB")
    OP_A2(0x258B)
    EventEnd(0x1)
    Jump("loc_BEE")

    label("loc_BEB")

    TalkEnd(0xFF)

    label("loc_BEE")

    Return()

    # Function_4_952 end

    def Function_5_BEF(): pass

    label("Function_5_BEF")

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
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_5_BEF end

    def Function_6_CCD(): pass

    label("Function_6_CCD")

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
    NewScene("ED6_DT21/M7102   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_CCD end

    def Function_7_D89(): pass

    label("Function_7_D89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DA6)

    label("loc_DB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DCF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DCF)

    label("loc_DDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DF8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DF8)

    label("loc_E04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E21():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E21)

    label("loc_E2D")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E59")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E70")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E70")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E87")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E9E")

    Return()

    # Function_7_D89 end

    def Function_8_E9F(): pass

    label("Function_8_E9F")


    def lambda_EA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EA5)

    def lambda_EB7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EB7)

    def lambda_EC9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EC9)

    def lambda_EDB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EDB)
    Sleep(1000)
    Return()

    # Function_8_E9F end

    def Function_9_EED(): pass

    label("Function_9_EED")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_F61")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_F46")

    label("loc_F46")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A8)
    Jump("loc_FCF")

    label("loc_F61")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_FB0")

    label("loc_FB0")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_FCF")

    Jump("loc_1005")

    label("loc_FD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1005")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_EED end

    def Function_10_1013(): pass

    label("Function_10_1013")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_6F(0x1A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)

    AnonymousTalk(    #18
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×５０\x01",
            "\x07\x02#60I空之耀晶片×５０\x01",
            "\x07\x02#61I幻之耀晶片×５０\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A9)
    Jump("loc_1150")

    label("loc_1136")


    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1150")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1013 end

    def Function_11_1162(): pass

    label("Function_11_1162")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1243")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x69, 1)"), scpexpr(EXPR_END)), "loc_11D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x69\x00\x07\x00。\x02",
    )

    Jump("loc_11B9")

    label("loc_11B9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AA)
    Jump("loc_1240")

    label("loc_11D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\x69\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x69\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1221")

    label("loc_1221")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_1240")

    Jump("loc_1274")

    label("loc_1243")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1274")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1162 end

    def Function_12_1282(): pass

    label("Function_12_1282")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1363")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x170, 1)"), scpexpr(EXPR_END)), "loc_12F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\x70\x01\x07\x00。\x02",
    )

    Jump("loc_12D9")

    label("loc_12D9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AE)
    Jump("loc_1360")

    label("loc_12F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\x70\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x70\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1341")

    label("loc_1341")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_1360")

    Jump("loc_1394")

    label("loc_1363")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1394")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1282 end

    SaveToFile()

Try(main)
