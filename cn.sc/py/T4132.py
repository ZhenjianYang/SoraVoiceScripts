from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4132   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '福立兹',                               # 9
        '阿加特',                               # 10
        '雪拉扎德',                             # 11
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
    )

    DeclNpc(
        X                   = 6940,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 166,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 6100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 6100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 7060,
        TriggerZ            = 0,
        TriggerY            = 1700,
        TriggerRange        = 800,
        ActorX              = 6940,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1BE",          # 02, 2
        "Function_3_1C3",          # 03, 3
        "Function_4_6E6",          # 04, 4
        "Function_5_733",          # 05, 5
        "Function_6_77E",          # 06, 6
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_178")
    Jump("loc_197")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_192")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_197")

    label("loc_192")

    ClearChrFlags(0xA, 0x80)

    label("loc_197")

    Return()

    # Function_0_16A end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B4")
    OP_B1("t4132_y")
    Jump("loc_1BD")

    label("loc_1B4")

    OP_B1("t4132_n")

    label("loc_1BD")

    Return()

    # Function_1_198 end

    def Function_2_1BE(): pass

    label("Function_2_1BE")

    Call(0, 3)
    Return()

    # Function_2_1BE end

    def Function_3_1C3(): pass

    label("Function_3_1C3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D6")
    Jump("loc_201")

    label("loc_1D6")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    OP_A9(0xCC)
    TalkEnd(0x8)
    Return()

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201")
    TalkEnd(0x8)
    Return()

    label("loc_201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C0")

    ChrTalk(    #0
        0x8,
        (
            "多亏了女王陛下，\x01",
            "营业才能继续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "虽然没有导力器了，\x01",
            "虽然我们一直在努力\x01",
            "保持一如既往的服务水准……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "可只有暖气和照明\x01",
            "确实什么也做不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "希望导力器能够\x01",
            "赶紧恢复……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_34A")

    ChrTalk(    #4
        0x8,
        "艾丝蒂尔小姐，您要出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "下次来格兰赛尔城时\x01",
            "也请您能光顾我们这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "我们全体工作人员\x01",
            "都真心等候着我们的再会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_45B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 5)), scpexpr(EXPR_END)), "loc_3AB")

    ChrTalk(    #7
        0x8,
        (
            "玲小姐就是昨天和您\x01",
            "一起住宿的那位小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "如果我看到她\x01",
            "会联络协会的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458")

    label("loc_3AB")


    ChrTalk(    #9
        0x101,
        (
            "#1011F福立兹先生，\x01",
            "你没看到玲吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "……玲小姐就是昨天和您\x01",
            "一起住宿的那位小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "不，她没\x01",
            "来过这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1015F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "如果我看到她\x01",
            "会联络协会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1665)

    label("loc_458")

    Jump("loc_6E2")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(    #14
        0x8,
        (
            "出门的客人都\x01",
            "快要回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "哈哈，工作的时候一天\x01",
            "很快就过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_591")

    ChrTalk(    #16
        0x8,
        (
            "关于恐吓信，\x01",
            "因为内容太过模糊，\x01",
            "我就让自己不要太介意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "现在游击士协会也在调查，\x01",
            "我还是感觉很放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "看来我原先在心底里\x01",
            "还是有点不安的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "如果有什么我们能帮忙的，\x01",
            "我们一定尽心竭力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A7")

    label("loc_591")


    ChrTalk(    #20
        0x8,
        "呼，真没办法……\x02",
    )

    CloseMessageWindow()

    label("loc_5A7")

    Jump("loc_6E2")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_6E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678")

    ChrTalk(    #21
        0x101,
        "#1001F福立兹先生，你好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "哎呀，这不是艾丝蒂尔小姐吗……\x01",
            "诞辰庆典之后就没见了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "今天是来工作的吗？\x01",
            "请随意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F（咦……？）\x02\x03",

            "(是错觉吗？\x01",
            "　他表情好像有点僵……)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1644)
    Jump("loc_6E2")

    label("loc_678")


    ChrTalk(    #25
        0x8,
        (
            "据说互不侵犯条约的签字仪式\x01",
            "快到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "最近有很多从外国\x01",
            "来的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "哈哈，看来要忙碌起来了……\x02",
    )

    CloseMessageWindow()

    label("loc_6E2")

    TalkEnd(0x8)
    Return()

    # Function_3_1C3 end

    def Function_4_6E6(): pass

    label("Function_4_6E6")

    TalkBegin(0xFE)

    ChrTalk(    #28
        0xFE,
        (
            "#050F艾丝蒂尔，你在干吗？\x02\x03",

            "这里是我负责的吧。\x01",
            "你赶快去其他地方。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_6E6 end

    def Function_5_733(): pass

    label("Function_5_733")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "#020F艾丝蒂尔，怎么了？\x02\x03",

            "宾馆是我负责的啊。\x01",
            "你赶快去其他地方。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_733 end

    def Function_6_77E(): pass

    label("Function_6_77E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #30
        (
            "\x07\x05　　　　　　　事务室\x01",
            "※无关人员请勿入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_77E end

    SaveToFile()

Try(main)
