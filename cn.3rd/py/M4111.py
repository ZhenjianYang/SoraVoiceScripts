from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4111   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'ED6_DT29/CH14360 ._CH',             # 00
        'ED6_DT29/CH14360 ._CH',             # 01
        'ED6_DT29/CH14690 ._CH',             # 02
        'ED6_DT29/CH14691 ._CH',             # 03
        'ED6_DT29/CH14460 ._CH',             # 04
        'ED6_DT29/CH14461 ._CH',             # 05
        'ED6_DT29/CH14620 ._CH',             # 06
        'ED6_DT29/CH14621 ._CH',             # 07
        'ED6_DT29/CH14630 ._CH',             # 08
        'ED6_DT29/CH14631 ._CH',             # 09
        'ED6_DT29/CH14010 ._CH',             # 0A
        'ED6_DT29/CH14011 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14360P._CP',             # 00
        'ED6_DT29/CH14360P._CP',             # 01
        'ED6_DT29/CH14690P._CP',             # 02
        'ED6_DT29/CH14691P._CP',             # 03
        'ED6_DT29/CH14460P._CP',             # 04
        'ED6_DT29/CH14461P._CP',             # 05
        'ED6_DT29/CH14620P._CP',             # 06
        'ED6_DT29/CH14621P._CP',             # 07
        'ED6_DT29/CH14630P._CP',             # 08
        'ED6_DT29/CH14631P._CP',             # 09
        'ED6_DT29/CH14010P._CP',             # 0A
        'ED6_DT29/CH14011P._CP',             # 0B
    )

    DeclMonster(
        X                   = 54240,
        Z                   = 0,
        Y                   = 4960,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39410,
        Z                   = 0,
        Y                   = -13960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x258,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 42430,
        Z                   = 40,
        Y                   = -41320,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3040,
        Z                   = 0,
        Y                   = -21430,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31660,
        Z                   = -40,
        Y                   = -17490,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -58180,
        Z                   = 0,
        Y                   = -14580,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -34410,
        Y                   = -1000,
        Z                   = -1390,
        Range               = -17390,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xF32,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 9670,
        TriggerZ            = 500,
        TriggerY            = -54320,
        TriggerRange        = 1500,
        ActorX              = 9670,
        ActorZ              = 4000,
        ActorY              = -54320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23880,
        TriggerZ            = 1000,
        TriggerY            = -10260,
        TriggerRange        = 1000,
        ActorX              = 23880,
        ActorZ              = 1000,
        ActorY              = -10260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23E",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_472",          # 03, 3
        "Function_4_125B",         # 04, 4
        "Function_5_19D7",         # 05, 5
        "Function_6_1CFE",         # 06, 6
        "Function_7_1F1D",         # 07, 7
        "Function_8_213A",         # 08, 8
        "Function_9_2535",         # 09, 9
        "Function_10_3503",        # 0A, 10
        "Function_11_3537",        # 0B, 11
        "Function_12_3570",        # 0C, 12
        "Function_13_35A9",        # 0D, 13
        "Function_14_35E2",        # 0E, 14
        "Function_15_37BE",        # 0F, 15
        "Function_16_3880",        # 10, 16
        "Function_17_3967",        # 11, 17
        "Function_18_3A7D",        # 12, 18
        "Function_19_3BA3",        # 13, 19
    )


    def Function_0_23E(): pass

    label("Function_0_23E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_256"),
        (SWITCH_DEFAULT, "loc_25D"),
    )


    label("loc_256")

    Event(0, 16)
    Jump("loc_25D")

    label("loc_25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_273")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_2BF")

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_289")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_2BF")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_2AA")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_2BF")

    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2BF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 2)

    label("loc_2BF")

    Return()

    # Function_0_23E end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x230064)
    OP_1B(0x1, 0x0, 0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2E7")
    OP_71(0x400, 0x0)
    ExitThread()
    Jump("loc_2F6")

    label("loc_2E7")

    OP_10(0x1, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x8E, 0x0)

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_314")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331")
    OP_6F(0x2, 0)
    Jump("loc_338")

    label("loc_331")

    OP_6F(0x2, 60)

    label("loc_338")

    Return()

    # Function_1_2C0 end

    def Function_2_339(): pass

    label("Function_2_339")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(12000, 6850, -52200, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(225000, 0)
    OP_6E(256, 0)

    def lambda_39C():
        OP_6D(12000, 2800, -52200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_39C)

    def lambda_3B4():
        OP_67(0, 3860, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3B4)

    def lambda_3CC():
        OP_6B(3410, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3CC)

    def lambda_3DC():
        OP_6E(244, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3DC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_400():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_400)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_339 end

    def Function_3_472(): pass

    label("Function_3_472")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9470, 250, -54520, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(224000, 0)
    OP_6E(355, 0)
    SetChrPos(0x109, 11600, 0, -52440, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xEF, 13000, 0, -50910, 225)
    SetChrPos(0xF0, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F")
    SetChrPos(0xF0, 13000, 0, -50910, 225)
    SetChrPos(0xEF, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_54F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593")
    SetChrPos(0xF1, 13000, 0, -50910, 225)
    SetChrPos(0xEF, 14390, 0, -50400, 225)
    SetChrPos(0xF0, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_593")

    SetChrPos(0xEF, 13000, 0, -50910, 225)
    SetChrPos(0xF0, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)

    label("loc_5C6")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        (
            "\x07\x05石碑表面的表盘发出了光芒，\x01",
            "逐渐浮现出了一段文章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W \x01",
            "#40W     前方是镜中秘所。\x01",
            "#500W \x01",
            "#40W      请与剑道之少女\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4B")

    ChrTalk(    #2
        0x109,
        (
            "#1063F#6P『镜中秘所』……\x01",
            "好像是新的领域啊。\x02\x03",

            "#1067F可是，说到『剑道之少女』……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80A")
    OP_A2(0x0)

    ChrTalk(    #3
        0x101,
        (
            "#1007F#6P嗯～尤莉亚小姐\x01",
            "和科洛丝虽然也用剑……\x02\x03",

            "#1006F不过在这种情况下，\x01",
            "最符合的应该是亚妮拉丝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2B")

    label("loc_80A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_894")

    ChrTalk(    #4
        0x103,
        (
            "#1525F#6P是啊，虽然尤莉亚上尉\x01",
            "和公主殿下也用剑……\x02\x03",

            "#1520F但在这种情况下，\x01",
            "最符合的应该是亚妮拉丝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2B")

    label("loc_894")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91E")

    ChrTalk(    #5
        0x10C,
        (
            "#115F#6P嗯，虽然尤莉亚上尉\x01",
            "和王太女殿下也用剑……\x02\x03",

            "#110F但在这种情况下，\x01",
            "最先想到的应该是亚妮拉丝了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2B")

    label("loc_91E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A0")

    ChrTalk(    #6
        0x10E,
        (
            "#176F#6P是啊，\x01",
            "虽然我和殿下也都是用剑的……\x02\x03",

            "#170F但在这种情况下，\x01",
            "最符合的应该是亚妮拉丝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2B")

    label("loc_9A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2B")

    ChrTalk(    #7
        0x105,
        (
            "#1167F#6P是啊，虽然我和\x01",
            "尤莉亚小姐也同样使用剑……\x02\x03",

            "#1160F但在这种情况下，\x01",
            "最符合的应该是亚妮拉丝小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B51")
    OP_A2(0x2B0B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(    #8
        0x10A,
        (
            "#819F#5P唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02\x03",

            "#816F不过，\x01",
            "还是去摸一下表盘试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1001F#6P嗯嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4E")

    label("loc_AD8")


    ChrTalk(    #10
        0x10A,
        (
            "#819F#5P唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02\x03",

            "#816F不过，\x01",
            "还是去摸一下表盘试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4E")

    Jump("loc_C48")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BDD")
    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #11
        0x109,
        (
            "#1075F#5P嗯……\x01",
            "我觉得应该没错了。\x02\x03",

            "#1060F好，那就回据点\x01",
            "把亚妮拉丝叫来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1006F好～\x02",
    )

    CloseMessageWindow()
    Jump("loc_C48")

    label("loc_BDD")

    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #13
        0x109,
        (
            "#1075F#5P嗯……\x01",
            "我觉得应该没错了。\x02\x03",

            "#1060F好，那就回据点\x01",
            "把亚妮拉丝叫来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C48")

    Jump("loc_10C4")

    label("loc_C4B")


    ChrTalk(    #14
        0x109,
        (
            "#1063F#6P『镜中秘所』……\x01",
            "好像是新的领域啊。\x02\x03",

            "#1067F可是，说到『剑道之少女』……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(    #15
        0x109,
        (
            "#1078F#5P虽然也可能是公主殿下或尤莉亚小姐，\x01",
            "不过最接近的\x01",
            "说不定是亚妮拉丝呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D80")

    label("loc_D26")


    ChrTalk(    #16
        0x109,
        (
            "#1078F#5P虽然也可能是公主殿下或尤莉亚小姐，\x01",
            "不过最接近的\x01",
            "说不定是亚妮拉丝呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0A")
    OP_A2(0x2B0B)

    ChrTalk(    #17
        0x10A,
        (
            "#819F#6P唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02\x03",

            "#816F不过，\x01",
            "还是去摸一下表盘试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#6P原来如此……\x02\x03",

            "#1448F这样的话，\x01",
            "我们就回据点把她叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_E71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED6")

    ChrTalk(    #19
        0x102,
        (
            "#1505F#6P确实……\x02\x03",

            "#1500F那么，\x01",
            "我们回据点把亚妮拉丝小姐叫来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F33")

    ChrTalk(    #20
        0x106,
        (
            "#053F#6P确实……\x02\x03",

            "#051F那我们回据点\x01",
            "把亚妮拉丝叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")

    ChrTalk(    #21
        0x107,
        (
            "#560F#6P原、原来如此……\x02\x03",

            "#061F那，我们回据点\x01",
            "把亚妮拉丝姐姐叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_F9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(    #22
        0x108,
        (
            "#573F#6P没错……\x02\x03",

            "#070F那么，\x01",
            "我们快回据点把她叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106A")

    ChrTalk(    #23
        0x104,
        (
            "#1545F#6P呵呵，的确是啊。\x02\x03",

            "#1540F那么，我们快回据点\x01",
            "把亚妮拉丝君叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_106A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #24
        0x10D,
        (
            "#278F#6P原来如此。\x02\x03",

            "#277F那么，\x01",
            "我们回据点把她叫过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1244")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(    #25
        0x110,
        (
            "#260F#6P唔。\x01",
            "是那个扎丝带的姐姐吗。\x02\x03",

            "#261F与其说她是『剑道之少女』，\x01",
            "不如说她是『布娃娃少女』更加贴切。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1203")

    label("loc_1174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1203")

    ChrTalk(    #26
        0x10B,
        (
            "#210F#6P嘿……\x01",
            "是那个扎丝带的女游击士吗。\x02\x03",

            "#211F与其说她是『剑道之少女』，\x01",
            "不如说她是『布娃娃少女』更加贴切。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1203")


    ChrTalk(    #27
        0x109,
        (
            "#1066F#5P哈哈，如果真这样说的话，\x01",
            "的确更容易理解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1244")

    OP_A2(0x2B09)
    OP_28(0x38, 0x1, 0x1)
    OP_28(0x38, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_472 end

    def Function_4_125B(): pass

    label("Function_4_125B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9470, 250, -54520, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(224000, 0)
    OP_6E(355, 0)
    SetChrPos(0x109, 11790, 0, -52090, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F4")
    SetChrPos(0xEF, 10550, 480, -53470, 225)
    SetChrPos(0xF0, 13300, 0, -51640, 225)
    SetChrPos(0xF1, 12430, 0, -50420, 225)
    Jump("loc_1379")

    label("loc_12F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1338")
    SetChrPos(0xF0, 10550, 480, -53470, 225)
    SetChrPos(0xEF, 13300, 0, -51640, 225)
    SetChrPos(0xF1, 12430, 0, -50420, 225)
    Jump("loc_1379")

    label("loc_1338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1379")
    SetChrPos(0xF1, 10550, 480, -53470, 225)
    SetChrPos(0xEF, 13300, 0, -51640, 225)
    SetChrPos(0xF0, 12430, 0, -50420, 225)

    label("loc_1379")

    OP_0D()
    Sleep(300)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #28
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W \x01",
            "#40W     前方是镜中秘所。\x01",
            "#500W \x01",
            "#40W      请与剑道之少女\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1479")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #29
        0x10A,
        "#812F#6P………唔……………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1479")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_148C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_14C2")

    label("loc_14C2")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14E8"),
        (SWITCH_DEFAULT, "loc_19BF"),
    )


    label("loc_14E8")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1560")

    def lambda_154E():
        OP_6D(9320, 10000, -55000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_154E)

    label("loc_1560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C4")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_15B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_15B3)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1609():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1609)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_165F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_165F)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_16B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_16B5)
    Jump("loc_1989")

    label("loc_16C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1828")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1717():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1717)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_176D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_176D)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_17C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17C3)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1819():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1819)
    Jump("loc_1989")

    label("loc_1828")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1989")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_187B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_187B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_18D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18D1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1927():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1927)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_197D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_197D)

    label("loc_1989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")
    Sleep(1500)
    Jump("loc_199E")

    label("loc_1999")

    Sleep(500)

    label("loc_199E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5600   ._SN", 104, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D1")

    label("loc_19BF")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D1")

    label("loc_19D1")

    Jump("loc_148C")

    label("loc_19D4")

    EventEnd(0x0)
    Return()

    # Function_4_125B end

    def Function_5_19D7(): pass

    label("Function_5_19D7")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9320, 0, -55000, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3290, 0)
    OP_6C(224000, 0)
    OP_6E(285, 0)
    SetChrPos(0x0, 10550, 480, -53470, 225)
    SetChrPos(0x1, 11790, 0, -52090, 225)
    SetChrPos(0x2, 13300, 0, -51640, 225)
    SetChrPos(0x3, 12430, 0, -50420, 225)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #30
        "\x07\x05石碑上的表盘散发着光芒。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_1AEF")

    label("loc_1AEF")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B15"),
        (SWITCH_DEFAULT, "loc_1CE6"),
    )


    label("loc_1B15")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1BB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1BB2)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1C08():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C08)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1C5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C5E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1CB4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1CB4)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5600   ._SN", 104, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CF8")

    label("loc_1CE6")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CF8")

    label("loc_1CF8")

    Jump("loc_1AB9")

    label("loc_1CFB")

    EventEnd(0x0)
    Return()

    # Function_5_19D7 end

    def Function_6_1CFE(): pass

    label("Function_6_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_1D0D")
    Call(0, 5)
    Return()

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_END)), "loc_1DEF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D2A")
    Call(0, 4)
    Return()

    label("loc_1D2A")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W \x01",
            "#40W     前方是镜中秘所。\x01",
            "#500W \x01",
            "#40W      请与剑道之少女\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1F1C")

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC0")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W \x01",
            "#40W     前方是镜中秘所。\x01",
            "#500W \x01",
            "#40W      请与剑道之少女\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1F1C")

    label("loc_1EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1ECF")
    Call(0, 3)
    Return()

    label("loc_1ECF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #33
        "\x07\x05琥耀石的石碑上没有刻任何东西。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_1F1C")

    Return()

    # Function_6_1CFE end

    def Function_7_1F1D(): pass

    label("Function_7_1F1D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-25570, 7850, -21590, 0)
    OP_67(0, 9600, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(0, 0)
    OP_6E(298, 0)

    def lambda_1F80():
        OP_6D(-25570, 7850, -2740, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1F80)

    def lambda_1F98():
        OP_67(0, 7220, -10000, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1F98)

    def lambda_1FB0():
        OP_6B(4120, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1FB0)

    def lambda_1FC0():
        OP_6C(0, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1FC0)

    def lambda_1FD0():
        OP_6E(300, 6500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1FD0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    Fade(1000)

    def lambda_1FF9():
        OP_6B(4000, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FF9)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xEE, 0x0)

    def lambda_20F8():
        OP_6D(-25570, 7850, -500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_20F8)

    def lambda_2110():
        OP_6B(3400, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2110)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2B2B)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1F1D end

    def Function_8_213A(): pass

    label("Function_8_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2143")
    Return()

    label("loc_2143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 5)), scpexpr(EXPR_END)), "loc_214B")
    Return()

    label("loc_214B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-24790, 0, -920, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrPos(0xEE, -26850, 0, -2240, 0)
    SetChrPos(0xEF, -25550, 0, -2130, 0)
    SetChrPos(0xF0, -27030, 0, -3900, 0)
    SetChrPos(0xF1, -25370, 0, -3510, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2209")

    ChrTalk(    #34
        0x10F,
        "#1444F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_2209")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2239")

    ChrTalk(    #35
        0x101,
        "#1004F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_2239")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2269")

    ChrTalk(    #36
        0x102,
        "#1504F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_2269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229C")

    ChrTalk(    #37
        0x10B,
        "#213F#11P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_229C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22CB")

    ChrTalk(    #38
        0x110,
        "#264F#11P哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_22CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FE")

    ChrTalk(    #39
        0x107,
        "#065F#11P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_22FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232B")

    ChrTalk(    #40
        0x10A,
        "#814F#11P这……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_232B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235B")

    ChrTalk(    #41
        0x105,
        "#1164F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_235B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238F")

    ChrTalk(    #42
        0x103,
        "#1523F#11P……这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_238F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C0")

    ChrTalk(    #43
        0x106,
        "#052F#11P这东西……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_23C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EF")

    ChrTalk(    #44
        0x108,
        "#073F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_23EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2426")

    ChrTalk(    #45
        0x10E,
        "#173F#11P……这东西………\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_2426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(    #46
        0x104,
        "#1543F#11P噢，这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_245A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2489")

    ChrTalk(    #47
        0x10D,
        "#273F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_2489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B5")

    ChrTalk(    #48
        0x10C,
        "#113F#11P这是……\x02",
    )

    CloseMessageWindow()

    label("loc_24B5")


    ChrTalk(    #49
        0x109,
        (
            "#1065F#6P……看起来，\x01",
            "这里面的确是有什么东西。\x02\x03",

            "#1063F总之……\x01",
            "做好准备后进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B2D)
    OP_28(0x3B, 0x1, 0x8)
    OP_28(0x3B, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_8_213A end

    def Function_9_2535(): pass

    label("Function_9_2535")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0xEE, -26720, 0, 2920, 180)
    SetChrPos(0xEF, -25360, 0, 3530, 180)
    SetChrPos(0xF0, -26760, 0, 4290, 180)
    SetChrPos(0xF1, -25240, 0, 4710, 180)
    OP_6D(-24900, 0, -1950, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    Sleep(1000)

    def lambda_25CD():
        OP_8E(0xFE, 0xFFFF97DC, 0x0, 0xFFFFF1D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_25CD)
    Sleep(100)

    def lambda_25ED():
        OP_8E(0xFE, 0xFFFF9D36, 0x0, 0xFFFFF146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_25ED)
    Sleep(100)

    def lambda_260D():
        OP_8E(0xFE, 0xFFFF9778, 0x0, 0xFFFFF786, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_260D)
    Sleep(100)

    def lambda_262D():
        OP_8E(0xFE, 0xFFFF9EC6, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_262D)
    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2691")

    ChrTalk(    #50
        0x101,
        "#1020F#5P哎……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(    #51
        0x102,
        "#1502F#5P！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_26BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E8")

    ChrTalk(    #52
        0x10B,
        "#216F#5P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_26E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2716")

    ChrTalk(    #53
        0x110,
        "#264F#5P哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2742")

    ChrTalk(    #54
        0x107,
        "#065F#5P啊！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_276F")

    ChrTalk(    #55
        0x10A,
        "#1317F#5P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_276F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(    #56
        0x105,
        "#1164F#5P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_279C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C9")

    ChrTalk(    #57
        0x103,
        "#1523F#5P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_27C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FB")

    ChrTalk(    #58
        0x106,
        "#055F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_27FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2829")

    ChrTalk(    #59
        0x108,
        "#072F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2829")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2855")

    ChrTalk(    #60
        0x10E,
        "#172F#5P什……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2855")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2882")

    ChrTalk(    #61
        0x104,
        "#1542F#5P哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_2882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B2")

    ChrTalk(    #62
        0x10D,
        "#270F#5P……什么。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DD")

    label("loc_28B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28DD")

    ChrTalk(    #63
        0x10C,
        "#112F#5P哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_28DD")


    def lambda_28E3():
        OP_6D(-25140, 0, -5790, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_28E3)

    def lambda_28FB():
        OP_67(0, 8070, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_28FB)

    def lambda_2913():
        OP_6B(3610, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2913)

    def lambda_2923():
        OP_6E(314, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2923)
    OP_43(0xEE, 0x0, 0x0, 0xA)
    Sleep(150)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    Sleep(150)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Fade(500)
    OP_6D(-25380, 0, -6900, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(279, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A0F")

    ChrTalk(    #64
        0x101,
        (
            "#1019F#5P为、为什么……！？\x01",
            "我们明明是一直往前走的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4E")

    ChrTalk(    #65
        0x102,
        "#1502F#5P明明是一直往前走的啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA3")

    ChrTalk(    #66
        0x10B,
        (
            "#216F#5P为、为什么……！？\x01",
            "我们明明是一直往前走的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AED")

    ChrTalk(    #67
        0x110,
        (
            "#1306F#5P哎呀……\x01",
            "我们明明是一直往前走的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2AED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3C")

    ChrTalk(    #68
        0x107,
        (
            "#065F#5P为、为什么……\x01",
            "我们明明是一直往前走的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8C")

    ChrTalk(    #69
        0x10A,
        (
            "#1317F#5P为、为什么……\x01",
            "我们明明是一直往前走的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDA")

    ChrTalk(    #70
        0x105,
        (
            "#1163F#5P为什么……\x01",
            "我们明明是一直往前走的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2BDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(    #71
        0x103,
        (
            "#1522F#5P好可疑呢。\x01",
            "我们明明是一直往前走的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C84")

    ChrTalk(    #72
        0x106,
        (
            "#055F#5P喂喂……\x01",
            "我们明明是一直往前走的啊。\x01",
            "究竟发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCB")

    ChrTalk(    #73
        0x108,
        (
            "#072F#5P唔……\x01",
            "我们明明是一直往前走的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D16")

    ChrTalk(    #74
        0x10E,
        (
            "#178F#5P不可能……\x01",
            "我们明明是一直往前走的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2D16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5E")

    ChrTalk(    #75
        0x104,
        (
            "#1540F#5P哈……\x01",
            "我们明明是一直往前走的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAB")

    ChrTalk(    #76
        0x10D,
        (
            "#270F#5P真是奇怪……\x01",
            "我们明明是一直往前走的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEF")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DEF")

    ChrTalk(    #77
        0x10C,
        (
            "#112F#5P唔……\x01",
            "我们明明是一直往前走的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEF")


    ChrTalk(    #78
        0x109,
        (
            "#1063F#6P……看起来，\x01",
            "想通过这里，要满足一定条件才行。\x02\x03",

            "#1067F…………………………………\x02\x03",

            "#1065F我在想……\x01",
            "也许要把莉丝带过来\x01",
            "我们才能够继续前行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC4")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F2B")

    label("loc_2EC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EEC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F2B")

    label("loc_2EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F14")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F2B")

    label("loc_2F14")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2F2B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F58")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FBF")

    label("loc_2F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F80")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FBF")

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FBF")

    label("loc_2FA8")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2FBF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEC")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3053")

    label("loc_2FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3014")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3053")

    label("loc_3014")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3053")

    label("loc_303C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3053")

    Sleep(1000)

    def lambda_305E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_305E)
    Sleep(100)

    def lambda_3071():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3071)
    Sleep(100)
    OP_8C(0xF1, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B5")

    ChrTalk(    #79
        0x107,
        "#064F#5P哎……？\x02",
    )

    CloseMessageWindow()

    label("loc_30B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30E1")

    ChrTalk(    #80
        0x110,
        "#1305F#5P哦……？\x02",
    )

    CloseMessageWindow()

    label("loc_30E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3116")

    ChrTalk(    #81
        0x101,
        "#1004F#5P为、为什么啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3179")

    label("loc_3116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3146")

    ChrTalk(    #82
        0x10B,
        "#212F#5P什、什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3179")

    label("loc_3146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3179")

    ChrTalk(    #83
        0x10A,
        "#814F#5P为、为什么……？\x02",
    )

    CloseMessageWindow()

    label("loc_3179")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AE")

    ChrTalk(    #84
        0x102,
        "#1504F#5P凯文先生……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E0")

    label("loc_31AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E0")

    ChrTalk(    #85
        0x105,
        "#1163F#5P凯文先生……？\x02",
    )

    CloseMessageWindow()

    label("loc_31E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321F")

    ChrTalk(    #86
        0x103,
        "#1522F#5P……是不是有了什么线索？\x02",
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_321F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3262")

    ChrTalk(    #87
        0x106,
        (
            "#555F#5P喂……\x01",
            "是不是有了什么头绪啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_3262")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A5")

    ChrTalk(    #88
        0x108,
        (
            "#072F#5P嗯……\x01",
            "是不是有了什么头绪啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_32A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32DF")

    ChrTalk(    #89
        0x10E,
        "#178F#5P……你有什么想法吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_32DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_331F")

    ChrTalk(    #90
        0x104,
        (
            "#1540F#5P哦……\x01",
            "难道有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_331F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_335E")

    ChrTalk(    #91
        0x10D,
        (
            "#270F#5P嗯……\x01",
            "难道有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339C")

    label("loc_335E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_339C")

    ChrTalk(    #92
        0x10C,
        (
            "#112F#5P嗯……\x01",
            "难道有了什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3468")

    ChrTalk(    #93
        0x109,
        (
            "#1075F#6P啊，\x01",
            "这是从刚才说的『确信』中推测来的。\x02\x03",

            "#1840F不入虎穴焉得虎子。\x01",
            "我们赶快回据点去，\x01",
            "把莉丝给带过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EC")

    label("loc_3468")


    ChrTalk(    #94
        0x109,
        (
            "#1075F#6P啊，\x01",
            "这是从刚才说的『确信』中推测来的。\x02\x03",

            "#1840F不入虎穴焉得虎子。\x01",
            "我们赶快回据点去，\x01",
            "把莉丝给带过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EC")

    OP_A2(0x2B2C)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_9_2535 end

    def Function_10_3503(): pass

    label("Function_10_3503")

    OP_8E(0xFE, 0xFFFF9606, 0x0, 0xFFFFDE86, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(600)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_3503 end

    def Function_11_3537(): pass

    label("Function_11_3537")

    OP_8E(0xFE, 0xFFFF9BF6, 0x0, 0xFFFFDF1C, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_3537 end

    def Function_12_3570(): pass

    label("Function_12_3570")

    OP_8E(0xFE, 0xFFFF95C0, 0x0, 0xFFFFE3F4, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(700)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_3570 end

    def Function_13_35A9(): pass

    label("Function_13_35A9")

    OP_8E(0xFE, 0xFFFF9CC8, 0x0, 0xFFFFE520, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8C(0xFE, 135, 400)
    Sleep(600)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_35A9 end

    def Function_14_35E2(): pass

    label("Function_14_35E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0xEE, -26720, 0, 2920, 180)
    SetChrPos(0xEF, -25360, 0, 3530, 180)
    SetChrPos(0xF0, -26760, 0, 4290, 180)
    SetChrPos(0xF1, -25240, 0, 4710, 180)
    OP_6D(-24900, 0, -1950, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)

    def lambda_3675():
        OP_8E(0xFE, 0xFFFF97DC, 0x0, 0xFFFFF1D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3675)
    Sleep(100)

    def lambda_3695():
        OP_8E(0xFE, 0xFFFF9D36, 0x0, 0xFFFFF146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3695)
    Sleep(100)

    def lambda_36B5():
        OP_8E(0xFE, 0xFFFF9778, 0x0, 0xFFFFF786, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_36B5)
    Sleep(100)

    def lambda_36D5():
        OP_8E(0xFE, 0xFFFF9EC6, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_36D5)
    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x0)

    def lambda_36FE():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_36FE)
    WaitChrThread(0xEF, 0x0)

    def lambda_3711():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3711)
    WaitChrThread(0xF0, 0x0)

    def lambda_3724():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3724)
    WaitChrThread(0xF1, 0x0)

    def lambda_3737():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3737)
    OP_0D()
    Sleep(500)

    ChrTalk(    #95
        0x109,
        (
            "#1065F#6P根据我的『确信』，\x01",
            "要进到这里面去的话\x01",
            "不带莉丝过来是不行的。\x02\x03",

            "#1063F先回一趟据点吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_35E2 end

    def Function_15_37BE(): pass

    label("Function_15_37BE")

    EventBegin(0x1)
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 16777215, -1)

    def lambda_37DE():
        OP_90(0x0, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_37DE)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3842")
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_387F")

    label("loc_3842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385C")
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_387F")

    label("loc_385C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3873")
    OP_A2(0x2506)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_387F")

    label("loc_3873")

    OP_A2(0x2507)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_387F")

    Return()

    # Function_15_37BE end

    def Function_16_3880(): pass

    label("Function_16_3880")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 12090, 0, -52300, 45)
    SetChrPos(0x1, 12090, 0, -52300, 45)
    SetChrPos(0x2, 12090, 0, -52300, 45)
    SetChrPos(0x3, 12090, 0, -52300, 45)
    OP_69(0x0, 0x0)
    OP_6C(270000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 17)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_3880 end

    def Function_17_3967(): pass

    label("Function_17_3967")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3990")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3984():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3984)

    label("loc_3990")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B9")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_39AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_39AD)

    label("loc_39B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E2")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_39D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_39D6)

    label("loc_39E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A0B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_39FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_39FF)

    label("loc_3A0B")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A37")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3A37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A4E")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3A4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A65")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3A65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A7C")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3A7C")

    Return()

    # Function_17_3967 end

    def Function_18_3A7D(): pass

    label("Function_18_3A7D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B62")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x299, 1)"), scpexpr(EXPR_END)), "loc_3AF1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x00得到了\x1F\x99\x02\x07\x00。\x02",
    )

    Jump("loc_3AD6")

    label("loc_3AD6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9D)
    Jump("loc_3B5F")

    label("loc_3AF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #97
        (
            "宝箱里装有\x1F\x99\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x99\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3B40")

    label("loc_3B40")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_3B5F")

    Jump("loc_3B95")

    label("loc_3B62")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #98
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3B95")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_3A7D end

    def Function_19_3BA3(): pass

    label("Function_19_3BA3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #99
        (
            "\x07\x05北　艾尔贝离宫\x01",
            "西　圣海姆门　　２２４塞尔矩\x01",
            "东　格鲁纳门　　２５６塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_3BA3 end

    SaveToFile()

Try(main)
