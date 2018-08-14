from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7002_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_6BA",          # 03, 3
        "Function_4_1EA0",         # 04, 4
        "Function_5_3352",         # 05, 5
        "Function_6_5A62",         # 06, 6
        "Function_7_7FE3",         # 07, 7
        "Function_8_8A36",         # 08, 8
        "Function_9_AC53",         # 09, 9
        "Function_10_D1E8",        # 0A, 10
        "Function_11_E9D3",        # 0B, 11
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_159")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #0
        0x11,
        (
            "#1446F……………………………………\x02\x03",

            "（………………果然……\x01",
            "  艾丝蒂尔和玲她们两个……）\x02\x03",

            "（那也是……\x01",
            "  羁绊……吗……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6B9")

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_330")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195")
    TalkBegin(0xFE)

    AnonymousTalk(    #1
        "◆无菜单\x02",
    )

    Jump("loc_18C")

    label("loc_18C")

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Jump("loc_325")

    label("loc_195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #2
        0x11,
        (
            "#1445F………………………………\x01",
            "……艾丝蒂尔………\x02\x03",

            "#1446F真是个老好人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1008F哈，哈哈…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_292")

    label("loc_235")


    ChrTalk(    #4
        0x11,
        (
            "#1445F………………………………\x01",
            "……艾丝蒂尔………\x02\x03",

            "#1446F真是个老好人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292")

    OP_A2(0xC)
    Jump("loc_325")

    label("loc_298")


    ChrTalk(    #5
        0x11,
        (
            "#1446F……………………………………\x02\x03",

            "（为什么我\x01",
            "  这么拘泥于此……）\x02\x03",

            "#1445F（我们和『噬身之蛇』\x01",
            "  明明是敌人……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6B9")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 0)), scpexpr(EXPR_END)), "loc_554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC")
    TalkBegin(0xFE)

    ChrTalk(    #6
        0x11,
        (
            "#1446F既然我们已经知道\x01",
            "这个世界的构成方式，\x01",
            "以后应该会遇到其它形式的进攻……\x02\x03",

            "#1440F我会提醒留守据点的各位\x01",
            "让他们注意。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_452")

    label("loc_3EC")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #7
        0x11,
        (
            "#1440F……最好让大家\x01",
            "提高警惕。\x02\x03",

            "#1446F……恩。\x01",
            "我这就去通知他们。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_452")

    OP_A2(0xC)
    Jump("loc_551")

    label("loc_458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB")
    TalkBegin(0xFE)

    ChrTalk(    #8
        0x11,
        (
            "#1446F『影之王』的攻击……\x01",
            "一定会以与之前\x01",
            "不同的方式前来……\x02\x03",

            "#1440F请去叫大家\x01",
            "提高警惕为好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_551")

    label("loc_4EB")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #9
        0x11,
        (
            "#1440F……最好让大家\x01",
            "提高警惕。\x02\x03",

            "#1446F……恩。\x01",
            "我这就去通知他们。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_551")

    Jump("loc_6B9")

    label("loc_554")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0x109,
        (
            "#1064F啊，莉丝……\x02\x03",

            "#1840F怎么样，\x01",
            "和大家相处的如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#1448F……嗯，没问题。\x02\x03",

            "在凯文睡觉的时候，\x01",
            "我们相处得很好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1061F哈哈，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#1443F凯文才是，记得要守约定。\x02\x03",

            "#1446F如果违背约定，\x01",
            "就给我一个礼拜别吃饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1068F哇，这可真严厉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "#1442F呵呵…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2650)
    TalkEnd(0xFE)

    label("loc_6B9")

    Return()

    # Function_2_AC end

    def Function_3_6BA(): pass

    label("Function_3_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 3)), scpexpr(EXPR_END)), "loc_8A1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78D")

    ChrTalk(    #16
        0x1E,
        (
            "#1000F说起来，\x01",
            "我家院子里也有个小水塘呢。\x02\x03",

            "#1012F记得约修亚以前经常露出\x01",
            "一副愁眉不展的样子坐在水塘边上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x110,
        "#1300F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_845")

    label("loc_78D")


    ChrTalk(    #18
        0x1E,
        (
            "#1000F说起来，\x01",
            "我家院子里也有个小水塘呢。\x02\x03",

            "#1012F记得约修亚以前经常露出\x01",
            "一副愁眉不展的样子坐在水塘边上。\x02\x03",

            "#1016F如果……什么时候\x01",
            "也能和玲那样坐在一起就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_845")

    OP_A2(0x8)
    Jump("loc_896")

    label("loc_84B")


    ChrTalk(    #19
        0x1E,
        (
            "#1012F呼…………\x02\x03",

            "像这样平静的感觉\x01",
            "已经很久都没有了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_896")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_1E9F")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_D9A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_946")
    Jump("loc_988")

    label("loc_946")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_962")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_988")

    label("loc_962")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_988")

    label("loc_97E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_988")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #20
        0x1E,
        (
            "#1012F呼……哎呀哎呀。\x02\x03",

            "#1006F约修亚真是的，\x01",
            "别人安慰你却不领情。\x02\x03",

            "难得姐姐想要\x01",
            "对你温柔一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1513F哈哈……\x01",
            "十分感谢你的心意，\x01",
            "不过真的不需要。\x02\x03",

            "#1501F倒不如说……\x01",
            "这次应该感谢『影之王』才对。\x02\x03",

            "给了我一个将那时\x01",
            "没能传达的话说出口的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1E,
        (
            "#1016F啊哈哈……\x01",
            "就和我与妈妈相会时\x01",
            "是一样的对吧。\x02\x03",

            "#1017F………嗯………………\x02\x03",

            "#1012F如果……\x01",
            "莱维也能像这样\x01",
            "和卡琳姐姐温馨地在一起就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#1513F嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_D94")

    label("loc_B9E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #24
        0x1E,
        (
            "#1012F呼……哎呀哎呀。\x02\x03",

            "#1006F约修亚真是的，\x01",
            "别人安慰你却不领情。\x02\x03",

            "难得姐姐想要\x01",
            "对你温柔一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x16,
        (
            "#1513F哈哈……\x01",
            "十分感谢你的心意，\x01",
            "不过真的不需要。\x02\x03",

            "#1501F倒不如说……\x01",
            "这次应该感谢『影之王』才对。\x02\x03",

            "给了我一个将那时\x01",
            "没能传达的话说出口的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1E,
        (
            "#1016F啊哈哈……\x01",
            "就和我与妈妈相会时\x01",
            "是一样的对吧。\x02\x03",

            "#1017F………嗯………………\x02\x03",

            "#1012F如果……\x01",
            "莱维也能像这样\x01",
            "和卡琳姐姐温馨地在一起就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x16,
        "#1513F嗯……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_D94")

    OP_A2(0x264B)
    Jump("loc_1E9F")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_179B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_END)), "loc_1045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB7")
    Call(5, 11)
    Jump("loc_1042")

    label("loc_DB7")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F74")

    ChrTalk(    #28
        0x1E,
        "#1010F……终于要面对了呢。\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1E)
    ClearChrFlags(0x1E, 0x10)
    TurnDirection(0x1E, 0x102, 0)
    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E84")
    Jump("loc_EC6")

    label("loc_E84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA0")
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC6")

    label("loc_EA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBC")
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC6")

    label("loc_EBC")

    OP_51(0x1E, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC6")

    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1E, 0x10)
    Sleep(500)

    ChrTalk(    #29
        0x1E,
        (
            "#1006F喂，约修亚，\x01",
            "你不是有必须要做的事吗？\x02\x03",

            "#1018F那就大胆去做呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1501F……嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0)
    Jump("loc_103A")

    label("loc_F74")


    ChrTalk(    #31
        0x1E,
        "#1010F……终于要面对了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x1E, 2)
    Sleep(500)

    ChrTalk(    #32
        0x1E,
        (
            "#1006F喂，约修亚，\x01",
            "你不是有必须要做的事吗？\x02\x03",

            "#1018F那就大胆去做呀！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x16, 1)
    Sleep(200)

    ChrTalk(    #33
        0x16,
        "#1501F……嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0)
    SetChrSubChip(0x16, 0)

    label("loc_103A")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1042")

    Jump("loc_1798")

    label("loc_1045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1550")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141C")
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_1135")

    label("loc_10F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_110F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1135")

    label("loc_110F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1135")

    label("loc_112B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1135")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #34
        0x102,
        (
            "#1504F……艾丝蒂尔，\x01",
            "难道你在一个人练习棒术？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1E,
        "#1000F嗯，是每天的功课嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1500F对不起，\x01",
            "现在没办法陪你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 5)), scpexpr(EXPR_END)), "loc_134D")

    ChrTalk(    #37
        0x1E,
        (
            "#1001F哈哈，没关系没关系。\x02\x03",

            "#1017F反正在这里对时间的感觉\x01",
            "并不是很敏感……\x02\x03",

            "#1017F怎么说呢，\x01",
            "有点抑制不住兴奋的感觉……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1312")

    ChrTalk(    #38
        0x104,
        (
            "#1542F……太见外了，艾丝蒂尔君。\x02\x03",

            "#1541F这种时候就该和\x01",
            "我这位哥哥交流下嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1E,
        "#1022F……你就算了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_1312")


    ChrTalk(    #40
        0x102,
        (
            "#1500F虽然这样也不错，\x01",
            "不过也要好好休息啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134A")

    Jump("loc_1419")

    label("loc_134D")


    ChrTalk(    #41
        0x1E,
        (
            "#1001F哈哈，没关系没关系。\x02\x03",

            "#1000F反正在这里对时间的感觉\x01",
            "并不是很清楚……\x02\x03",

            "#1007F为了追上爸爸，\x01",
            "必须要不断\x01",
            "脚踏实地的努力才行。\x02\x03",

            "#1006F好，稍微休息一下。\x01",
            "然后再来一次吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    Jump("loc_153A")

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 3)), scpexpr(EXPR_END)), "loc_147B")

    ChrTalk(    #42
        0x16,
        (
            "#1501F……已经很久\x01",
            "没有和父亲战斗了。\x02\x03",

            "#1513F大概……有六年了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C2")

    label("loc_147B")


    ChrTalk(    #43
        0x16,
        (
            "#1503F父亲吗……\x02\x03",

            "#1514F我也仅仅和他\x01",
            "战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C2")


    ChrTalk(    #44
        0x1E,
        "#1017F……啊，是那时候吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x16,
        (
            "#1501F…………嗯。\x02\x03",

            "#1509F呵呵，现在想起来\x01",
            "那时真是太乱来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153A")

    OP_A2(0x8)
    OP_A2(0x2)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_1798")

    label("loc_1550")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1660")
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15F6")
    Jump("loc_1638")

    label("loc_15F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1612")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1638")

    label("loc_1612")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_162E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1638")

    label("loc_162E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1638")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jump("loc_1665")

    label("loc_1660")

    SetChrSubChip(0xFE, 0)

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 5)), scpexpr(EXPR_END)), "loc_1716")

    ChrTalk(    #46
        0x1E,
        (
            "#1007F我大概也是第一次\x01",
            "和认真的老爸战斗。\x02\x03",

            "#1002F……为了追上他，\x01",
            "必须要不断\x01",
            "脚踏实地的努力才行。\x02\x03",

            "#1006F好，稍微休息一下。\x01",
            "然后再来一次吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178B")

    label("loc_1716")


    ChrTalk(    #47
        0x1E,
        (
            "#1002F……为了追上他，\x01",
            "必须要不断\x01",
            "脚踏实地的努力才行。\x02\x03",

            "#1006F好，稍微休息一下。\x01",
            "然后再来一次吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178B")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1798")

    Jump("loc_1E9F")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A4")
    TalkBegin(0xFE)

    ChrTalk(    #48
        0x1E,
        (
            "#1003F没想到渡鸦帮那些家伙\x01",
            "和菲利普先生\x01",
            "都被利用了……\x02\x03",

            "就连王立学院也……\x02\x03",

            "#1007F唉，\x01",
            "真是有点过分啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1860")

    ChrTalk(    #49
        0x105,
        "#1163F艾丝蒂尔…………\x02",
    )

    CloseMessageWindow()

    label("loc_1860")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(    #50
        0x102,
        "#1503F因为是充满回忆的场所吧……\x02",
    )

    CloseMessageWindow()

    label("loc_189B")

    OP_A2(0x8)
    TalkEnd(0xFE)
    Jump("loc_190F")

    label("loc_18A4")

    TalkBegin(0xFE)

    ChrTalk(    #51
        0x1E,
        (
            "#1010F……大概是故意\x01",
            "使用我们抱有\x01",
            "很深感情的场所……\x02\x03",

            "#1007F唉，\x01",
            "真是有点过分啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_190F")

    Jump("loc_1E9F")

    label("loc_1912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B75")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    ChrTalk(    #52
        0x1E,
        (
            "#1004F啊，凯文先生。\x02\x03",

            "#1002F……身体还好吧？\x01",
            "你可不要硬撑呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1066F哈哈，不要紧了。\x02\x03",

            "#1060F对不起，\x01",
            "连个招呼都没打就倒下了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A72")
    TurnDirection(0x10F, 0x109, 0)

    ChrTalk(    #54
        0x10F,
        (
            "#1446F…………是啊。#1157W \x01",
            "#20W那时大家都呆掉了。\x02\x03",

            "#1801F明明是守护骑士，\x01",
            "凯文也太软弱了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF5")

    label("loc_1A72")

    OP_4A(0x11, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x11, 0x109, 0)

    ChrTalk(    #55
        0x11,
        (
            "#1446F…………是啊。#1157W \x01",
            "#20W那时大家都呆掉了。\x02\x03",

            "#1801F明明是守护骑士，\x01",
            "凯文也太软弱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF5")

    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x1E,
        (
            "#1016F啊、啊哈哈…………\x01",
            "（其实莉丝小姐\x01",
            "  是最慌张的呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x11, 255)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x264A)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_1E9F")

    label("loc_1B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 6)), scpexpr(EXPR_END)), "loc_1BF8")
    TalkBegin(0xFE)

    ChrTalk(    #57
        0x1E,
        (
            "#1000F凯文先生，\x01",
            "可不要硬撑呀。\x02\x03",

            "#1015F虽不清楚详细情况……\x02\x03",

            "#1002F不过大家\x01",
            "都很担心呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1E9F")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 2)), scpexpr(EXPR_END)), "loc_1E9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D3C")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #58
        0x1E,
        (
            "#1011F……啊，约修亚。\x02\x03",

            "#1003F那个，\x01",
            "有件事情我有点在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1503F…………是吗。\x02\x03",

            "#1505F艾丝蒂尔也发现了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x1E,
        (
            "#1026F啊，嗯。\x02\x03",

            "那么，\x01",
            "所谓『试炼』果然是……\x02",
        )
    )

    Jump("loc_1CF3")

    label("loc_1CF3")

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1505F……是啊。\x02\x03",

            "#1503F看来我也有必要\x01",
            "做好准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1D3C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x11, 255)
    OP_4A(0x16, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB1")

    ChrTalk(    #62
        0x11,
        (
            "#1443F………………嗯。\x02\x03",

            "『影之国』最强的守护者……\x01",
            "他是这么自称的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB1")

    TurnDirection(0x1E, 0x16, 400)

    ChrTalk(    #63
        0x1E,
        (
            "#1011F……那个，约修亚。\x02\x03",

            "#1003F我也遇到过他一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        (
            "#1505F嗯，我知道。\x02\x03",

            "#1503F『试炼』……\x01",
            "看来我也有必要做好准备。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_1E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(    #65
        0x110,
        "#1300F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1E91")

    OP_4B(0x11, 255)
    OP_4B(0x16, 255)
    OP_A2(0x2636)
    TalkEnd(0xFE)

    label("loc_1E9F")

    Return()

    # Function_3_6BA end

    def Function_4_1EA0(): pass

    label("Function_4_1EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 3)), scpexpr(EXPR_END)), "loc_1EE9")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #66
        0x16,
        "#1513F……………………………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_3351")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_23C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CD")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F8E")
    Jump("loc_1FD0")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FAA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FD0")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FC6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FD0")

    label("loc_1FC6")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FD0")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #67
        0x101,
        (
            "#1012F呼……哎呀哎呀。\x02\x03",

            "#1006F约修亚真是的，\x01",
            "别人安慰你却不领情。\x02\x03",

            "难得姐姐想要\x01",
            "对你温柔一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1513F哈哈……\x01",
            "十分感谢你的心意，\x01",
            "不过真的不需要。\x02\x03",

            "#1501F倒不如说……\x01",
            "这次应该感谢『影之王』才对。\x02\x03",

            "给了我一个将那时\x01",
            "没能传达的话说出口的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "就和我与妈妈相会时\x01",
            "是一样的对吧。\x02\x03",

            "#1017F………嗯………………\x02\x03",

            "#1012F如果……\x01",
            "莱维也能像这样\x01",
            "和卡琳姐姐温馨地在一起就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_23C3")

    label("loc_21CD")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #70
        0x1E,
        (
            "#1012F呼……哎呀哎呀。\x02\x03",

            "#1006F约修亚真是的，\x01",
            "别人安慰你却不领情。\x02\x03",

            "难得姐姐想要\x01",
            "对你温柔一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x16,
        (
            "#1513F哈哈……\x01",
            "十分感谢你的心意，\x01",
            "不过真的不需要。\x02\x03",

            "#1501F倒不如说……\x01",
            "这次应该感谢『影之王』才对。\x02\x03",

            "给了我一个将那时\x01",
            "没能传达的话说出口的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x1E,
        (
            "#1016F啊哈哈……\x01",
            "就和我与妈妈相会时\x01",
            "是一样的对吧。\x02\x03",

            "#1017F………嗯………………\x02\x03",

            "#1012F如果……\x01",
            "莱维也能像这样\x01",
            "和卡琳姐姐温馨地在一起就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x16,
        "#1513F嗯……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_23C3")

    OP_A2(0x264B)
    Jump("loc_3351")

    label("loc_23C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_2879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_END)), "loc_2558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E6")
    Call(5, 11)
    Jump("loc_2555")

    label("loc_23E6")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2476")
    Jump("loc_24B8")

    label("loc_2476")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2492")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24B8")

    label("loc_2492")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24AE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24B8")

    label("loc_24AE")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24B8")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #74
        0x16,
        (
            "#1505F看来『黑骑士』\x01",
            "是特地指名找我的。\x02\x03",

            "#1500F……我已经做好准备了。\x01",
            "随时可以让我加入同伴。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_2555")

    Jump("loc_2876")

    label("loc_2558")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2665")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25FE")
    Jump("loc_2640")

    label("loc_25FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_261A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2640")

    label("loc_261A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2636")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2640")

    label("loc_2636")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2640")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_2665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 3)), scpexpr(EXPR_END)), "loc_26CC")

    ChrTalk(    #75
        0x16,
        (
            "#1501F……已经很久\x01",
            "没有和父亲战斗了。\x02\x03",

            "#1513F大概……有六年了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_26CC")


    ChrTalk(    #76
        0x16,
        (
            "#1503F父亲吗……\x02\x03",

            "#1514F我也仅仅和他\x01",
            "战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274D")

    ChrTalk(    #77
        0x101,
        "#1017F……啊，是那个时候吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2776")

    label("loc_274D")


    ChrTalk(    #78
        0x1E,
        "#1017F……啊，是那个时候吗。\x02",
    )

    CloseMessageWindow()

    label("loc_2776")


    ChrTalk(    #79
        0x16,
        (
            "#1501F…………嗯。\x02\x03",

            "#1509F呼，现在想起来\x01",
            "那时真是太乱来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x2)
    Jump("loc_2869")

    label("loc_27CE")


    ChrTalk(    #80
        0x16,
        (
            "#1500F因为对手只是个小孩，\x01",
            "父亲已经手下留情了呢。\x02\x03",

            "#1513F……已经六年了。\x02\x03",

            "如果不是因为有这样的机会，\x01",
            "还真是个不想挑战的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2869")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_2876")

    Jump("loc_3351")

    label("loc_2879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_29BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2944")
    TalkBegin(0xFE)

    ChrTalk(    #81
        0x16,
        (
            "#1500F『守护者』的领域……\x01",
            "是从艾尔贝周游道的石碑\x01",
            "进去的吧。\x02\x03",

            "#1503F……那些石碑\x01",
            "原本是以四种属性\x01",
            "守护王都的设施……\x02\x03",

            "它们也被『王』\x01",
            "进行了变化吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    TalkEnd(0xFE)
    Jump("loc_29BB")

    label("loc_2944")

    TalkBegin(0xFE)

    ChrTalk(    #82
        0x16,
        (
            "#1503F……那些石碑\x01",
            "原本是以四种属性\x01",
            "守护王都的设施……\x02\x03",

            "#1505F它们也被『王』\x01",
            "进行了变化吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_29BB")

    Jump("loc_3351")

    label("loc_29BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 6)), scpexpr(EXPR_END)), "loc_2B1F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAB")

    ChrTalk(    #83
        0x16,
        (
            "#1503F解放赛雷斯托小姐，\x01",
            "是为了让我们了解\x01",
            "这个世界的构造……\x02\x03",

            "那么也许会以与至今不同的方式\x01",
            "利用我们的记忆和思念\x01",
            "来设下圈套。\x02\x03",

            "#1502F……『影之王』\x01",
            "会再现利贝尔，\x01",
            "也许一开始就是为了这个。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2B19")

    label("loc_2AAB")


    ChrTalk(    #84
        0x16,
        (
            "#1503F……『影之王』\x01",
            "会再现利贝尔，\x01",
            "也许一开始就是为了『试炼』。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B19")

    TalkEnd(0xFE)
    Jump("loc_3351")

    label("loc_2B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2DB9")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C62")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #85
        0x101,
        (
            "#1011F……啊，约修亚。\x02\x03",

            "#1003F那个，\x01",
            "有件事情我有点在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x16,
        (
            "#1503F…………是吗。\x01",
            "#1505F艾丝蒂尔也发现了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1026F啊，嗯。\x02\x03",

            "那么，\x01",
            "所谓的『试炼』果然是……\x02",
        )
    )

    Jump("loc_2C19")

    label("loc_2C19")

    CloseMessageWindow()

    ChrTalk(    #88
        0x16,
        (
            "#1505F……是啊。\x02\x03",

            "#1503F看来我也有必要\x01",
            "做好准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6A")

    label("loc_2C62")

    OP_4A(0x11, 255)
    OP_4A(0x1E, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCF")

    ChrTalk(    #89
        0x11,
        (
            "#1443F………………嗯。\x02\x03",

            "『影之国』最强的守护者……\x01",
            "他是这么自称的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCF")


    ChrTalk(    #90
        0x1E,
        (
            "#1003F……那个，约修亚。\x02\x03",

            "#1003F我也遇到过他一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x16,
        (
            "#1505F嗯，我知道。\x02\x03",

            "#1503F『试炼』……\x01",
            "看来我也有必要做好准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA3")

    ChrTalk(    #92
        0x110,
        "#1300F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2DA3")

    OP_4B(0x11, 255)
    OP_4B(0x1E, 255)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2636)
    TalkEnd(0xFE)
    Jump("loc_3351")

    label("loc_2DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_30E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF5")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E5E")
    Jump("loc_2EA0")

    label("loc_2E5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E7A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EA0")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E96")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EA0")

    label("loc_2E96")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EA0")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7C")

    ChrTalk(    #93
        0x16,
        (
            "#1503F看来『影之王』\x01",
            "是打算和我们\x01",
            "玩一场游戏了。\x02\x03",

            "#1503F那到底是什么\x01",
            "现在还是不清楚……\x02\x03",

            "#1502F不过和至今忽隐忽现的\x01",
            "『规则』应该有着什么关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2FEA")

    label("loc_2F7C")


    ChrTalk(    #94
        0x16,
        (
            "#1502F『影之王』设置的游戏\x01",
            "应该也有一定的『规则』。\x02\x03",

            "……如果明白了什么，\x01",
            "请马上来告诉我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_30E0")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3004")
    Call(5, 7)
    Jump("loc_30E0")

    label("loc_3004")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3079")

    ChrTalk(    #95
        0x16,
        (
            "#1505F嗯，我被卷进来时\x01",
            "艾丝蒂尔也在旁边。\x02\x03",

            "#1503F她也一起被卷进来的\x01",
            "可能性很高。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_30DD")

    label("loc_3079")


    ChrTalk(    #96
        0x16,
        (
            "#1505F嗯，我被卷进来时\x01",
            "艾丝蒂尔也在旁边。\x02\x03",

            "#1503F她也一起被卷进来的\x01",
            "可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DD")

    TalkEnd(0xFF)

    label("loc_30E0")

    Jump("loc_3351")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 5)), scpexpr(EXPR_END)), "loc_31AD")
    TalkBegin(0xFE)
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #97
        0x16,
        (
            "#1503F虽然不清楚\x01",
            "『敌人』的真实意图……\x02\x03",

            "#1505F因为当时艾丝蒂尔和我在一起，\x01",
            "所以她也被卷进\x01",
            "这个世界的可能性很高。\x02\x03",

            "#1502F……凯文先生，\x01",
            "请让我也来帮忙。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_3351")

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_3351")
    TalkBegin(0xFE)
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #98
        0x16,
        (
            "#1500F……凯文先生。\x02\x03",

            "我已经调查过一遍了，\x01",
            "在这个『据点』里\x01",
            "没有发现什么陷阱。\x02\x03",

            "#1505F虽然也可能存在着\x01",
            "我所不知道的陷阱类型，\x01",
            "不过可以暂时认为这里是安全的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1060F啊，我也调查过，\x01",
            "大概只有这个地方是安全的。\x02\x03",

            "#1067F虽然如此，\x01",
            "只要离开这里一步，\x01",
            "就到处都是无法理解的魔物了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x16,
        (
            "#1505F嗯…………\x02\x03",

            "#1503F我们要避免单独行动，\x01",
            "谨慎行事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2635)
    TalkEnd(0xFE)

    label("loc_3351")

    Return()

    # Function_4_1EA0 end

    def Function_5_3352(): pass

    label("Function_5_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_38E3")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3751")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #101
        0x1C,
        (
            "#1526F…………………………\x02\x03",

            "#1527F……呵………………\x01",
            "差不多该说出真心话了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(    #102
        0x101,
        (
            "#1011F咦，雪拉姐……\x01",
            "…………怎么了？\x02\x03",

            "#1015F那个……\x01",
            "你是不是忘带上塔罗牌了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)
    Jump("loc_35A5")

    label("loc_3478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E8")

    ChrTalk(    #103
        0x102,
        (
            "#1504F那个，雪拉姐姐……\x02\x03",

            "#1500F你把塔罗牌\x01",
            "忘在桌子上了吧……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Sleep(300)
    Jump("loc_35A5")

    label("loc_34E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354F")

    ChrTalk(    #104
        0x10A,
        (
            "#814F……啊，雪拉前辈。\x02\x03",

            "你是不是忘了\x01",
            "带上塔罗牌……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x10A, 400)
    Sleep(300)
    Jump("loc_35A5")

    label("loc_354F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A5")

    ChrTalk(    #105
        0x109,
        (
            "#1066F……哎呀，大姐。\x01",
            "你把卡片忘在桌子上了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    label("loc_35A5")


    ChrTalk(    #106
        0x1C,
        (
            "#1526F……不要紧。\x02\x03",

            "#1536F因为抽中了许久不见的好牌，\x01",
            "所以想就那样放着做个纪念。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3638")

    ChrTalk(    #107
        0x101,
        "#1016F纪、纪念……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36EE")

    label("loc_3638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366C")

    ChrTalk(    #108
        0x102,
        "#1504F是、是这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36EE")

    label("loc_366C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BD")

    ChrTalk(    #109
        0x10A,
        (
            "#814F我说…………\x02\x03",

            "#818F少一张牌可以吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36EE")

    label("loc_36BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36EE")

    ChrTalk(    #110
        0x109,
        "#1064F哈、哈哈…………\x02",
    )

    CloseMessageWindow()

    label("loc_36EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_374B")

    ChrTalk(    #111
        0x104,
        (
            "#1545F呵……这样也好。\x02\x03",

            "#1540F雪拉君也有\x01",
            "自己的思考方式嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374B")

    OP_A2(0x2663)
    Jump("loc_38C6")

    label("loc_3751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3866")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #112
        0x1C,
        (
            "#1526F…………………………\x02\x03",

            "#1527F……呵………………\x01",
            "差不多该说出真心话了吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #113
        0x1C,
        "#1523F…………嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #114
        0x1C,
        (
            "#1520F呵呵，\x01",
            "我也该做好准备了。\x02\x03",

            "#1536F要磨亮才算得上『银闪』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_38C6")

    label("loc_3866")

    TalkBegin(0xFE)

    ChrTalk(    #115
        0x1C,
        (
            "#1526F接下来，我也该做好准备了。\x02\x03",

            "#1536F呵呵……\x01",
            "要磨亮才算得上『银闪』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C6")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_5A61")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_3C6B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_397A")
    Jump("loc_39BC")

    label("loc_397A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3996")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39BC")

    label("loc_3996")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39B2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39BC")

    label("loc_39B2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39BC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7F")

    ChrTalk(    #116
        0x1C,
        (
            "#1526F约修亚出去旅行后\x01",
            "也变得坚强了不少嘛。\x02\x03",

            "#1520F虽然我认为\x01",
            "还有不足的地方……\x02\x03",

            "#1535F不过对我们来说也是一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B64")

    label("loc_3A7F")


    ChrTalk(    #117
        0x1C,
        (
            "#1526F福音设施『紫苑之家』……吗。\x02\x03",

            "……虽然我们局外人\x01",
            "不该这样说三道四……\x02\x03",

            "#1522F……不过还真是有点在意啊。\x02\x03",

            "为什么那种地方\x01",
            "会被再现出来呢…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x109,
        "#1067F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3B64")

    OP_A2(0x9)
    Jump("loc_3C60")

    label("loc_3B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD7")

    ChrTalk(    #119
        0x1C,
        (
            "#1520F约修亚和艾丝蒂尔两个人\x01",
            "都变坚强了呢。\x02\x03",

            "#1521F呵呵，\x01",
            "真期待他们赶快回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C60")

    label("loc_3BD7")


    ChrTalk(    #120
        0x1C,
        (
            "#1522F……虽然我们局外人\x01",
            "不该这样说三道四……\x01",
            "……不过还真是有点在意啊。\x02\x03",

            "#1526F为什么那种地方\x01",
            "会被再现出来………呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C60")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_5A61")

    label("loc_3C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_45BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 4)), scpexpr(EXPR_END)), "loc_3E3F")
    SetChrSubChip(0xFE, 0)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D1E")
    Jump("loc_3D60")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D3A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D60")

    label("loc_3D3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D56")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D60")

    label("loc_3D56")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D60")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #121
        0x1C,
        (
            "#1525F呼………………\x02\x03",

            "#1530F五脏六腑都被浸透了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E01")

    ChrTalk(    #122
        0x101,
        "#1019F这么快就喝上了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E34")

    label("loc_3E01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E34")

    ChrTalk(    #123
        0x102,
        "#1508F这么快就喝上了……\x02",
    )

    CloseMessageWindow()

    label("loc_3E34")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3FF8")

    label("loc_3E3F")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ECF")
    Jump("loc_3F11")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EEB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F11")

    label("loc_3EEB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F07")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F11")

    label("loc_3F07")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F11")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #124
        0x1C,
        (
            "#1526F这次的『守护者』是老师吗……\x02\x03",

            "#1520F我在研修时期\x01",
            "也和他切磋过好几次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1068F唉，真是难为人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1C,
        (
            "#1527F呵呵，和他作对手\x01",
            "的确是个试炼呀。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_3FF8")

    Jump("loc_429A")

    label("loc_3FFB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_408B")
    Jump("loc_40CD")

    label("loc_408B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40A7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40CD")

    label("loc_40A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40C3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40CD")

    label("loc_40C3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40CD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 1)), scpexpr(EXPR_END)), "loc_4184")

    ChrTalk(    #127
        0x1C,
        (
            "#1526F（…………假的露茜奥拉姐姐吗。）\x02\x03",

            "（姐姐的样子\x01",
            "  我总是记在心里……）\x02\x03",

            "#1532F（没感觉到有什么区别……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4255")

    label("loc_4184")


    ChrTalk(    #128
        0x1C,
        "#1526F是吗，姐姐她……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x109,
        "#1067F对了，大姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x1C,
        (
            "#1520F……没关系啦。\x02\x03",

            "如果打算去寻找姐姐的话，\x01",
            "在这半年里早就仔细调查了。\x02\x03",

            "#1521F呵呵，\x01",
            "我已经不是爱撒娇的年龄了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4292")

    ChrTalk(    #131
        0x104,
        "#1542F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_4292")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_429A")

    OP_A2(0x9)
    Jump("loc_45BA")

    label("loc_42A0")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4330")
    Jump("loc_4372")

    label("loc_4330")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_434C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4372")

    label("loc_434C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4368")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4372")

    label("loc_4368")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4372")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 4)), scpexpr(EXPR_END)), "loc_4486")

    ChrTalk(    #132
        0x1C,
        (
            "#1528F啊，\x01",
            "总算是渡过难关了。\x02\x03",

            "#1530F稍微喝点酒，\x01",
            "应该不会遭报应吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_443D")

    ChrTalk(    #133
        0x102,
        (
            "#1508F这……稍微喝点\x01",
            "应该不会啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4483")

    label("loc_443D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4483")

    ChrTalk(    #134
        0x101,
        (
            "#1019F……不过话说回来，\x01",
            "你不是一直在喝吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4483")

    Jump("loc_4512")

    label("loc_4486")


    ChrTalk(    #135
        0x1C,
        (
            "#1527F……回去后，这次的见闻倒是个不错的话题呢。\x02\x03",

            "#1526F最后的领域……\x01",
            "恐怕是最难的试炼。\x02\x03",

            "#1520F鼓起干劲前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4512")

    Jump("loc_45B2")

    label("loc_4515")


    ChrTalk(    #136
        0x1C,
        (
            "#1521F……呵呵，我也不是特意\x01",
            "打算追踪露茜奥拉姐姐的消息。\x02\x03",

            "#1520F有缘的话一定还能相见……\x02\x03",

            "我已经是\x01",
            "利贝尔的游击士了。\x02",
        )
    )

    Jump("loc_45B1")

    label("loc_45B1")

    CloseMessageWindow()

    label("loc_45B2")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_45BA")

    Jump("loc_5A61")

    label("loc_45BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_479A")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4654")
    Jump("loc_4696")

    label("loc_4654")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4670")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4696")

    label("loc_4670")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_468C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4696")

    label("loc_468C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4696")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4735")

    ChrTalk(    #137
        0x1C,
        (
            "#1526F事到如今再慌慌张张的\x01",
            "就什么也办不到。\x02\x03",

            "#1520F要确实地抓住机会。\x01",
            "……不管对手是谁。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_478F")

    label("loc_4735")


    ChrTalk(    #138
        0x1C,
        (
            "#1526F之后的守护者\x01",
            "肯定会更厉害……\x02\x03",

            "#1535F至少准备工作\x01",
            "要做充分一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478F")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_5A61")

    label("loc_479A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_4E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C6")
    Call(5, 10)
    Jump("loc_4927")

    label("loc_47C6")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4856")
    Jump("loc_4898")

    label("loc_4856")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4872")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4898")

    label("loc_4872")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_488E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4898")

    label("loc_488E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4898")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #139
        0x1C,
        (
            "#1525F……原本就觉得\x01",
            "她有点粗神经。\x02\x03",

            "#1534F该说是自我主义呢\x01",
            "还是精力旺盛呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_4927")

    Jump("loc_4BBF")

    label("loc_492A")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49BA")
    Jump("loc_49FC")

    label("loc_49BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49D6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49FC")

    label("loc_49D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49F2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49FC")

    label("loc_49F2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49FC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #140
        0x1C,
        (
            "#1525F……呼，\x01",
            "好像听到了奇怪的事情呢。\x02\x03",

            "#1532F竟然能用意念\x01",
            "来影响世界……\x02\x03",

            "这不就和喝得\x01",
            "烂醉的时候一个样嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B30")

    ChrTalk(    #141
        0x104,
        (
            "#1545F嘻嘻，嘻嘻……\x02\x03",

            "#1546F雪拉君，\x01",
            "我明白你的心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1016F奥利维尔，你脸色很差哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BB7")

    label("loc_4B30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B7D")

    ChrTalk(    #143
        0x102,
        (
            "#1508F这话由雪拉姐姐来说\x01",
            "意外地很有说服力呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB7")

    label("loc_4B7D")


    ChrTalk(    #144
        0x101,
        (
            "#1016F这话由雪拉姐来说\x01",
            "意外地很有说服力呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB7")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_4BBF")

    OP_A2(0x9)
    Jump("loc_4E98")

    label("loc_4BC5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C55")
    Jump("loc_4C97")

    label("loc_4C55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C71")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C97")

    label("loc_4C71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C8D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C97")

    label("loc_4C8D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C97")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D5A")
    Jump("loc_4D9C")

    label("loc_4D5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D76")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D9C")

    label("loc_4D76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D92")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D9C")

    label("loc_4D92")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D9C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #145
        0x1C,
        (
            "#1525F……原本就觉得\x01",
            "她有点粗神经。\x02\x03",

            "#1534F该说是自我主义呢\x01",
            "还是精力旺盛呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4E90")

    label("loc_4E2E")


    ChrTalk(    #146
        0x1C,
        (
            "#1525F……竟然能用意念\x01",
            "来影响世界……\x02\x03",

            "#1532F这不就和喝得\x01",
            "烂醉的时候一个样嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E90")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_4E98")

    Jump("loc_5A61")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 4)), scpexpr(EXPR_END)), "loc_526B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F32")
    Jump("loc_4F74")

    label("loc_4F32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F4E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F74")

    label("loc_4F4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F6A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F74")

    label("loc_4F6A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F74")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5209")
    OP_A2(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50A0")

    ChrTalk(    #147
        0x1C,
        (
            "#1526F……那么。\x02\x03",

            "#1527F出发旅行之后，\x01",
            "你们的进展怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1013F唔…………\x02\x03",

            "#1022F雪、雪拉姐真是的，\x01",
            "怎么突然提起\x01",
            "这种话题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#1514F不过，会遇到这种提问\x01",
            "在某种程度上也可以想像得到……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_513A")

    label("loc_50A0")


    ChrTalk(    #150
        0x1C,
        (
            "#1526F……那么。\x02\x03",

            "#1527F和约修亚进展的怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        (
            "#1013F唔…………\x02\x03",

            "#1022F雪、雪拉姐真是的，\x01",
            "怎么突然提起\x01",
            "这种话题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_513A")


    ChrTalk(    #152
        0x1C,
        "#1535F怎么，告诉我不行吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51B4")

    ChrTalk(    #153
        0x105,
        (
            "#1165F啊、啊哈哈……\x02\x03",

            "（的确……\x01",
            "  有点在意呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5206")
    OP_62(0x10B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #154
        0x10B,
        (
            "#216F什、什么都别说\x01",
            "就行了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5206")

    Jump("loc_5260")

    label("loc_5209")


    ChrTalk(    #155
        0x1C,
        (
            "#1520F你们两个都在这里。\x02\x03",

            "#1535F差不多该鼓起干劲，\x01",
            "离开这个世界了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5260")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_5A61")

    label("loc_526B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_5848")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5302")
    Jump("loc_5344")

    label("loc_5302")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_531E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5344")

    label("loc_531E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_533A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5344")

    label("loc_533A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5344")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #156
        0x1C,
        (
            "#1525F呼，不管怎么说，\x01",
            "你能平安无事真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#1004F哎…………我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x1C,
        (
            "#1525F……是啊。\x02\x03",

            "#1532F你不在的时候，\x01",
            "约修亚可是努力装出镇静的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_564B")

    ChrTalk(    #159
        0x102,
        (
            "#1505F……其实我也并没有\x01",
            "不知所措啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1017F那个……\x01",
            "让你担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x102,
        (
            "#1511F哎呀………\x01",
            "一般听说恋人被抓了的话，\x01",
            "都会很担心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1004F哎………………！？\x02\x03",

            "#1013F是、是吗……\x01",
            "什么时候变成这样……\x02\x03",

            "但、但是\x01",
            "虽说是被抓起来，\x01",
            "可我并没有那样的记忆……\x02\x03",

            "怎么说呢，\x01",
            "根本没有切身体会……\x02",
        )
    )

    Jump("loc_5591")

    label("loc_5591")

    CloseMessageWindow()

    ChrTalk(    #163
        0x1C,
        (
            "#1522F…………………………\x02\x03",

            "#1521F嗯，很好很好。\x02\x03",

            "这样姐姐我\x01",
            "也能安心喝酒了……㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1508F我说，雪拉姐姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1009F别随便理解呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_583A")

    label("loc_564B")


    ChrTalk(    #166
        0x101,
        "#1017F哎……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1C,
        (
            "#1526F哎呀，\x01",
            "你不是被『影之王』\x01",
            "那家伙抓起了来吗。\x02\x03",

            "#1535F约修亚\x01",
            "可是担心得\x01",
            "坐立不安哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1004F哎………………！？\x02\x03",

            "#1013F是、是吗……\x01",
            "什么时候变成这样……\x02\x03",

            "但、但是\x01",
            "虽说是被抓起来，\x01",
            "可我并没有那样的记忆……\x02\x03",

            "怎么说呢，\x01",
            "根本没有切身体会……\x02",
        )
    )

    Jump("loc_579D")

    label("loc_579D")

    CloseMessageWindow()

    ChrTalk(    #169
        0x1C,
        (
            "#1522F…………………………\x02\x03",

            "#1521F嗯，很好很好。\x02\x03",

            "这样姐姐我\x01",
            "也能安心喝酒了……㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1009F等一下，\x01",
            "怎么随便就理解了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583A")

    OP_A2(0x264C)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_5A61")

    label("loc_5848")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C4")

    ChrTalk(    #171
        0x1C,
        (
            "#1525F唉，这还真是\x01",
            "难以接受的情况啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x1C,
        "#1532F至少这里面都是酒也好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        "#1514F这不好吧，雪拉姐姐……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(    #174
        0x1C,
        (
            "#1526F好啦好啦，我知道了。\x02\x03",

            "#1520F要说卢·洛克尔训练场的话，\x01",
            "我也很熟悉呢。\x02\x03",

            "#1520F要是去那里探索的话，\x01",
            "就带上我吧。\x02\x03",

            "#1535F而且我也担心艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_5A50")

    label("loc_59C4")


    ChrTalk(    #175
        0x1C,
        (
            "#1532F唉，这还真是\x01",
            "难以接受的情况啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_63(0x1C)

    ChrTalk(    #176
        0x1C,
        (
            "#1525F嘁，爱娜那家伙……\x01",
            "现在是不是又在痛饮呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A50")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A61")

    Return()

    # Function_5_3352 end

    def Function_6_5A62(): pass

    label("Function_6_5A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5DAF")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE0")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #177
        0x19,
        (
            "#1543F……嗯…………？\x02\x03",

            "啊啊………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #178
        0x19,
        (
            "#1545F……看来事件\x01",
            "已经接近谢幕了。\x02\x03",

            "#1544F唉，\x01",
            "我可不想回到\x01",
            "工作堆积如山的现实世界中去……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BDA")

    ChrTalk(    #179
        0x10D,
        (
            "#272F不用担心，奥利维尔。\x02\x03",

            "#270F就算把你的耳朵揪掉\x01",
            "我也会把你带回去的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x10D, 0)

    ChrTalk(    #180
        0x19,
        "#1546F穆拉君好过分……！\x02",
    )

    CloseMessageWindow()

    label("loc_5BDA")

    OP_A2(0xF)
    Jump("loc_5D92")

    label("loc_5BE0")

    TalkBegin(0xFE)

    ChrTalk(    #181
        0x19,
        (
            "#1545F唉，这样看来\x01",
            "还真是有点舍不得呢。\x02\x03",

            "#1540F……要不要在临走之前\x01",
            "去追求一下那位始祖大人呢。\x02\x03",

            "#1541F唔～\x01",
            "应该不会遭报应吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CC9")

    ChrTalk(    #182
        0x101,
        (
            "#1007F还是算了吧。\x02\x03",

            "说不定你会被赶出庭院哦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D0B")

    ChrTalk(    #183
        0x102,
        (
            "#1514F……你还真是不怕死啊，\x01",
            "奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D5B")

    ChrTalk(    #184
        0x103,
        (
            "#1527F呵呵，说不定会遭到讨厌，\x01",
            "然后被扔到星层之外哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D92")

    ChrTalk(    #185
        0x105,
        "#1165F啊、啊哈哈哈哈…………\x02",
    )

    CloseMessageWindow()

    label("loc_5D92")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7FE2")

    label("loc_5DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_END)), "loc_5FD4")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E46")
    Jump("loc_5E88")

    label("loc_5E46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E62")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E88")

    label("loc_5E62")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E88")

    label("loc_5E7E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E88")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4D")

    ChrTalk(    #186
        0x19,
        (
            "#1540F教会的福音设施吗……\x01",
            "在边境好像有很多呢。\x02\x03",

            "#1545F的确，\x01",
            "帝国也有不少呢。\x02\x03",

            "被吞并的自治州等地区\x01",
            "经济也变得衰弱了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_5FC9")

    label("loc_5F4D")


    ChrTalk(    #187
        0x19,
        (
            "#1545F……被吞并的自治州等地区\x01",
            "经济也变得衰弱了。\x02\x03",

            "#1540F如果没有教会那样的慈善活动，\x01",
            "根本支撑不下去呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC9")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_5FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_6705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6357")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_607D")
    Jump("loc_60BF")

    label("loc_607D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6099")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60BF")

    label("loc_6099")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60B5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60BF")

    label("loc_60B5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60BF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E1")

    ChrTalk(    #188
        0x19,
        (
            "#1545F呼…………\x01",
            "在这里呆久了，\x01",
            "就会任凭想象力驰骋于上古时代。\x02\x03",

            "#1540F为什么这个能够满足一切愿望的\x01",
            "桃源乡会招来灭顶之灾，\x01",
            "我也说不清个所以然来……\x02\x03",

            "#1541F不过我认为\x01",
            "人们还是有资格拥有愿望和信念的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_622C")

    ChrTalk(    #189
        0x103,
        (
            "#1523F……奥利维尔，\x01",
            "你的杯子又空了。\x02\x03",

            "#1521F我给你倒满吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6280")

    label("loc_622C")

    SetChrSubChip(0x1C, 2)

    ChrTalk(    #190
        0x1C,
        (
            "#1523F……奥利维尔，\x01",
            "你的杯子又空了。\x02\x03",

            "#1530F我给你倒满吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6280")

    SetChrSubChip(0x19, 0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #191
        0x19,
        (
            "#1546F不、不用了……\x01",
            "再喝我的意识就会飞走的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0)
    OP_A2(0xF)
    Jump("loc_634C")

    label("loc_62E1")


    ChrTalk(    #192
        0x19,
        (
            "#1545F呼…………\x01",
            "我认为人们还是有资格\x01",
            "拥有愿望和信念的。\x02\x03",

            "#1546F总、总之\x01",
            "酒差不多该……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_634C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_6702")

    label("loc_6357")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63E7")
    Jump("loc_6429")

    label("loc_63E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6403")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6429")

    label("loc_6403")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6429")

    label("loc_641F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6429")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #193
        0x102,
        (
            "#1505F……奥利维尔先生。\x02\x03",

            "#1500F我们前往帝国的时候，\x01",
            "哈梅尔村的封锁\x01",
            "已经解除了。\x02\x03",

            "那是奥利维尔先生\x01",
            "你的指示吧。\x02\x03",

            "#1513F……谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x19,
        (
            "#1545F呼，\x01",
            "别说那么见外的话嘛。\x02\x03",

            "#1547F就凭我们两个的\x01",
            "既甜蜜又危险的关系，\x01",
            "这点事还不是小菜一碟？\x02\x03",

            "#1541F不过，\x01",
            "如果你非要向我道谢的话，\x01",
            "那就用你的拥抱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x102,
        (
            "#1514F………哈哈…………\x02\x03",

            "#1513F就算是皇族的人……#400W\x01",
            "#20W不，正因为是皇族，\x01",
            "哈梅尔的事件更是所谓的禁忌。\x02\x03",

            "#1501F明知道这一点，却还……\x01",
            "真的是十分感谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x19,
        (
            "#1540F哈哈…………\x02\x03",

            "#1545F的确，从我的立场上来说，\x01",
            "那可不是能够随便接近的地方。\x02\x03",

            "本来想顺便去献花的……\x01",
            "还是让你们代劳吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2654)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_6702")

    Jump("loc_7FE2")

    label("loc_6705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_6B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F6")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_685F")
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)

    ChrTalk(    #197
        0x19,
        "#1548F呜，咕噜咕噜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x103,
        "#1523F……哎呀，怎么了奥利维尔。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67EB")

    ChrTalk(    #199
        0x101,
        (
            "#1016F你问怎么了……\x02\x03",

            "这不明摆着是\x01",
            "被雪拉姐灌醉的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_67EB")


    ChrTalk(    #200
        0x109,
        (
            "#1061F无论怎么想，\x01",
            "原因都出在这个大姐身上吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6827")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_685C")

    ChrTalk(    #201
        0x102,
        "#1508F……没有自知之明吗？\x02",
    )

    CloseMessageWindow()

    label("loc_685C")

    Jump("loc_68E8")

    label("loc_685F")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #202
        0x19,
        (
            "#1546F雪、雪拉君……\x02\x03",

            "你是不是\x01",
            "喝得太快了……？\x02",
        )
    )

    Jump("loc_68C4")

    label("loc_68C4")

    CloseMessageWindow()

    ChrTalk(    #203
        0x1C,
        "#1526F嗝………………！\x02",
    )

    CloseMessageWindow()

    label("loc_68E8")

    OP_A2(0xF)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6B30")

    label("loc_68F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_698E")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #204
        0x103,
        (
            "#1527F……只有喝饱了才能行动嘛。\x02\x03",

            "#1530F下次探索就带上我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x109,
        "#1068F（真是酒鬼…………）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6B30")

    label("loc_698E")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A1E")
    Jump("loc_6A60")

    label("loc_6A1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A3A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A60")

    label("loc_6A3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A56")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A60")

    label("loc_6A56")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A60")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #206
        0x19,
        (
            "#1542F处于思考状态中的雪拉君，\x01",
            "在无意识中\x01",
            "喝酒会越来越猛烈。\x02\x03",

            "不过那副样子也不错……\x02\x03",

            "#1547F呼，陪酒时一不小心\x01",
            "就把自己弄得烂醉……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_6B30")

    Jump("loc_7FE2")

    label("loc_6B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_6E58")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BCA")
    Jump("loc_6C0C")

    label("loc_6BCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BE6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C0C")

    label("loc_6BE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C02")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C0C")

    label("loc_6C02")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C0C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D72")

    ChrTalk(    #207
        0x19,
        (
            "#1540F尤莉亚小姐、雾香小姐……\x02\x03",

            "#1545F哎呀，\x01",
            "利贝尔的女强人还真多。\x02\x03",

            "#1544F小提妲身边也总是跟着\x01",
            "可怕的保镖，唉……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D13")

    ChrTalk(    #208
        0x106,
        "#053F……这话别让我听到第二次哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D3F")

    label("loc_6D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D3F")

    ChrTalk(    #209
        0x107,
        "#064F哎…………？\x02",
    )

    CloseMessageWindow()

    label("loc_6D3F")


    ChrTalk(    #210
        0x109,
        (
            "#1077F哈哈，\x01",
            "最好别惹阿加特生气哦？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC9")

    label("loc_6D72")


    ChrTalk(    #211
        0x19,
        (
            "#1540F正如雪拉君所说的那样。\x02\x03",

            "#1541F这次就装出\x01",
            "稳重严肃点的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC9")

    OP_A2(0xF)
    Jump("loc_6E4D")

    label("loc_6DCF")


    ChrTalk(    #212
        0x19,
        (
            "#1542F唔，\x01",
            "没想到『影之国』竟然也能\x01",
            "重现身处共和国的人……\x02\x03",

            "#1551F说不定，\x01",
            "以后还会遇上\x01",
            "意想不到的人物呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E4D")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_6E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_7079")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EEF")
    Jump("loc_6F31")

    label("loc_6EEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F0B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F31")

    label("loc_6F0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F27")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F31")

    label("loc_6F27")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F31")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700A")

    ChrTalk(    #213
        0x19,
        (
            "#1545F唔……\x01",
            "能根据意念改变构造的世界吗……\x02\x03",

            "如果认清这件事实\x01",
            "就是通过名为『第五星层』的\x01",
            "游戏盘的条件的话……\x02\x03",

            "#1540F的确已经接近终点了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_706E")

    label("loc_700A")


    ChrTalk(    #214
        0x19,
        (
            "#1541F呵呵，\x01",
            "真没想到必须得分析\x01",
            "和证明到如此程度才行。\x02\x03",

            "我感到了一种莫名的激动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_706E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_7079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_76BF")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7110")
    Jump("loc_7152")

    label("loc_7110")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_712C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7152")

    label("loc_712C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7148")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7152")

    label("loc_7148")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7152")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_739A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72FB")

    ChrTalk(    #215
        0x19,
        "#1543F呵，这游戏……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #216
        0x19,
        (
            "#1547F真是前所未闻的冲击。\x02\x03",

            "让我们愉快地迎接它吧！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x101,
        "#1019F奥利维尔，你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x103,
        (
            "#1535F把你倒着吊到\x01",
            "那个瀑布上怎么样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x19,
        (
            "#1546F……对不起。\x01",
            "请原谅我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7397")

    label("loc_72FB")


    ChrTalk(    #220
        0x19,
        (
            "#1540F要找雪拉君吗？\x01",
            "她去找那个神父了。\x02\x03",

            "#1545F……所以，艾丝蒂尔君，\x01",
            "作为妹妹你就来安慰我一番吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1019F哼，\x01",
            "别胡搅蛮缠了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7397")

    Jump("loc_7594")

    label("loc_739A")


    ChrTalk(    #222
        0x19,
        (
            "#1540F……小提妲，\x01",
            "你是不是累了呢。\x02\x03",

            "#1541F那就来边听我讲故事\x01",
            "边睡个觉吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1019F……我感到了一种\x01",
            "非常危险的气息……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7461")

    ChrTalk(    #224
        0x102,
        "#1505F………………同感。\x02",
    )

    CloseMessageWindow()

    label("loc_7461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749A")

    ChrTalk(    #225
        0x10D,
        (
            "#272F嗯，\x01",
            "我也这么觉得。\x02",
        )
    )

    Jump("loc_7499")

    label("loc_7499")

    CloseMessageWindow()

    label("loc_749A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D8")

    ChrTalk(    #226
        0x103,
        (
            "#1525F你那油嘴滑舌\x01",
            "还是没有变啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7516")

    ChrTalk(    #227
        0x106,
        "#057F#3S（怒）…………………！！#2S\x02",
    )

    CloseMessageWindow()

    label("loc_7516")


    ChrTalk(    #228
        0x19,
        (
            "#1541F哈哈，讨厌啦……\x02\x03",

            "#1547F我的行动方针\x01",
            "永远是女士优先呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1022F你这种想法才是最危险的呢。\x02",
    )

    CloseMessageWindow()

    label("loc_7594")

    OP_A2(0xF)
    Jump("loc_76B4")

    label("loc_759A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7608")

    ChrTalk(    #230
        0x19,
        (
            "#1551F唉，\x01",
            "总觉得有些美中不足呢。 \x02\x03",

            "#1542F……艾丝蒂尔君，\x01",
            "请来安慰我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B4")

    label("loc_7608")

    SetChrSubChip(0x19, 1)

    ChrTalk(    #231
        0x19,
        (
            "#1540F呵呵，这睡觉的表情\x01",
            "还真是能激发我的父性之爱呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #232
        0x19,
        (
            "#1541F虽然被称呼哥哥也不错，\x01",
            "不过当爸爸也别有一番浪漫㈱\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0)

    label("loc_76B4")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_76BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 3)), scpexpr(EXPR_END)), "loc_7930")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7756")
    Jump("loc_7798")

    label("loc_7756")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7772")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7798")

    label("loc_7772")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_778E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7798")

    label("loc_778E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7798")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78AE")

    ChrTalk(    #233
        0x19,
        (
            "#1551F与带有『圣痕』的\x01",
            "守护骑士为敌的\x01",
            "『黑骑士』和『影之王』……\x02\x03",

            "唔，\x01",
            "这可是非常难缠的对手。\x02\x03",

            "#1547F……所以，\x01",
            "就让我稍稍舒展一下手脚吧。\x02",
        )
    )

    Jump("loc_786F")

    label("loc_786F")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78A8")

    ChrTalk(    #234
        0x10D,
        "#274F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_78A8")

    OP_A2(0xF)
    Jump("loc_7925")

    label("loc_78AE")


    ChrTalk(    #235
        0x19,
        (
            "#1551F与带有『圣痕』的\x01",
            "守护骑士为敌的\x01",
            "『黑骑士』和『影之王』……\x02\x03",

            "唔，\x01",
            "这可是非常难缠的对手。\x02",
        )
    )

    Jump("loc_7924")

    label("loc_7924")

    CloseMessageWindow()

    label("loc_7925")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_7930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_7D77")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79C7")
    Jump("loc_7A09")

    label("loc_79C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79E3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A09")

    label("loc_79E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79FF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A09")

    label("loc_79FF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A09")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #236
        0x19,
        (
            "#1542F……我也调查过\x01",
            "与封圣省和星杯骑士团\x01",
            "相关的事情……\x02\x03",

            "#1551F能操纵『圣痕』的守护骑士吗……\x01",
            "没想到拥有那么强大的力量。\x02\x03",

            "#1542F不过，那个『影之王』\x01",
            "敢与这样的星杯骑士团作对，\x01",
            "看来也是个非常难缠的对手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#1002F嗯，从大家说的话来看，\x01",
            "确实不是普通的对手呢。\x02\x03",

            "#1011F……这个暂且不说。\x02\x03",

            "#1006F奥利维尔，\x01",
            "你那边进行的还顺利吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #238
        0x19,
        "#1543F我这边…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1006F就是你回到\x01",
            "帝国之后的事情啦。\x02\x03",

            "#1012F你在哈肯大门\x01",
            "竟然演了那么一出好戏，\x01",
            "把我们都给骗过去了……\x02\x03",

            "#1018F不老实交代的话我可要揍你哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x19,
        (
            "#1543F………………………………\x02\x03",

            "#1540F……哈哈，你说的没错。\x02\x03",

            "#1541F不愧是艾丝蒂尔君。\x01",
            "你的训诫我接受了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1004F嗯……你还真老实。\x02\x03",

            "#1002F奥利维尔，你没事吧？\x01",
            "是不是喝的太多了？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2653)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_7FE2")

    label("loc_7D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_7FE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E84")
    TalkBegin(0xFF)

    ChrTalk(    #242
        0x19,
        (
            "#1545F雪拉君，\x01",
            "你想喝酒的话就来找我吧。\x02\x03",

            "这是从那棵大树那里找到的，\x01",
            "相当香醇的美酒呢。\x02\x03",

            "#1541F……虽然无法判定品种和年代。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#1500F你还敢说这样的话，\x01",
            "又会被灌得不省人事的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x19,
        "#1546F铛铛…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    TalkEnd(0xFF)
    Jump("loc_7FE2")

    label("loc_7E84")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F14")
    Jump("loc_7F56")

    label("loc_7F14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F30")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F56")

    label("loc_7F30")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F4C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F56")

    label("loc_7F4C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F56")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #245
        0x19,
        (
            "#1545F哦、哦呵呵……\x01",
            "爱娜君不在，没关系啦。\x02\x03",

            "#1546F谁快来告诉我『没关系』！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_7FE2")

    Return()

    # Function_6_5A62 end

    def Function_7_7FE3(): pass

    label("Function_7_7FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 1)), scpexpr(EXPR_END)), "loc_83D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8214")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81BF")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8090")
    Jump("loc_80D2")

    label("loc_8090")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80AC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_80D2")

    label("loc_80AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80C8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_80D2")

    label("loc_80C8")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80D2")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #246
        0x17,
        (
            "#1160F……说起来，\x01",
            "这还真是个美丽的地方呢。\x02\x03",

            "既有茂密的大树，\x01",
            "又有流淌的泉水，\x01",
            "给人一种心平气和的感觉呢。\x02\x03",

            "#1382F…………那个……\x01",
            "这里是叫做……『隐者之庭院』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_820E")

    label("loc_81BF")

    TalkBegin(0xFF)

    ChrTalk(    #247
        0x17,
        (
            "#1169F……是吗。\x02\x03",

            "难不成，\x01",
            "艾丝蒂尔也……\x02",
        )
    )

    Jump("loc_820A")

    label("loc_820A")

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_820E")

    OP_A2(0xD)
    Jump("loc_83D2")

    label("loc_8214")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8383")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82B2")
    Jump("loc_82F4")

    label("loc_82B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_82CE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82F4")

    label("loc_82CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82EA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82F4")

    label("loc_82EA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_82F4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #248
        0x17,
        (
            "#1383F『隐者之庭院』…………\x02\x03",

            "#1160F呵呵，的确是个\x01",
            "能让人感到平静的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_83D2")

    label("loc_8383")

    TalkBegin(0xFF)

    ChrTalk(    #249
        0x17,
        (
            "#1169F……是吗。\x02\x03",

            "难不成，\x01",
            "艾丝蒂尔也……\x02",
        )
    )

    Jump("loc_83CE")

    label("loc_83CE")

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_83D2")

    Jump("loc_8A35")

    label("loc_83D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_8A35")
    SetChrFlags(0x17, 0x10)
    TalkBegin(0x17)

    ChrTalk(    #250
        0x17,
        (
            "#1167F……在睡觉之前\x01",
            "我本来是打算写日记的……\x02\x03",

            "#1162F不经意间看了一眼窗外，\x01",
            "却看到了十分刺眼的光芒。\x02\x03",

            "#1163F然后，眼前就变得一片白……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84D8")

    ChrTalk(    #251
        0x16,
        (
            "#1503F……是吗，\x01",
            "从你的房间可以看到格兰赛尔的码头……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_858A")

    label("loc_84D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8530")

    ChrTalk(    #252
        0x13,
        (
            "#176F……原来如此，从殿下的寝室\x01",
            "可以看到格兰赛尔的码头……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_858A")

    label("loc_8530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_858A")

    ChrTalk(    #253
        0x15,
        (
            "#213F啊啊，是吗……\x02\x03",

            "格兰赛尔的王城，\x01",
            "的确离码头很近呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_858A")


    ChrTalk(    #254
        0x17,
        (
            "#1167F是的…………\x02\x03",

            "从大家所叙述的情况来看，\x01",
            "每个人都是在『方石』\x01",
            "发动的时候被卷进去的吧。\x02\x03",

            "#1169F……在看到那光芒的时候\x01",
            "也许应该采取些\x01",
            "什么措施才好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88AA")
    TurnDirection(0x10B, 0x17, 0)

    ChrTalk(    #255
        0x10B,
        (
            "#215F啊，那个…………\x02\x03",

            "#210F虽然还搞不清楚状况，\x01",
            "不过总之水和食物\x01",
            "都不用发愁了呢。\x02\x03",

            "所以就不用担心了。\x01",
            "做饭的事就交给我吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x10B, 0)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8778")
    Jump("loc_87BA")

    label("loc_8778")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8794")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87BA")

    label("loc_8794")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B0")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87BA")

    label("loc_87B0")

    OP_51(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87BA")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(    #256
        0x17,
        (
            "#1160F那个……如果可以的话，\x01",
            "请让我也一起好吗。\x02\x03",

            "#1165F呵呵，我也很擅长料理呢……\x01",
            "找点事情做就可以让心情平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10B,
        (
            "#213F啊，嗯…………\x02\x03",

            "#210F是啊，就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0F")

    label("loc_88AA")


    ChrTalk(    #258
        0x15,
        (
            "#215F啊，那个…………\x02\x03",

            "#210F虽然还搞不清楚状况，\x01",
            "不过总之水和食物\x01",
            "都不用发愁了呢。\x02\x03",

            "所以就不用担心了。\x01",
            "做饭的事就交给我吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 2)

    ChrTalk(    #259
        0x17,
        (
            "#1160F那个……如果可以的话，\x01",
            "请让我也一起好吗。\x02\x03",

            "#1165F呵呵，我也很擅长料理呢……\x01",
            "找点事情做就可以让心情平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x15,
        (
            "#213F啊，嗯…………\x02\x03",

            "#210F是啊，就这么办吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A25")
    SetChrSubChip(0x17, 0)
    Jump("loc_8A2A")

    label("loc_8A25")

    SetChrSubChip(0x17, 2)

    label("loc_8A2A")

    OP_A2(0x2651)
    ClearChrFlags(0x17, 0x10)
    TalkEnd(0x17)

    label("loc_8A35")

    Return()

    # Function_7_7FE3 end

    def Function_8_8A36(): pass

    label("Function_8_8A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_8C2F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ACD")
    Jump("loc_8B0F")

    label("loc_8ACD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AE9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0F")

    label("loc_8AE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B05")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0F")

    label("loc_8B05")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B0F")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB2")

    ChrTalk(    #261
        0x1D,
        (
            "#551F……呼………………\x02\x03",

            "#053F那么，也该继续前进了吧。\x02\x03",

            "#051F接下来是『第七星层』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_8C24")

    label("loc_8BB2")


    ChrTalk(    #262
        0x1D,
        (
            "#053F接下来是『第七星层』吧。\x02\x03",

            "#051F……据说是『影之王』\x01",
            "最初创建的场所。\x02\x03",

            "要小心前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C24")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_8C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 7)), scpexpr(EXPR_END)), "loc_8D19")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CB7")

    ChrTalk(    #263
        0x1D,
        (
            "#053F……跟那个胡子大叔\x01",
            "第一次见面的时候，\x01",
            "可被他整惨了……\x02\x03",

            "#051F总有一天会让他加倍偿还的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_8D13")

    label("loc_8CB7")


    ChrTalk(    #264
        0x1D,
        (
            "#053F……那个胡子大叔\x01",
            "欠了我很多人情。\x02\x03",

            "#051F总有一天会让他\x01",
            "加倍偿还的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D13")

    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_8D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_910F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 1)), scpexpr(EXPR_END)), "loc_8F3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D8E")
    TurnDirection(0x1D, 0x101, 0)

    ChrTalk(    #265
        0x101,
        (
            "#1004F啊，阿加特。\x02\x03",

            "#1028F呵呵……和父亲战斗的感觉如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E76")

    label("loc_8D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E03")
    TurnDirection(0x1D, 0x103, 0)

    ChrTalk(    #266
        0x103,
        (
            "#1520F哎呀，阿加特……\x02\x03",

            "#1521F呵呵，实现了怨念已久的对决，\x01",
            "你有什么感想？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E76")

    label("loc_8E03")


    ChrTalk(    #267
        0x109,
        (
            "#1066F啊，阿加特。\x01",
            "刚才真是帮大忙了。\x02\x03",

            "#1060F……说起来，\x01",
            "你好像和卡西乌斯先生\x01",
            "有过什么纠葛……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E76")


    ChrTalk(    #268
        0x1D,
        (
            "#053F哼…………\x01",
            "就打了一场，\x01",
            "真是不过瘾。\x02\x03",

            "#552F跟那个胡子大叔\x01",
            "第一次见面的时候，\x01",
            "可被他整惨了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x109,
        "#1064F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1D,
        (
            "#051F哼，总有一天\x01",
            "会让他加倍偿还的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9106")

    label("loc_8F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FA0")
    TurnDirection(0x1D, 0x101, 0)

    ChrTalk(    #271
        0x101,
        (
            "#1004F啊，阿加特。\x02\x03",

            "#1015F那个，\x01",
            "第三守护者是我老爸……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_905C")

    label("loc_8FA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_900D")
    TurnDirection(0x1D, 0x103, 0)

    ChrTalk(    #272
        0x103,
        (
            "#1523F哎呀，阿加特……\x02\x03",

            "#1520F……第三守护者\x01",
            "是卡西乌斯先生呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_905C")

    label("loc_900D")


    ChrTalk(    #273
        0x109,
        (
            "#1066F啊，阿加特。\x02\x03",

            "……第三守护者\x01",
            "是那个卡西乌斯先生呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_905C")


    ChrTalk(    #274
        0x1D,
        (
            "#053F……我知道了。\x02\x03",

            "那位始祖大人\x01",
            "已经告诉过我们了。\x02\x03",

            "#552F……哼，\x01",
            "没能跟他打一场真是遗憾……\x02\x03",

            "#556F那时候欠下的人情，\x01",
            "下次再让他还吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9106")

    OP_A2(0x264F)
    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_910F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_9370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9290")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 3)), scpexpr(EXPR_END)), "loc_91F2")

    ChrTalk(    #275
        0x1D,
        (
            "#552F雾香那家伙……\x02\x03",

            "之前我就觉得她是个\x01",
            "十分不通情理的女人……\x02\x03",

            "#053F……哼，算了。\x02\x03",

            "回去之后，\x01",
            "暂时在蔡斯工作一段时间吧。\x02\x03",

            "#051F那家伙好像很喜欢\x01",
            "那个城市呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9287")

    label("loc_91F2")


    ChrTalk(    #276
        0x1D,
        (
            "#552F雾香那家伙……\x02\x03",

            "#053F……哼，算了。\x02\x03",

            "回去之后，\x01",
            "暂时在蔡斯工作一段时间吧。\x02\x03",

            "#051F那家伙好像很喜欢\x01",
            "那个城市呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9287")

    OP_A2(0x6)
    TalkEnd(0xFE)
    Jump("loc_936D")

    label("loc_9290")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #277
        0x1D,
        (
            "#057F…………不，等一下。\x01",
            "艾莉卡·拉赛尔也在蔡斯……\x02\x03",

            "#555F……………………………………\x01",
            "……………………………………\x01",
            "……………………………………\x02\x03",

            "#552F…………哼……………………\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_936D")

    Jump("loc_AC52")

    label("loc_9370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_9551")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9494")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_942A")

    ChrTalk(    #278
        0x108,
        (
            "#073F……阿加特，\x01",
            "你在一个人练功吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1D,
        (
            "#051F金，\x01",
            "有空的话我们来切磋一下吧。\x02\x03",

            "果然还是要有对手\x01",
            "练起功来才方便。\x02",
        )
    )

    Jump("loc_9426")

    label("loc_9426")

    CloseMessageWindow()
    Jump("loc_948E")

    label("loc_942A")


    ChrTalk(    #280
        0x1D,
        (
            "#053F……哦，\x01",
            "你们最好也锻炼一下。\x02\x03",

            "#051F以后还不知道\x01",
            "会遇到什么样的危险情况呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_948E")

    OP_A2(0x6)
    Jump("loc_9546")

    label("loc_9494")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94FC")

    ChrTalk(    #281
        0x1D,
        (
            "#053F嘶……哈～………\x01",
            "嘶……哈～………\x02\x03",

            "#057F呼～～～………………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9546")

    label("loc_94FC")


    ChrTalk(    #282
        0x1D,
        (
            "#053F……好，再来一次。\x02\x03",

            "#051F金，一会儿来切磋一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9546")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_AC52")

    label("loc_9551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_98C4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9815")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_961F")

    ChrTalk(    #283
        0x1D,
        (
            "#053F……刚才，\x01",
            "我听金说过了。\x02\x03",

            "这个世界好像近似于\x01",
            "什么仙界之类的地方。\x02\x03",

            "#051F哼，虽然不知道怎么回事……\x01",
            "不过在这里修行的话，\x01",
            "应该会变得很强吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96C3")

    label("loc_961F")


    ChrTalk(    #284
        0x1D,
        (
            "#053F……喂，听说了吗？\x02\x03",

            "这个世界好像近似于\x01",
            "什么仙界之类的地方。\x02\x03",

            "#051F哼，虽然不知道怎么回事……\x01",
            "不过在这里修行的话，\x01",
            "应该会变得很强吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96C3")

    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_970A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9700")
    TurnDirection(0x106, 0x108, 400)
    Jump("loc_9707")

    label("loc_9700")

    TurnDirection(0x1D, 0x108, 400)

    label("loc_9707")

    Jump("loc_9729")

    label("loc_970A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9722")
    TurnDirection(0x106, 0x1A, 400)
    Jump("loc_9729")

    label("loc_9722")

    TurnDirection(0x1D, 0x1A, 400)

    label("loc_9729")


    ChrTalk(    #285
        0x1D,
        (
            "#051F……金，\x01",
            "一会儿我们来切磋一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x1A, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9790")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9786")
    TurnDirection(0x108, 0x106, 400)
    Jump("loc_978D")

    label("loc_9786")

    TurnDirection(0x1A, 0x106, 400)

    label("loc_978D")

    Jump("loc_97AF")

    label("loc_9790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97A8")
    TurnDirection(0x108, 0x1D, 400)
    Jump("loc_97AF")

    label("loc_97A8")

    TurnDirection(0x1A, 0x1D, 400)

    label("loc_97AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97E2")

    ChrTalk(    #286
        0x108,
        "#070F哈哈，我无所谓。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9804")

    label("loc_97E2")


    ChrTalk(    #287
        0x1A,
        "#070F哈哈，我无所谓。\x02",
    )

    CloseMessageWindow()

    label("loc_9804")

    OP_4B(0x1A, 255)
    OP_8C(0x1A, 81, 0)
    OP_A2(0x6)
    Jump("loc_98BE")

    label("loc_9815")


    ChrTalk(    #288
        0x1D,
        (
            "#050F这里好像近似于\x01",
            "什么仙界之类的地方。\x02\x03",

            "#053F哼，虽然不知道怎么回事……\x01",
            "不过真是个不错的修行场呢。\x02\x03",

            "#051F好，\x01",
            "也在这里锻炼一下吧……！\x02",
        )
    )

    Jump("loc_98BD")

    label("loc_98BD")

    CloseMessageWindow()

    label("loc_98BE")

    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_98C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_99E5")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9971")

    ChrTalk(    #289
        0x1D,
        (
            "#552F虽然还不清楚这个\x01",
            "异空间世界的原理……\x02\x03",

            "不过可以肯定的是\x01",
            "这里的魔物不是一般的强大。\x02\x03",

            "#057F我们也必须锻炼得更强才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_99DF")

    label("loc_9971")


    ChrTalk(    #290
        0x1D,
        (
            "#053F每次『恶魔』出现的时候\x01",
            "不能总交给\x01",
            "那个神父对付啊。\x02\x03",

            "#057F我们也必须锻炼得更强才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99DF")

    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_99E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 6)), scpexpr(EXPR_END)), "loc_9BCF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A8F")
    TurnDirection(0x1D, 0x10C, 0)

    ChrTalk(    #291
        0x1D,
        (
            "#051F上校，你的功夫相当了得。\x02\x03",

            "在这里遇到也算是一种缘分。\x01",
            "能跟我切磋一番吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x10C,
        "#119F哈、哈哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AED")

    label("loc_9A8F")


    ChrTalk(    #293
        0x1D,
        (
            "#051F那个上校也相当厉害嘛。\x02\x03",

            "在这里遇到也算是一种缘分。\x01",
            "真想和他切磋一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AED")

    OP_A2(0x6)
    Jump("loc_9BC9")

    label("loc_9AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B6B")
    TurnDirection(0x1D, 0x10C, 0)

    ChrTalk(    #294
        0x1D,
        (
            "#051F上校，你的功夫相当了得。\x02\x03",

            "在这里遇到也算是一种缘分。\x01",
            "能跟我切磋一番吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BC9")

    label("loc_9B6B")


    ChrTalk(    #295
        0x1D,
        (
            "#051F那个上校也相当厉害嘛。\x02\x03",

            "在这里遇到也算是一种缘分。\x01",
            "真想和他切磋一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BC9")

    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_9BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_A745")
    TalkBegin(0xFE)
    OP_4A(0x1D, 255)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D13")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C9C")

    ChrTalk(    #296
        0x1D,
        (
            "#052F哦，是艾丝蒂尔和约修亚。\x02\x03",

            "#051F刚才我从雪拉扎德\x01",
            "那里听说了……\x02\x03",

            "#051F亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D10")

    label("loc_9C9C")


    ChrTalk(    #297
        0x1D,
        (
            "#052F哦，是艾丝蒂尔和约修亚。\x02\x03",

            "#051F……你们听说了吗？\x01",
            "亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D10")

    Jump("loc_9E14")

    label("loc_9D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DAA")

    ChrTalk(    #298
        0x1D,
        (
            "#052F哦，是艾丝蒂尔。\x02\x03",

            "#051F刚才我从雪拉扎德\x01",
            "那里听说了……\x02\x03",

            "#051F亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E14")

    label("loc_9DAA")


    ChrTalk(    #299
        0x1D,
        (
            "#052F哦，是艾丝蒂尔。\x02\x03",

            "#051F……你听说过吗？\x01",
            "亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E44")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E3A")
    TurnDirection(0x101, 0x10A, 400)
    Jump("loc_9E41")

    label("loc_9E3A")

    TurnDirection(0x1E, 0x10A, 400)

    label("loc_9E41")

    Jump("loc_9E63")

    label("loc_9E44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E5C")
    TurnDirection(0x101, 0x1B, 400)
    Jump("loc_9E63")

    label("loc_9E5C")

    TurnDirection(0x1E, 0x1B, 400)

    label("loc_9E63")


    ChrTalk(    #300
        0x101,
        "#1004F哎，是真的吗……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EAE")
    TurnDirection(0x10A, 0x101, 400)
    Jump("loc_9EB5")

    label("loc_9EAE")

    TurnDirection(0x1B, 0x101, 400)

    label("loc_9EB5")

    Jump("loc_9ED7")

    label("loc_9EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9ED0")
    TurnDirection(0x10A, 0x1E, 400)
    Jump("loc_9ED7")

    label("loc_9ED0")

    TurnDirection(0x1B, 0x1E, 400)

    label("loc_9ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F34")

    ChrTalk(    #301
        0x10A,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F80")

    label("loc_9F34")


    ChrTalk(    #302
        0x1B,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F80")


    ChrTalk(    #303
        0x10C,
        (
            "#111F呵呵，\x01",
            "其实那都是卡西乌斯准将的安排。\x02\x03",

            "#110F让我能有机会再次\x01",
            "拿起这远未成熟的剑。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A07E")

    ChrTalk(    #304
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        (
            "#1500F嗯，四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0FC")

    label("loc_A07E")


    ChrTalk(    #306
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02\x03",

            "四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    Jump("loc_A0FB")

    label("loc_A0FB")

    CloseMessageWindow()

    label("loc_A0FC")


    ChrTalk(    #307
        0x10C,
        (
            "#118F哈哈，现在想起来，\x01",
            "只有不堪回首的记忆而已……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x10C, 400)

    ChrTalk(    #308
        0x1D,
        (
            "#051F哼，你的剑法\x01",
            "是得自卡西乌斯大叔的直传吧？\x02\x03",

            "有机会的话，\x01",
            "我也想和你切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x10C,
        (
            "#495F（哎呀，这么看得起我\x01",
            "  我也很难办啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A734")

    label("loc_A1E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A30B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A294")

    ChrTalk(    #310
        0x1D,
        (
            "#052F哦，是艾丝蒂尔和约修亚。\x02\x03",

            "#051F刚才我从雪拉扎德\x01",
            "那里听说了……\x02\x03",

            "#051F亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A308")

    label("loc_A294")


    ChrTalk(    #311
        0x1D,
        (
            "#052F哦，是艾丝蒂尔和约修亚。\x02\x03",

            "#051F……你们听说了吗？\x01",
            "亚妮拉丝那家伙，\x01",
            "好像和这个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A308")

    Jump("loc_A40C")

    label("loc_A30B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3A2")

    ChrTalk(    #312
        0x1D,
        (
            "#052F哦，是艾丝蒂尔。\x02\x03",

            "#051F刚才我从雪拉扎德\x01",
            "那里听说了……\x02\x03",

            "#051F亚妮拉丝那家伙，\x01",
            "好像和那个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A40C")

    label("loc_A3A2")


    ChrTalk(    #313
        0x1D,
        (
            "#052F哦，是艾丝蒂尔。\x02\x03",

            "#051F……你听说过吗？\x01",
            "亚妮拉丝那家伙，\x01",
            "好像和那个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A40C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A43C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A432")
    TurnDirection(0x101, 0x10A, 400)
    Jump("loc_A439")

    label("loc_A432")

    TurnDirection(0x1E, 0x10A, 400)

    label("loc_A439")

    Jump("loc_A45B")

    label("loc_A43C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A454")
    TurnDirection(0x101, 0x1B, 400)
    Jump("loc_A45B")

    label("loc_A454")

    TurnDirection(0x1E, 0x1B, 400)

    label("loc_A45B")


    ChrTalk(    #314
        0x101,
        "#1004F哎，是真的吗……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4BC")

    ChrTalk(    #315
        0x103,
        (
            "#1525F我听说的时候，\x01",
            "也很吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4E2")
    TurnDirection(0x10A, 0x101, 400)
    Jump("loc_A4E9")

    label("loc_A4E2")

    TurnDirection(0x1B, 0x101, 400)

    label("loc_A4E9")

    Jump("loc_A50B")

    label("loc_A4EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A504")
    TurnDirection(0x10A, 0x1E, 400)
    Jump("loc_A50B")

    label("loc_A504")

    TurnDirection(0x1B, 0x1E, 400)

    label("loc_A50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A568")

    ChrTalk(    #316
        0x10A,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5B4")

    label("loc_A568")


    ChrTalk(    #317
        0x1B,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A648")

    ChrTalk(    #318
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x102,
        (
            "#1500F嗯，四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6C6")

    label("loc_A648")


    ChrTalk(    #320
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02\x03",

            "四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    Jump("loc_A6C5")

    label("loc_A6C5")

    CloseMessageWindow()

    label("loc_A6C6")


    ChrTalk(    #321
        0x1D,
        (
            "#053F那家伙的剑法\x01",
            "是得自卡西乌斯大叔的直传……\x02\x03",

            "#051F哼，有机会的话\x01",
            "我也想和他切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A734")

    OP_4B(0x1D, 255)
    OP_4B(0x1B, 255)
    OP_A2(0x264E)
    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_A745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_A86E")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A802")

    ChrTalk(    #322
        0x1D,
        (
            "#552F我不知道那个神父\x01",
            "是『守护骑士』还是什么的……\x02\x03",

            "#053F哼，就会乱来……\x02\x03",

            "一句话没说就倒下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1019F……你有资格说这种话吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_A868")

    label("loc_A802")


    ChrTalk(    #324
        0x1D,
        (
            "#552F一开始我还觉得\x01",
            "那个神父是个可疑的人物……\x02\x03",

            "#053F哼……\x01",
            "居然这么简单就倒下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A868")

    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_A86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB8C")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A893")
    Call(5, 9)
    Jump("loc_AB89")

    label("loc_A893")

    TurnDirection(0x1D, 0x107, 0)

    ChrTalk(    #325
        0x107,
        (
            "#067F可是可是，\x01",
            "阿加特大哥哥没事真是太好了。\x02\x03",

            "#560F我一直害怕\x01",
            "万一阿加特大哥哥也被卷入其中，\x01",
            "所以担心得不得了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x1D,
        (
            "#551F所以啦，\x01",
            "你就别这样搂着我了。\x02\x03",

            "#050F反倒是提妲，\x01",
            "你…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #327
        0x1D,
        (
            "#552F……在我没注意到的地方，\x01",
            "是不是又遇到什么危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x107,
        (
            "#565F那个…………\x02\x03",

            "没、没什么事啦。\x02\x03",

            "#067F反正是和凯文哥哥\x01",
            "他们一起行动…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x1D,
        (
            "#053F是吗…………\x02\x03",

            "#051F那我就不多说了。\x02\x03",

            "把被封印的\x01",
            "那些家伙救出来之后，\x01",
            "赶快离开这个奇怪的世界吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x109, 400)

    ChrTalk(    #330
        0x1D,
        (
            "#050F喂，神父，把我带上吧。\x02\x03",

            "我才不管异空间\x01",
            "还是影之王什么的，\x01",
            "目前得赶快把这里的状况摸清才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x109,
        (
            "#1066F不、不愧是阿加特。\x01",
            "干劲真是满满的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 224, 0)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2631)

    label("loc_AB89")

    Jump("loc_AC52")

    label("loc_AB8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABE6")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #332
        0x1D,
        (
            "#555F哦，哦…………\x02\x03",

            "原、原来如此……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_AC52")

    label("loc_ABE6")

    TalkBegin(0xFE)

    ChrTalk(    #333
        0x1D,
        (
            "#053F在这种地方呆着\x01",
            "也没什么事情做。\x02\x03",

            "#051F……让我一起去吧。\x01",
            "也好把握现在的状况。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_AC52")

    Return()

    # Function_8_8A36 end

    def Function_9_AC53(): pass

    label("Function_9_AC53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_B0D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF92")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE25")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #334
        0x12,
        (
            "#066F其实他本来是很尊敬\x01",
            "卡西乌斯叔叔的……\x02\x03",

            "#562F阿、阿加特大哥哥\x01",
            "他真是太不直率了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD36")

    ChrTalk(    #335
        0x101,
        (
            "#1028F（说的没错啊……#1490W \x01",
            "  #20W…………阿加特？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADF6")

    label("loc_AD36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8A")

    ChrTalk(    #336
        0x103,
        (
            "#1535F（确实如此呢……#1740W \x01",
            "  #20W…………阿加特？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADF6")

    label("loc_AD8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADC9")

    ChrTalk(    #337
        0x10A,
        "#816F（说的没错呢，阿加特前辈！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADF6")

    label("loc_ADC9")


    ChrTalk(    #338
        0x109,
        "#1840F（说的没错啊，阿加特……）\x02",
    )

    CloseMessageWindow()

    label("loc_ADF6")


    ChrTalk(    #339
        0x106,
        "#055F（别、别都这样看着我啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF84")

    label("loc_AE25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 1)), scpexpr(EXPR_END)), "loc_AEE6")

    ChrTalk(    #340
        0x12,
        (
            "#066F……阿加特大哥哥\x01",
            "因为能够和卡西乌斯叔叔战斗\x01",
            "而感到非常高兴。\x02\x03",

            "#564F不过，他又说下次见到真人\x01",
            "一定要好好揍他一顿……\x02\x03",

            "#562F男生为什么\x01",
            "都是这个样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF84")

    label("loc_AEE6")


    ChrTalk(    #341
        0x12,
        (
            "#060F……阿加特大哥哥\x01",
            "好像很想和\x01",
            "卡西乌斯叔叔交手。\x02\x03",

            "#063F……本来应该是很尊敬\x01",
            "卡西乌斯叔叔的……\x02\x03",

            "#562F男生为什么\x01",
            "都是这个样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF84")

    OP_A2(0x1)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_B0D3")

    label("loc_AF92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B03D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #342
        0x12,
        (
            "#066F本来应该是很尊敬\x01",
            "卡西乌斯叔叔的……\x02\x03",

            "#562F阿加特大哥哥真是的，\x01",
            "真是太不直率了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x106,
        "#551F（别、别跟我说话……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0CB")

    label("loc_B03D")

    TalkBegin(0xFE)

    ChrTalk(    #344
        0x12,
        (
            "#063F其实他本来是很尊敬\x01",
            "卡西乌斯叔叔的……\x02\x03",

            "#063F却总是说要\x01",
            "决一胜负什么的……\x02\x03",

            "#562F男生为什么\x01",
            "都是这个样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0CB")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_B0D3")

    Jump("loc_D1E7")

    label("loc_B0D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_B2F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1DA")
    TalkBegin(0xFE)

    ChrTalk(    #345
        0x12,
        (
            "#060F雾香姐姐回国的时候，\x01",
            "好像是爷爷出去旅行\x01",
            "之前不久的事情。\x02\x03",

            "#564F有一天突然来到我家，\x01",
            "说差不多该休假了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1A7")

    ChrTalk(    #346
        0x101,
        "#1016F真、真像雾香姐姐的作风……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1D1")

    label("loc_B1A7")


    ChrTalk(    #347
        0x109,
        (
            "#1066F哈哈，\x01",
            "真是活灵活现……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1D1")

    OP_A2(0x1)
    TalkEnd(0xFE)
    Jump("loc_B2F1")

    label("loc_B1DA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #348
        0x12,
        (
            "#064F啊，对了。\x01",
            "我都忘记了……\x02\x03",

            "#063F玛多克叔叔没关系吗……\x02\x03",

            "这次又是因为妈妈的研究\x01",
            "而引起了事故……\x02\x03",

            "总能来帮助收拾局面的雾香姐姐\x01",
            "现在也不在这里了……\x02\x03",

            "#561F玛多克叔叔\x01",
            "现在也许早就晕倒了也说不定……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_B2F1")

    Jump("loc_D1E7")

    label("loc_B2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_B805")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B38B")
    Jump("loc_B3CD")

    label("loc_B38B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3A7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B3CD")

    label("loc_B3A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3C3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B3CD")

    label("loc_B3C3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B3CD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B764")
    OP_A2(0x1)

    ChrTalk(    #349
        0x12,
        (
            "#563F#40W………………………………\x02\x03",

            "#562F………嗯……………………\x01",
            "………………呼…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #350
        0x12,
        "#064F呵啊…………！？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    SetChrChipByIndex(0xFE, 39)
    Sleep(800)

    ChrTalk(    #351
        0x12,
        "#0562F#40W………………嗯嗯…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#1016F（啊哈哈……\x01",
            "  好像在睡觉呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x10F,
        (
            "#1448F（提妲是第一个从\x01",
            "  封印石里面解放出来的。）\x02\x03",

            "（体力差不多\x01",
            "  也该到极限了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B62A")

    ChrTalk(    #354
        0x106,
        (
            "#556F（……没办法，\x01",
            "  让她稍微休息一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        "#1000F（嗯，没错。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B761")

    label("loc_B62A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B698")

    ChrTalk(    #356
        0x102,
        (
            "#1501F（……艾丝蒂尔，\x01",
            "  让她稍微休息一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        "#1000F（嗯，没错。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B761")

    label("loc_B698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B706")

    ChrTalk(    #358
        0x105,
        (
            "#1165F（……艾丝蒂尔，\x01",
            "  让她稍微休息一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1000F（嗯，没错。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B761")

    label("loc_B706")


    ChrTalk(    #360
        0x101,
        (
            "#1006F（那就没办法了。\x01",
            "  让她稍微休息一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x10F,
        "#1447F（……好。）\x02",
    )

    CloseMessageWindow()

    label("loc_B761")

    Jump("loc_B7FA")

    label("loc_B764")


    ChrTalk(    #362
        0x12,
        (
            "#562F#40W………嗯……………………\x01",
            "………………唔…………\x02\x03",

            "#067F#20W……嘿、嘿嘿……………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x10F,
        "#1442F（……真可爱…………）\x02",
    )

    CloseMessageWindow()

    label("loc_B7FA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_B805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 2)), scpexpr(EXPR_END)), "loc_B9DA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B932")

    ChrTalk(    #364
        0x12,
        (
            "#564F我也很担心凯文哥哥的情况……\x02\x03",

            "#063F『影之王』先生\x01",
            "似乎已经预测到凯文哥哥\x01",
            "会在使用『圣痕』之后倒下。\x02\x03",

            "还说如果那样的话\x01",
            "『影之国』就会接近完成……\x02\x03",

            "#561F那个，如果继续向前探索的话，\x01",
            "一定要更加注意才行啊。\x02\x03",

            "我不想再看到\x01",
            "有谁受伤了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B9D4")

    label("loc_B932")


    ChrTalk(    #365
        0x12,
        (
            "#063F至今为止，\x01",
            "『影之王』先生好像没有\x01",
            "直接加害过别人……\x02\x03",

            "但现在看来好像不是这样。\x02\x03",

            "#062F如果继续向前探索的话，\x01",
            "一定要更加注意才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9D4")

    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_B9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_BD42")
    TalkBegin(0xFE)
    TurnDirection(0x12, 0x101, 0)

    ChrTalk(    #366
        0x12,
        (
            "#064F啊，艾丝蒂尔姐姐。\x02\x03",

            "#063F那个，凯文哥哥的情况怎么样……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAA2")

    ChrTalk(    #367
        0x101,
        (
            "#1000F嗯，应该没事了。\x02\x03",

            "#1016F现在乔丝特\x01",
            "正在照顾他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA7")

    label("loc_BAA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAFC")

    ChrTalk(    #368
        0x101,
        (
            "#1012F嗯，应该没事了。\x02\x03",

            "#1000F现在科洛丝\x01",
            "正在照顾他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA7")

    label("loc_BAFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB56")

    ChrTalk(    #369
        0x101,
        (
            "#1000F嗯，应该没事了。\x02\x03",

            "#1012F现在约修亚\x01",
            "正在照顾他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA7")

    label("loc_BB56")


    ChrTalk(    #370
        0x101,
        (
            "#1000F嗯，应该没事了。\x02\x03",

            "#1012F现在约修亚和科洛丝\x01",
            "正在照顾他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA7")


    ChrTalk(    #371
        0x12,
        (
            "#066F是、是吗……\x02\x03",

            "#561F呼，太好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #372
        0x10F,
        (
            "#1440F那、那个……\x02\x03",

            "#1445F……抱歉。\x01",
            "让你们担心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x12, 0x10F, 300)
    Sleep(500)

    ChrTalk(    #373
        0x12,
        "#064F哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10F, 300)

    ChrTalk(    #374
        0x101,
        (
            "#1015F嗯……\x01",
            "为什么莉丝姐姐要道歉呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x10F,
        (
            "#1440F…………………………#1050W \x01",
            "#20W是啊。\x02\x03",

            "#1446F把刚才我说的忘掉吧。\x02",
        )
    )

    Jump("loc_BD19")

    label("loc_BD19")

    CloseMessageWindow()

    ChrTalk(    #376
        0x101,
        "#1016F忘、忘掉……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2632)
    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_BD42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 1)), scpexpr(EXPR_END)), "loc_BFA8")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDE3")

    ChrTalk(    #377
        0x12,
        (
            "#560F那、那个……\x01",
            "这个地方……\x02\x03",

            "与『里塔』平坦的\x01",
            "次元空间不同，\x01",
            "这个异空间竟然是多层构造……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEB7")

    label("loc_BDE3")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #378
        0x106,
        (
            "#051F提妲，\x01",
            "你在这里稍微等一会儿。\x02\x03",

            "我去看看这个所谓的\x01",
            "异空间的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x12,
        (
            "#560F啊，好的。\x02\x03",

            "#067F那个那个，\x01",
            "一定要注意安全啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x106,
        "#051F这个就不用你提醒啦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 245, 0)

    label("loc_BEB7")

    OP_A2(0x1)
    Jump("loc_BF99")

    label("loc_BEBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF1C")

    ChrTalk(    #381
        0x12,
        (
            "#560F与『里塔』平坦的\x01",
            "次元空间不同，\x01",
            "这个异空间竟然是多层构造……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF99")

    label("loc_BF1C")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #382
        0x106,
        (
            "#051F……我去看看这个所谓的\x01",
            "异空间的情况。\x02\x03",

            "提妲，你就呆在这里看家吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x12,
        "#067F是！\x02",
    )

    Jump("loc_BF98")

    label("loc_BF98")

    CloseMessageWindow()

    label("loc_BF99")

    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D1E7")

    label("loc_BFA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_C5C3")
    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)
    OP_4A(0x1D, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2BC")

    ChrTalk(    #384
        0x12,
        (
            "#067F可是可是，\x01",
            "阿加特大哥哥没事真是太好了。\x02\x03",

            "#560F我一直害怕\x01",
            "万一阿加特大哥哥也遇到危险，\x01",
            "所以担心得不得了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x1D,
        (
            "#551F我都说啦，\x01",
            "你就别这样搂着我了。\x02\x03",

            "#050F反倒是提妲，\x01",
            "你…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #386
        0x1D,
        (
            "#552F……在我没注意到的地方，\x01",
            "是不是又遇到什么危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x12,
        (
            "#565F那个…………\x02\x03",

            "没、没什么事啦。\x02\x03",

            "#067F反正是和凯文哥哥\x01",
            "他们一起行动…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x1D,
        (
            "#053F是吗…………\x02\x03",

            "#051F那我就不多说了。\x02\x03",

            "把被封印的\x01",
            "那些家伙救出来之后，\x01",
            "赶快离开这个奇怪的世界吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x109, 400)
    Sleep(500)

    ChrTalk(    #389
        0x1D,
        (
            "#050F喂，神父，把我带上吧。\x02\x03",

            "我才不管异空间\x01",
            "还是影之王什么的，\x01",
            "目前得赶快把这里的状况摸清才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x1D, 400)

    ChrTalk(    #390
        0x109,
        (
            "#1066F不、不愧是阿加特。\x01",
            "干劲真是满满的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x12, 400)
    Jump("loc_C5B1")

    label("loc_C2BC")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #391
        0x12,
        (
            "#067F可是可是，\x01",
            "阿加特大哥哥没事真是太好了。\x02\x03",

            "#560F我一直害怕\x01",
            "万一阿加特大哥哥也遇到危险，\x01",
            "所以担心得不得了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x106,
        (
            "#551F所以啦，\x01",
            "你就别这样搂着我了。\x02\x03",

            "#050F反倒是提妲，\x01",
            "你…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #393
        0x106,
        (
            "#552F……在我没注意到的地方，\x01",
            "是不是又遇到什么危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x12,
        (
            "#565F那个…………\x02\x03",

            "没、没什么事啦。\x02\x03",

            "#067F反正是和凯文哥哥\x01",
            "他们一起行动…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x106,
        (
            "#053F是吗…………\x02\x03",

            "#051F那我就不多说了。\x02\x03",

            "把被封印的\x01",
            "那些家伙救出来之后，\x01",
            "赶快离开这个奇怪的世界吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x109, 400)
    Sleep(500)

    ChrTalk(    #396
        0x106,
        (
            "#050F喂，神父，赶快出发吧。\x02\x03",

            "我才不管异空间\x01",
            "还是影之王什么的，\x01",
            "目前得赶快把这里的状况摸清才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x106, 400)

    ChrTalk(    #397
        0x109,
        (
            "#1066F不、不愧是阿加特。\x01",
            "干劲真是满满的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 245, 0)

    label("loc_C5B1")

    OP_A2(0x2631)
    OP_4B(0x1D, 255)
    TalkEnd(0x12)
    SetChrFlags(0x12, 0x10)
    Jump("loc_D1E7")

    label("loc_C5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_C835")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C65A")
    Jump("loc_C69C")

    label("loc_C65A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C676")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C69C")

    label("loc_C676")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C692")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C69C")

    label("loc_C692")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C69C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C794")

    ChrTalk(    #398
        0x12,
        (
            "#062F因为是靠传送阵和方石的力量来进行移动，\x01",
            "所以根本搞不清方向……\x02\x03",

            "不过这个『星层』\x01",
            "似乎是越往深处前进\x01",
            "就越靠下的感觉。\x02\x03",

            "#065F这、这样的话……\x01",
            "最下面到底有什么东西呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C82A")

    label("loc_C794")


    ChrTalk(    #399
        0x12,
        (
            "#063F关于『规则』\x01",
            "已经差不多明白了……\x02\x03",

            "#561F但是『影之国』的谜题\x01",
            "还基本上都没有解开。\x02\x03",

            "『影之王』先生\x01",
            "到底打算干什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C82A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_C835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_CA57")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9DC")

    ChrTalk(    #400
        0x12,
        (
            "#560F嘿嘿，不过，真是太好了……\x02\x03",

            "能够把约修亚哥哥\x01",
            "成功解救出来……\x02\x03",

            "#063F不过，\x01",
            "艾丝蒂尔姐姐很有可能\x01",
            "也被卷入到这里面来了。\x02\x03",

            "要赶快找到她，\x01",
            "把她解救出来才行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9D6")
    TurnDirection(0x12, 0x10D, 400)
    Sleep(300)

    ChrTalk(    #401
        0x12,
        "#063F啊，还有奥利维尔先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x10D,
        (
            "#270F嗯………………？\x02\x03",

            "#278F啊啊，你不用担心。\x02\x03",

            "#277F这种程度的觉悟他还是有的。\x01",
            "才不会因为被封印起来而消沉的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9D6")

    OP_A2(0x1)
    Jump("loc_CA51")

    label("loc_C9DC")


    ChrTalk(    #403
        0x12,
        (
            "#063F果然，\x01",
            "封印石会把吸进去的人\x01",
            "都封印起来。\x02\x03",

            "#062F不、不赶快找到大家，\x01",
            "把大家解救出来就糟了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA51")

    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_CA57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_CCCD")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CAEE")
    Jump("loc_CB30")

    label("loc_CAEE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB0A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB30")

    label("loc_CB0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB26")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB30")

    label("loc_CB26")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB30")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC43")

    ChrTalk(    #404
        0x12,
        (
            "#063F关于这个异空间，\x01",
            "我觉得还是能够解释的。\x02\x03",

            "在塞姆里亚时期，\x01",
            "人们似乎掌握着制作『里塔』\x01",
            "那样的异空间的技术……\x02\x03",

            "#562F但是，能把人吸进来的封印石，\x01",
            "以及那个奇怪的王都，\x01",
            "实在是想象不出其中的原理……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_CCC2")

    label("loc_CC43")


    ChrTalk(    #405
        0x12,
        (
            "#063F那、那个…………\x02\x03",

            "#561F果然\x01",
            "不明白的东西还是太多了。\x02\x03",

            "如果能找到\x01",
            "更多一点的线索就好了……\x02",
        )
    )

    Jump("loc_CCC1")

    label("loc_CCC1")

    CloseMessageWindow()

    label("loc_CCC2")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_CCCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 0)), scpexpr(EXPR_END)), "loc_CF35")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CD64")
    Jump("loc_CDA6")

    label("loc_CD64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD80")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CDA6")

    label("loc_CD80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD9C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CDA6")

    label("loc_CD9C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CDA6")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEA9")

    ChrTalk(    #406
        0x12,
        (
            "#063F……古代遗物………\x01",
            "异空间……封、封印石………？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #407
        0x12,
        "#562F………唔、唔………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x10F,
        "#1440F……也许是肚子饿了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x109,
        "#1068F不，才不会呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_CF2A")

    label("loc_CEA9")


    ChrTalk(    #410
        0x12,
        (
            "#063F……古代遗物………\x01",
            "异空间……封、封印石………？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #411
        0x12,
        "#562F………唔、唔………\x02",
    )

    CloseMessageWindow()

    label("loc_CF2A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_D1E7")

    label("loc_CF35")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CFC5")
    Jump("loc_D007")

    label("loc_CFC5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CFE1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D007")

    label("loc_CFE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFFD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D007")

    label("loc_CFFD")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D007")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #412
        0x12,
        "#064F哎…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x109,
        (
            "#1079F怎么了，提妲。\x02\x03",

            "…………你没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x12,
        (
            "#060F啊……是、是的。\x02\x03",

            "对不起，\x01",
            "我刚才在发呆……\x02\x03",

            "#561F因为不明白的事情太多了，\x01",
            "所以…………\x02",
        )
    )

    Jump("loc_D10A")

    label("loc_D10A")

    CloseMessageWindow()

    ChrTalk(    #415
        0x109,
        (
            "#1060F嗯，没关系。\x01",
            "我也是一头雾水呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x12,
        (
            "#064F啊，不过不过，\x01",
            "我会努力的！\x02\x03",

            "#62F探索的时候\x01",
            "尽管把我带上吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x109,
        "#1066F知、知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x10F,
        "#1440F………………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2630)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_D1E7")

    Return()

    # Function_9_AC53 end

    def Function_10_D1E8(): pass

    label("Function_10_D1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_D2F4")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2AB")

    ChrTalk(    #419
        0x1B,
        "#812F喝啊啊…………！！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2A5")

    ChrTalk(    #420
        0x101,
        (
            "#1002F（真厉害的气势………………）\x02\x03",

            "#1006F（唔……\x01",
            "  这样的话，\x01",
            "  我作为对手也不能认输啊……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A5")

    OP_A2(0xA)
    Jump("loc_D2E9")

    label("loc_D2AB")


    ChrTalk(    #421
        0x1B,
        (
            "#812F还没有…………\x02\x03",

            "#815F还没有结束……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2E9")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_E9D2")

    label("loc_D2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_D967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7F0")
    SetChrFlags(0x1B, 0x10)
    TalkBegin(0x1B)

    ChrTalk(    #422
        0x1B,
        (
            "#813F唔………\x02\x03",

            "#1312F唔…………！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #423
        0x101,
        (
            "#1011F那个，亚妮拉丝……？\x02\x03",

            "#1020F怎、怎么了……！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3F2")

    ChrTalk(    #424
        0x103,
        (
            "#1525F……亚妮拉丝，\x01",
            "你又在做这个啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1026F做、做什么……？\x02",
    )

    CloseMessageWindow()

    label("loc_D3F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D470")
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #426
        0x103,
        (
            "#1526F……哎呀，\x01",
            "刚才玲不是说了吗。\x02\x03",

            "#1522F这个世界也许\x01",
            "会根据人们的愿望而改变……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D6")

    label("loc_D470")


    ChrTalk(    #427
        0x1C,
        (
            "#1526F……哎呀，\x01",
            "刚才玲不是说了吗。\x02\x03",

            "#1522F这个世界也许\x01",
            "会根据人们的愿望而改变……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D6")


    ChrTalk(    #428
        0x101,
        (
            "#1026F嗯、嗯。\x01",
            "那个倒是听说过……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D54F")

    ChrTalk(    #429
        0x103,
        (
            "#1525F所以这孩子正在努力\x01",
            "打算变出布娃娃来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D589")

    label("loc_D54F")


    ChrTalk(    #430
        0x1C,
        (
            "#1525F所以这孩子正在努力\x01",
            "打算变出布娃娃来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D589")

    Sleep(300)
    TurnDirection(0x1B, 0x0, 400)

    ChrTalk(    #431
        0x1B,
        (
            "#812F等一下，\x01",
            "你们能不能安静一下呢！\x02\x03",

            "我会无法集中精力的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5FB")
    TurnDirection(0x103, 0x1B, 0)
    Jump("loc_D600")

    label("loc_D5FB")

    SetChrSubChip(0x1C, 0)

    label("loc_D600")

    OP_8C(0x1B, 316, 400)
    Sleep(300)
    OP_62(0x1B, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(    #432
        0x1B,
        (
            "#811F天使羊波波的\x01",
            "圆眼睛。\x02\x03",

            "可爱熊宝宝，\x01",
            "还有绒毛熊……\x02\x03",

            "#1311F嘿嘿～……\x01",
            "到底要哪一个呢……㈱\x02",
        )
    )

    Jump("loc_D6A2")

    label("loc_D6A2")

    CloseMessageWindow()
    OP_63(0x1B)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D76F")
    Sleep(1000)

    ChrTalk(    #433
        0x103,
        (
            "#1526F……我说，\x01",
            "你的杂念也太多了吧？\x02\x03",

            "#1534F还是集中精力想一个吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E2")

    label("loc_D76F")

    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #434
        0x1C,
        (
            "#1526F……我说，\x01",
            "你的杂念也太多了吧？\x02\x03",

            "#1534F还是集中精力想一个吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7E2")

    OP_A2(0x264D)
    TalkEnd(0x1B)
    ClearChrFlags(0x1B, 0x10)
    Jump("loc_D964")

    label("loc_D7F0")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8D7")
    OP_A2(0xA)

    ChrTalk(    #435
        0x1B,
        (
            "#811F天使羊波波的\x01",
            "圆眼睛。\x02\x03",

            "可爱熊宝宝，\x01",
            "还有绒毛熊……\x02\x03",

            "#1311F嘿嘿～……\x01",
            "到底要哪一个呢……㈱\x02",
        )
    )

    Jump("loc_D887")

    label("loc_D887")

    CloseMessageWindow()

    ChrTalk(    #436
        0x101,
        (
            "#1019F……就算没有『福音』之类的东西，\x01",
            "我也觉得已经很幸福了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D95C")

    label("loc_D8D7")


    ChrTalk(    #437
        0x1B,
        (
            "#811F天使羊波波的\x01",
            "圆眼睛。\x02\x03",

            "可爱熊宝宝，\x01",
            "还有绒毛熊……\x02\x03",

            "#1311F嘿嘿～……\x01",
            "到底要哪一个呢……㈱\x02",
        )
    )

    Jump("loc_D95B")

    label("loc_D95B")

    CloseMessageWindow()

    label("loc_D95C")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_D964")

    Jump("loc_E9D2")

    label("loc_D967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_E316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1EE")
    TalkBegin(0xFE)
    OP_4A(0x1D, 255)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE0D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9CA")

    ChrTalk(    #438
        0x1B,
        "#814F啊，是艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9EA")

    label("loc_D9CA")


    ChrTalk(    #439
        0x1B,
        "#814F啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    label("loc_D9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA5F")

    ChrTalk(    #440
        0x106,
        (
            "#053F……亚妮拉丝，\x01",
            "刚才我听雪拉扎德说了……\x02\x03",

            "#051F你是不是和这个上校\x01",
            "交过手啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DABA")

    label("loc_DA5F")


    ChrTalk(    #441
        0x1D,
        (
            "#051F你听说了吗，艾丝蒂尔。\x02\x03",

            "#051F……这家伙，\x01",
            "好像和那个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DABA")


    ChrTalk(    #442
        0x101,
        "#1004F哎，是真的吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x1B,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x10C,
        (
            "#111F那是卡西乌斯准将的安排。\x02\x03",

            "#110F让我能有机会再次\x01",
            "拿起这远未成熟的剑。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC1C")

    ChrTalk(    #445
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x102,
        (
            "#1500F嗯，四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC9A")

    label("loc_DC1C")


    ChrTalk(    #447
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02\x03",

            "四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    Jump("loc_DC99")

    label("loc_DC99")

    CloseMessageWindow()

    label("loc_DC9A")


    ChrTalk(    #448
        0x10C,
        (
            "#118F哈哈，现在想起来，\x01",
            "只有不堪回首的记忆而已……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD58")
    TurnDirection(0x106, 0x10C, 400)

    ChrTalk(    #449
        0x106,
        (
            "#051F哼，你的剑法\x01",
            "是得自卡西乌斯大叔的直传吧？\x02\x03",

            "有机会的话，\x01",
            "我也想和你切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC6")

    label("loc_DD58")

    TurnDirection(0x1D, 0x10C, 400)

    ChrTalk(    #450
        0x1D,
        (
            "#051F哼，你的剑法\x01",
            "是得自卡西乌斯大叔的直传吧？\x02\x03",

            "有机会的话，\x01",
            "我也想和你切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC6")


    ChrTalk(    #451
        0x10C,
        (
            "#495F（哎呀，你这么看得起我\x01",
            "  我也很难办啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 136, 0)
    Jump("loc_E1DD")

    label("loc_DE0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE48")

    ChrTalk(    #452
        0x1B,
        "#814F啊，是艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE68")

    label("loc_DE48")


    ChrTalk(    #453
        0x1B,
        "#814F啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    label("loc_DE68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEDD")

    ChrTalk(    #454
        0x106,
        (
            "#053F……亚妮拉丝，\x01",
            "刚才我听雪拉扎德说了……\x02\x03",

            "#051F你是不是和那个上校\x01",
            "交过手啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF33")

    label("loc_DEDD")


    ChrTalk(    #455
        0x1D,
        (
            "#051F你听说了吗，艾丝蒂尔。\x02\x03",

            "……这家伙，\x01",
            "好像和那个上校交过手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF33")


    ChrTalk(    #456
        0x101,
        "#1004F哎，是真的吗……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF92")

    ChrTalk(    #457
        0x103,
        (
            "#1525F我听说的时候\x01",
            "也很吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF92")


    ChrTalk(    #458
        0x1B,
        (
            "#819F嘿嘿，稍微有一些事情啦……\x02\x03",

            "反正就是顺便\x01",
            "打了一场。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E072")

    ChrTalk(    #459
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x102,
        (
            "#1500F嗯，四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0F0")

    label("loc_E072")


    ChrTalk(    #461
        0x101,
        (
            "#1017F是、是这样啊。\x02\x03",

            "#1015F说起来，\x01",
            "我们也曾经战斗过一次……\x02\x03",

            "四对一\x01",
            "好不容易才取胜的……\x02",
        )
    )

    Jump("loc_E0EF")

    label("loc_E0EF")

    CloseMessageWindow()

    label("loc_E0F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E16F")

    ChrTalk(    #462
        0x106,
        (
            "#053F那家伙的剑法\x01",
            "是得自卡西乌斯大叔的直传……\x02\x03",

            "#051F哼，有机会的话\x01",
            "我也想和他切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1DD")

    label("loc_E16F")


    ChrTalk(    #463
        0x1D,
        (
            "#053F那家伙的剑法\x01",
            "是得自卡西乌斯大叔的直传……\x02\x03",

            "#051F哼，有机会的话\x01",
            "我也想和他切磋一番呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1DD")

    OP_4B(0x1D, 255)
    OP_4B(0x1B, 255)
    OP_A2(0x264E)
    TalkEnd(0xFE)
    Jump("loc_E313")

    label("loc_E1EE")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2AA")

    ChrTalk(    #464
        0x1B,
        (
            "#818F唔，不过在那之后\x01",
            "我也又变强了一些……\x02\x03",

            "如果能和上校\x01",
            "再切磋一次就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2A4")

    ChrTalk(    #465
        0x10C,
        (
            "#495F（哎呀，\x01",
            "  都说我已经不是上校了……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2A4")

    OP_A2(0xA)
    Jump("loc_E30B")

    label("loc_E2AA")


    ChrTalk(    #466
        0x1B,
        (
            "#818F唔，不过在那之后\x01",
            "我也又变强了一些……\x02\x03",

            "如果能和上校\x01",
            "再切磋一次就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E30B")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_E313")

    Jump("loc_E9D2")

    label("loc_E316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_E7D8")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E3AD")
    Jump("loc_E3EF")

    label("loc_E3AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E3C9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3EF")

    label("loc_E3C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3E5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3EF")

    label("loc_E3E5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3EF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E753")

    ChrTalk(    #467
        0x1B,
        (
            "#814F啊，莉丝。\x01",
            "你的伤已经好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x10F,
        (
            "#1448F嗯，没有问题了。\x01",
            "因为避开了直接袭击。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 5)), scpexpr(EXPR_END)), "loc_E4D8")

    ChrTalk(    #469
        0x1B,
        (
            "#819F嘿嘿，不过，\x01",
            "你还是来帮忙了呢。\x02\x03",

            "#816F真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E512")

    label("loc_E4D8")


    ChrTalk(    #470
        0x1B,
        (
            "#819F嘿嘿，不过，\x01",
            "你果然去帮\x01",
            "凯文先生他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E512")


    ChrTalk(    #471
        0x10F,
        (
            "#1446F……亚妮拉丝。\x01",
            "你说的事，我仔细考虑过了。\x02\x03",

            "#1440F就像凯文以骑士为目标那样，\x01",
            "我作为随从骑士，\x01",
            "来到这里也是有相应的理由的。\x02\x03",

            "#1448F所以…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x1B,
        (
            "#810F……是吗。\x02\x03",

            "#1310F嗯，\x01",
            "接下来就等凯文先生醒了之后，\x01",
            "去好好跟他谈谈吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x10F,
        (
            "#1442F……好的。\x02\x03",

            "#1806F那个，真是谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x1B,
        "#811F呵呵，没关系啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x101,
        (
            "#1015F那个…………\x02\x03",

            "#1011F亚妮拉丝，\x01",
            "你和莉丝还真是要好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x1B,
        (
            "#1311F嘿嘿，理由很简单嘛。\x02\x03",

            "#815F#3S因为莉丝\x01",
            "太可爱了！！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x101,
        "#1016F是、是吗，我明白了…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x265E)
    Jump("loc_E7CD")

    label("loc_E753")


    ChrTalk(    #478
        0x1B,
        (
            "#810F嗯，\x01",
            "艾丝蒂尔也被顺利解救出来了……\x02\x03",

            "#1310F如果凯文先生\x01",
            "能够醒过来，\x01",
            "就能暂时放心一阵子了。\x02",
        )
    )

    Jump("loc_E7CC")

    label("loc_E7CC")

    CloseMessageWindow()

    label("loc_E7CD")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_E9D2")

    label("loc_E7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_E9D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E924")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E888")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #479
        0x1B,
        (
            "#814F啊，雪拉前辈。\x02\x03",

            "#810F你和莉丝见过面了吗？\x02\x03",

            "#811F嘿嘿，虽然性格有点奇怪，\x01",
            "不过她也是个很有趣的人呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E91E")

    label("loc_E888")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #480
        0x1B,
        (
            "#816F雪拉前辈，\x01",
            "我们到那边的书架去吧。\x02\x03",

            "那边有个\x01",
            "看起来怪怪的修女……\x02\x03",

            "#1311F不过还真是可爱呢。\x02",
        )
    )

    Jump("loc_E915")

    label("loc_E915")

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_E91E")

    OP_A2(0xA)
    Jump("loc_E9D2")

    label("loc_E924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E99A")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #481
        0x1B,
        (
            "#818F虽然莉丝\x01",
            "性格有点怪怪的……\x02\x03",

            "#811F不过，\x01",
            "还真是个可爱的修女呢！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E9D2")

    label("loc_E99A")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #482
        0x1B,
        "#812F雪拉前辈，你在听吗～？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_E9D2")

    Return()

    # Function_10_D1E8 end

    def Function_11_E9D3(): pass

    label("Function_11_E9D3")

    EventBegin(0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1E, 14)
    SetChrSubChip(0x1E, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x16, 6)
    SetChrSubChip(0x16, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x1E, -52160, 1000, -31820, 135)
    SetChrPos(0x16, -52770, 1000, -32640, 135)
    SetChrPos(0xEE, -50000, 1000, -32990, 270)
    SetChrPos(0xEF, -50800, 1000, -34830, 328)
    SetChrPos(0xF0, -49170, 1000, -35040, 300)
    SetChrPos(0xF1, -48960, 1000, -33690, 300)
    SetChrPos(0x109, -51280, 1000, -33640, 322)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-51810, 1000, -32700, 0)
    OP_67(0, 7730, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EACB")
    SetChrFlags(0x101, 0x8)

    label("loc_EACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EADE")
    SetChrFlags(0x102, 0x8)

    label("loc_EADE")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #483
        (
            "\x07\x05凯文把黑耀石石碑上\x01",
            "记述的语句向约修亚作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_EB34")

    label("loc_EB34")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #484
        0x16,
        (
            "#1505F……………………………\x02\x03",

            "……看来，『黑骑士』\x01",
            "就在这最后的领域中啊。\x02\x03",

            "#1503F而且不知为何，\x01",
            "故意点了我的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x109,
        (
            "#1065F#12P啊啊……看来是这样。\x02\x03",

            "#1063F约修亚。\x01",
            "你打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x16,
        (
            "#1505F那还用说……\x01",
            "当然是接受招待了。\x02\x03",

            "#1502F我已经做好准备了，\x01",
            "随时可以加入你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x1E,
        "#1003F约修亚……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECD5")

    ChrTalk(    #488
        0x10B,
        "#215F哎，那个……\x02",
    )

    CloseMessageWindow()

    label("loc_ECD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED00")

    ChrTalk(    #489
        0x105,
        "#1163F约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_ED00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED2C")

    ChrTalk(    #490
        0x107,
        "#063F哥、哥哥……\x02",
    )

    CloseMessageWindow()

    label("loc_ED2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED59")

    ChrTalk(    #491
        0x110,
        "#1300F……约修亚。\x02",
    )

    CloseMessageWindow()

    label("loc_ED59")


    ChrTalk(    #492
        0x16,
        (
            "#1513F……没关系。\x01",
            "不管发生什么都无所谓。\x02\x03",

            "#1500F总之……\x01",
            "现在只需考虑如何前进。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B22)
    Fade(500)
    EventEnd(0x5)
    OP_4F(0x64, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_67(0, 3620, -10000, 0)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_44(0x1E, 0x0)
    SetChrFlags(0x1E, 0x4)
    SetChrPos(0x1E, -54150, 2000, -29940, 135)
    SetChrChipByIndex(0x16, 29)
    SetChrSubChip(0x16, 0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -54720, 2000, -30720, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE3A")
    SetChrFlags(0x1E, 0x80)

    label("loc_EE3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE4D")
    SetChrFlags(0x16, 0x80)

    label("loc_EE4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE60")
    ClearChrFlags(0x101, 0x8)

    label("loc_EE60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE73")
    ClearChrFlags(0x102, 0x8)

    label("loc_EE73")

    Return()

    # Function_11_E9D3 end

    SaveToFile()

Try(main)
