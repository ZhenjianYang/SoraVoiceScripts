from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7003_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
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
        "Function_3_11DF",         # 03, 3
        "Function_4_1720",         # 04, 4
        "Function_5_2566",         # 05, 5
        "Function_6_38E9",         # 06, 6
        "Function_7_51C8",         # 07, 7
        "Function_8_5D33",         # 08, 8
        "Function_9_797E",         # 09, 9
        "Function_10_8D75",        # 0A, 10
        "Function_11_8FC2",        # 0B, 11
        "Function_12_A1B3",        # 0C, 12
        "Function_13_B6A2",        # 0D, 13
        "Function_14_EF96",        # 0E, 14
        "Function_15_EFE4",        # 0F, 15
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_4A0")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C1")

    ChrTalk(    #0
        0x11,
        (
            "#1936F…………………………\x02\x03",

            "……５年前的那一天，\x01",
            "救了我的人果然是\x01",
            "凯文和姐姐。\x02\x03",

            "#1938F不管结果如何……\x01",
            "凯文和姐姐都是我最重要的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    ChrTalk(    #1
        0x11,
        (
            "#1932F所以，\x01",
            "『影之王』一定要由我们来打倒。\x02\x03",

            "……这也是为了姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1075F嗯，说的没错。\x02\x03",

            "…………………………\x02\x03",

            "#1079F不过……\x01",
            "莉丝，你在干什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #3
        0x11,
        (
            "#1940F……保、保证足够的粮食\x01",
            "也是身在前线最重要的使命……\x02\x03",

            "…………你要是敢笑的话我就揍你。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6")

    label("loc_2C1")


    ChrTalk(    #4
        0x11,
        (
            "#1936F…………………………\x02\x03",

            "……５年前的那一天，\x01",
            "救了我的人果然是\x01",
            "凯文和姐姐。\x02\x03",

            "#1938F不管结果如何……\x01",
            "凯文和姐姐都是我最重要的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x11,
        (
            "#1932F所以，\x01",
            "『影之王』一定要由我们来打倒。\x02\x03",

            "#1932F……这也是为了姐姐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6")

    OP_A2(0x2665)
    Jump("loc_495")

    label("loc_3CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_439")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #6
        0x11,
        (
            "#1936F『影之王』\x01",
            "一定要由我们来打倒。\x02\x03",

            "#1932F……这也是为了姐姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_495")

    label("loc_439")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #7
        0x11,
        (
            "#1936F『影之王』\x01",
            "一定要由我们来打倒。\x02\x03",

            "#1932F……这也是为了姐姐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_495")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_11DE")

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_END)), "loc_6DB")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_581")

    label("loc_53F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_581")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_577")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_581")

    label("loc_577")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_581")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")

    ChrTalk(    #8
        0x11,
        (
            "#1446F……凯文，\x01",
            "进入紫苑之家必须要有我同行……\x02\x03",

            "#1801F难道………你是故意把我扔下的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1077F不，\x01",
            "……不是的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#1801F（盯着看）………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_6CB")

    label("loc_66A")


    ChrTalk(    #11
        0x11,
        (
            "#1446F……凯文，\x01",
            "进入紫苑之家必须要有我同行……\x02\x03",

            "#1801F………你不是故意的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CB")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_11DE")

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_A6D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(    #12
        0x109,
        "#1065F…………莉丝。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7BF")
    Jump("loc_801")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7DB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_801")

    label("loc_7DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_801")

    label("loc_7F7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_801")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Sleep(200)

    ChrTalk(    #13
        0x11,
        "#1802F哎…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1060F不好意思，\x01",
            "你跟我们走一趟好吗？\x02\x03",

            "#1075F一会儿我再解释……#2000W \x01",
            "#20W不，你来了就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#1440F………………………………\x02\x03",

            "#1446F……我知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_A5D")

    label("loc_90B")

    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99B")
    Jump("loc_9DD")

    label("loc_99B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DD")

    label("loc_9B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DD")

    label("loc_9D3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #16
        0x11,
        (
            "#1445F………………………………\x02\x03",

            "#1443F……我已经做好准备了。\x01",
            "一起走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5D")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_11DE")

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #17
        0x11,
        (
            "#1445F（『剑帝』莱恩哈特………）\x02\x03",

            "#1446F（……他好像知道\x01",
            "  姐姐的事情……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_B60")

    label("loc_B0A")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #18
        0x11,
        (
            "#1446F…………………………\x02\x03",

            "#1445F是这样吗…………\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_B60")

    Jump("loc_B67")

    label("loc_B63")

    Call(5, 8)

    label("loc_B67")

    Jump("loc_F3E")

    label("loc_B6A")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_C01")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #19
        0x11,
        (
            "#1447F#32W……精灵落下的水滴\x01",
            "在森林中被称为朝雾。\x02\x03",

            "在那泉水湖畔，\x01",
            "集齐了七只铃铛……#20W\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_D55")

    label("loc_C01")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C91")
    Jump("loc_CD3")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CAD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CD3")

    label("loc_CAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CD3")

    label("loc_CC9")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CD3")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #20
        0x11,
        (
            "#1448F……我来读一下\x01",
            "圣典中的故事吧。\x02\x03",

            "#1442F怎么说我也是个修女。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_D55")

    OP_A2(0xB)
    Jump("loc_F35")

    label("loc_D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_DE1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #21
        0x11,
        (
            "#1447F#32W……愿那两个清贫的人\x01",
            "得到安息的永眠。\x02\x03",

            "#1442F愿所有的生命\x01",
            "得到勇气和祝福。#20W\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_F35")

    label("loc_DE1")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E71")
    Jump("loc_EB3")

    label("loc_E71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E8D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EB3")

    label("loc_E8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EB3")

    label("loc_EA9")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EB3")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #22
        0x11,
        (
            "#1448F……我来读一下\x01",
            "圣典中的故事吧。\x02\x03",

            "#1442F怎么说我也是个修女。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_F35")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3E")

    Jump("loc_11DE")

    label("loc_F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_F4B")
    Jump("loc_11DE")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_106A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6C")
    Call(5, 13)
    Jump("loc_1067")

    label("loc_F6C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1011")

    ChrTalk(    #23
        0x11,
        "#1445F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1079F……莉丝，你怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        "#1446F………没什么。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0xB)
    Jump("loc_105F")

    label("loc_1011")


    ChrTalk(    #26
        0x11,
        (
            "#1445F………………………………\x02\x03",

            "（为什么凯文和姐姐都……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105F")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1067")

    Jump("loc_11DE")

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_11DE")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1154")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #27
        0x11,
        (
            "#1447F#40W………………………………#20W\x02\x03",

            "#1442F哦………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x0, 800)
    Sleep(200)

    ChrTalk(    #28
        0x11,
        "#1802F有………有什么事！？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_43(0xFE, 0x0, 0x0, 0xD)
    OP_A2(0xB)
    Jump("loc_11DE")

    label("loc_1154")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0x11,
        (
            "#1800F咳咳……\x02\x03",

            "圣典可以给所有的人\x01",
            "带来平安和宁静……\x02\x03",

            "#1805F如果可以的话，\x01",
            "我来为大家阅读一段吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_43(0xFE, 0x0, 0x0, 0xD)

    label("loc_11DE")

    Return()

    # Function_2_AC end

    def Function_3_11DF(): pass

    label("Function_3_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D0")
    TalkBegin(0xFE)

    ChrTalk(    #30
        0x1E,
        (
            "#1008F那个，\x01",
            "到达目的地还要很久吧？\x02\x03",

            "#1017F半路上肯定会饿的，\x01",
            "还是要准备必要的食品才好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #31
        0x10F,
        "#1932F…………真是我知心的朋友。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #32
        0x109,
        "#1066F哈哈哈…………\x02",
    )

    CloseMessageWindow()

    label("loc_12C7")

    OP_A2(0x7)
    TalkEnd(0xFE)
    Jump("loc_143B")

    label("loc_12D0")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #33
        0x1E,
        (
            "#1015F那个，赛雷斯托大人\x01",
            "好像不需要吃饭……\x02\x03",

            "嗯～１６人份吗……\x01",
            "还真多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1433")

    ChrTalk(    #34
        0x10F,
        (
            "#1932F……请带上１８人份的。\x02\x03",

            "#1938F我一个人要３人份。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x10F, 0)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #35
        0x1E,
        (
            "#1004F啊，是吗……\x02\x03",

            "#1006F……嗯，知道了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1433")

    ChrTalk(    #36
        0x109,
        (
            "#1068F（这两个人……\x01",
            "  都把基尔巴特那小子\x01",
            "  给忘得一干二净……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1433")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_143B")

    Jump("loc_171F")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_171F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153E")
    TalkBegin(0xFE)

    ChrTalk(    #37
        0x1E,
        (
            "#1008F啊，\x01",
            "我肚子有点饿了……\x02\x03",

            "#1019F只、只要一运动\x01",
            "肚子就会饿！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1538")

    ChrTalk(    #38
        0x10F,
        (
            "#1447F……没错。\x02\x03",

            "#1448F那个是真理。\x01",
            "谁也无法否认的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        "#1068F（这两个人还真是臭味相投……）\x02",
    )

    CloseMessageWindow()

    label("loc_1538")

    TalkEnd(0xFE)
    Jump("loc_167C")

    label("loc_153E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #40
        0x1E,
        (
            "#1007F真是的，那两个人啊……\x02\x03",

            "就没有办法让他们\x01",
            "相处得融洽一点吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FF")

    ChrTalk(    #41
        0x109,
        (
            "#1061F（哈哈，如果是艾丝蒂尔的话，\x01",
            "  倒是没什么问题……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_15FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_163B")

    ChrTalk(    #42
        0x10F,
        "#1440F………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_163B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #43
        0x110,
        "#1300F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1674")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_167C")

    OP_A2(0x7)
    Jump("loc_171F")

    label("loc_1682")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")

    ChrTalk(    #44
        0x1E,
        (
            "#1015F唔，喉咙干了……\x02\x03",

            "#1006F好，就吃冰淇淋吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1717")

    label("loc_16D9")


    ChrTalk(    #45
        0x1E,
        (
            "#1007F那两个人……\x02\x03",

            "好像还是不能和好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1717")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_171F")

    Return()

    # Function_3_11DF end

    def Function_4_1720(): pass

    label("Function_4_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_1BD0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A68")
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #46
        0x16,
        (
            "#1500F凯文先生……\x01",
            "这段时间说长也不算很长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1075F哈哈……也许吧。\x02\x03",

            "#1840F……约修亚。\x01",
            "我想对你说一句真心话。\x02\x03",

            "我啊……\x01",
            "现在非常羡慕你呢。\x02",
        )
    )

    Jump("loc_1802")

    label("loc_1802")

    CloseMessageWindow()

    ChrTalk(    #48
        0x16,
        "#1504F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1844F在某种意义上……\x01",
            "我和你走的是同样的道路不是吗？\x02\x03",

            "但是只有你能够\x01",
            "回到充满阳光的地方……\x02\x03",

            "#1846F半年前，\x01",
            "我只是为你的转变感觉到高兴……\x02\x03",

            "……而事到如今，\x01",
            "我却产生了强烈的羡慕之情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x16,
        (
            "#1514F凯文先生……\x02\x03",

            "#1513F……大概这会成为你\x01",
            "『永不放弃』的动力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1068F啊啊……\x01",
            "看来的确是这样啊。\x02\x03",

            "#1066F哈哈……\x01",
            "总觉得很没有面子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x16,
        (
            "#1509F这样不也很好吗。\x01",
            "没有面子又怎么样呢。\x02\x03",

            "#1501F……凯文先生。\x01",
            "我们一定要从这个世界逃出去。\x02\x03",

            "要相信大家……\x01",
            "还有，相信自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        "#1840F啊啊……当然！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2667)
    Jump("loc_1BCA")

    label("loc_1A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1F")

    ChrTalk(    #54
        0x16,
        (
            "#1505F『影之王』\x01",
            "把我们都称呼为棋子。\x02\x03",

            "#1502F……大概他设下了\x01",
            "只要我们所有人不齐心协力\x01",
            "就无法逃出这里的安排。\x02\x03",

            "『影之王』似乎\x01",
            "对规则十分偏执。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1BCA")

    label("loc_1B1F")


    ChrTalk(    #55
        0x16,
        (
            "#1502F如果我们在这里的\x01",
            "所有人不齐心协力，\x01",
            "肯定就无法逃出这里……\x02\x03",

            "#1503F这也许就是他\x01",
            "预先设定好的规则。\x02\x03",

            "『王』本身似乎就是\x01",
            "由规则所定下的存在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCA")

    TalkEnd(0xFE)
    Jump("loc_2565")

    label("loc_1BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2301")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D44")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #56
        0x110,
        (
            "#264F……约修亚？\x02\x03",

            "#260F你在这种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x110, 400)
    Sleep(300)

    ChrTalk(    #57
        0x16,
        (
            "#1513F啊啊，这个……\x02\x03",

            "#1500F我想试着推测一下\x01",
            "接下来会有怎样的进展……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x110,
        (
            "#266F……呼，\x01",
            "那种事不前进怎么知道。\x02\x03",

            "#262F唉，\x01",
            "难得我说过\x01",
            "要给你们帮忙的……\x02",
        )
    )

    Jump("loc_1D19")

    label("loc_1D19")

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        "#1509F哈哈，是啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_22FE")

    label("loc_1D44")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    TurnDirection(0x16, 0x101, 0)
    TurnDirection(0x0, 0x16, 0)
    TurnDirection(0x1, 0x16, 0)
    TurnDirection(0x2, 0x16, 0)
    TurnDirection(0x3, 0x16, 0)
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F22")
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(    #60
        0x101,
        (
            "#1000F……约修亚？\x02\x03",

            "在这里做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x16,
        "#1505F嗯，关于玲的事……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58170, 1000, -57430, 147)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 60320, 1000, -59930, 129)
    SetChrPos(0x105, 58640, 1000, -59150, 133)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x16, 0x105, 0)
    TurnDirection(0x105, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #62
        0x105,
        (
            "#1382F那个，艾丝蒂尔，\x01",
            "你们离开利贝尔出去旅行，\x01",
            "是为了去找玲吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1F22")

    TurnDirection(0x17, 0x101, 0)

    ChrTalk(    #63
        0x101,
        (
            "#1000F……约修亚和科洛丝？\x02\x03",

            "在这里做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        "#1505F嗯，关于玲的事……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58040, 1000, -58350, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x16, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #65
        0x17,
        (
            "#1382F那个，艾丝蒂尔，\x01",
            "你们离开利贝尔出去旅行，\x01",
            "是为了去找玲吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")


    ChrTalk(    #66
        0x101,
        (
            "#1003F嗯，因为当时\x01",
            "在中枢塔没能好好说明白……\x02\x03",

            "#1007F还有一些\x01",
            "要告诉玲的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x16, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #67
        0x101,
        (
            "#1016F呵呵，\x01",
            "不过现在的她看起来好多了呢。\x02\x03",

            "#1017F……嗯，\x01",
            "就这样继续在一旁守护着她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1501F…………是啊。\x02\x03",

            "#1513F着急是没有用的。\x01",
            "作出最后决定的\x01",
            "只能是玲自己……\x02\x03",

            "……她被吸进\x01",
            "这个世界里面……\x02\x03",

            "#1500F在这里与大家见面，\x01",
            "对玲来说也许会\x01",
            "产生不错的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227C")

    ChrTalk(    #69
        0x105,
        "#1168F……嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_229D")

    label("loc_227C")


    ChrTalk(    #70
        0x17,
        "#1168F……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_229D")

    Sleep(500)
    Fade(500)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_51(0x0, 0x1, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x2, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x3, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x4, (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_51(0x16, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2666)
    EventEnd(0x6)

    label("loc_22FE")

    Jump("loc_2565")

    label("loc_2301")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2497")
    OP_A2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E8")

    ChrTalk(    #71
        0x16,
        (
            "#1505F如果和玲所说的一样，\x01",
            "这个世界是由『影之王』\x01",
            "构建起来的……\x02\x03",

            "那么这前方的星层\x01",
            "也一定是遵照着\x01",
            "『影之王』的目的而产生。\x02\x03",

            "#1503F『王』所设置的游戏……\x01",
            "……真是没什么好感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2494")

    label("loc_23E8")


    ChrTalk(    #72
        0x16,
        (
            "#1501F关于玲的事情，\x01",
            "就这样继续在一旁\x01",
            "默默守护着她吧。\x02\x03",

            "作出最后决定的\x01",
            "只能是玲自己……\x02\x03",

            "#1513F在这里与大家见面，\x01",
            "对玲来说也许会\x01",
            "产生不错的影响。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    Jump("loc_2562")

    label("loc_2497")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F7")

    ChrTalk(    #73
        0x16,
        (
            "#1505F『王』所设置的游戏……#2580W \x01",
            "#20W#1503F……真是没什么好感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2562")

    label("loc_24F7")


    ChrTalk(    #74
        0x16,
        (
            "#1501F关于玲的事情，\x01",
            "就这样继续在一旁\x01",
            "默默守护着她吧。\x02\x03",

            "作出最后决定的\x01",
            "只能是她自己……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2562")

    TalkEnd(0xFE)

    label("loc_2565")

    Return()

    # Function_4_1720 end

    def Function_5_2566(): pass

    label("Function_5_2566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28FD")
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2711")
    TurnDirection(0xFE, 0x10E, 0)

    ChrTalk(    #75
        0x19,
        (
            "#1541F……尤莉亚小姐。\x02\x03",

            "我回国的时候，\x01",
            "真是受你多方照顾了。\x02\x03",

            "#1547F怎么样，\x01",
            "待会儿一起去喝一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10E,
        "#172F啊………………\x02",
    )

    CloseMessageWindow()
    OP_4A(0x14, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2667")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_265D")
    TurnDirection(0x10D, 0x10E, 400)
    Jump("loc_2664")

    label("loc_265D")

    TurnDirection(0x14, 0x10E, 400)

    label("loc_2664")

    Jump("loc_2686")

    label("loc_2667")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_267F")
    TurnDirection(0x10D, 0x13, 400)
    Jump("loc_2686")

    label("loc_267F")

    TurnDirection(0x14, 0x13, 400)

    label("loc_2686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CC")

    ChrTalk(    #77
        0x10D,
        (
            "#272F……上尉，\x01",
            "请不要把这家伙的话当真。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2701")

    label("loc_26CC")


    ChrTalk(    #78
        0x14,
        (
            "#272F……上尉，\x01",
            "请不要把这家伙的话当真。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2701")

    OP_4B(0x14, 255)
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28F4")

    label("loc_2711")


    ChrTalk(    #79
        0x19,
        (
            "#1545F哼，其实我想趁这个机会\x01",
            "和尤莉亚小姐多亲近一些呢。\x02\x03",

            "#1542F趁别人没发现……\x01",
            "不对，应该瞅准时机……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D4")

    ChrTalk(    #80
        0x102,
        (
            "#1505F我劝你最好\x01",
            "还是放弃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_285F")

    label("loc_27D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280E")

    ChrTalk(    #81
        0x101,
        "#1007F唉……还是不要这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_285F")

    label("loc_280E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(    #82
        0x105,
        (
            "#1165F啊、啊哈哈……\x02\x03",

            "我劝你最好\x01",
            "还是放弃吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_285F")


    ChrTalk(    #83
        0x10D,
        (
            "#274F……我不是已经那么警告过你\x01",
            "不要惹出问题来吗。\x02\x03",

            "乖乖地留在这里看家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F4")

    label("loc_28C0")


    ChrTalk(    #84
        0x19,
        (
            "#1541F真是不走运，\x01",
            "让穆拉那家伙看到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F4")

    OP_A2(0xE)
    TalkEnd(0xFE)
    Jump("loc_2A0B")

    label("loc_28FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2964")
    TurnDirection(0x19, 0x10E, 0)

    ChrTalk(    #85
        0x19,
        (
            "#1547F哦呵呵，尤莉亚小姐。\x01",
            "待会儿一起去喝一杯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29AE")

    label("loc_2964")


    ChrTalk(    #86
        0x19,
        (
            "#1542F呼，还真是滴水不漏啊。\x02\x03",

            "到底从哪边开始下手呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AE")

    TalkEnd(0xFE)
    Jump("loc_2A0B")

    label("loc_29B4")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x14, 255)

    ChrTalk(    #87
        0x19,
        "#1541F穆拉君真讨厌……\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_4B(0x14, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_2A0B")

    Jump("loc_38E8")

    label("loc_2A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2CB0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AA5")
    Jump("loc_2AE7")

    label("loc_2AA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AC1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE7")

    label("loc_2AC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ADD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE7")

    label("loc_2ADD")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AE7")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1B")

    ChrTalk(    #88
        0x19,
        (
            "#1540F哎呀，凯文神父……\x02\x03",

            "#1545F呵呵，\x01",
            "你似乎也隐瞒着很多事情呢。\x02\x03",

            "虽然我不会要求你都说出来，\x01",
            "但既然把我们也卷了进来，\x01",
            "至少要告诉我们来龙去脉吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x109,
        (
            "#1843F嗯，我一定会坦白的。\x02\x03",

            "#1060F不好意思，\x01",
            "请你们再等一段时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2CA5")

    label("loc_2C1B")


    ChrTalk(    #90
        0x19,
        (
            "#1545F呼……从你的职业来说，\x01",
            "不可能把全部事情都告诉我们……\x02\x03",

            "#1540F但既然把我们也卷了进来，\x01",
            "至少要告诉我们来龙去脉吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_38E8")

    label("loc_2CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_3099")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EDB")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D55")
    Jump("loc_2D97")

    label("loc_2D55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D71")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D97")

    label("loc_2D71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D8D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D97")

    label("loc_2D8D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D97")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E65")

    ChrTalk(    #91
        0x19,
        (
            "#1545F呵呵，\x01",
            "这次豪华的聚会\x01",
            "看来还要继续下去。\x02\x03",

            "#1540F偶尔在这种地方\x01",
            "安静地修养一下也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10D,
        "#272F…………你也至少干点活吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2ED0")

    label("loc_2E65")

    TalkBegin(0xFE)

    ChrTalk(    #93
        0x19,
        (
            "#1545F各位，你们就\x01",
            "随便使唤穆拉这家伙吧。\x02\x03",

            "为了我，\x01",
            "他一定会努力工作的。\x02",
        )
    )

    Jump("loc_2ECF")

    label("loc_2ECF")

    CloseMessageWindow()

    label("loc_2ED0")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3096")

    label("loc_2EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3022")
    SetChrFlags(0x19, 0x10)
    TalkBegin(0x19)
    OP_4A(0x19, 255)
    OP_4A(0x14, 255)

    ChrTalk(    #94
        0x19,
        (
            "#1542F……不，这次的事件\x01",
            "应该和宰相阁下没有关系。\x02\x03",

            "那个人要是动手的话，\x01",
            "一定不会采用这种\x01",
            "麻烦的方式的。\x02\x03",

            "#1551F至于与『蛇』的关系就不好断言了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x14,
        (
            "#272F的确，不像是他的作风呢。\x02\x03",

            "#276F如果要弄出这种花样，\x01",
            "趁我们在帝都时应该有的是机会……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    ClearChrFlags(0x19, 0x10)
    OP_4B(0x19, 255)
    OP_4B(0x14, 255)
    TalkEnd(0x19)
    Jump("loc_3096")

    label("loc_3022")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0x19,
        (
            "#1540F哎呀，各位，\x01",
            "探索方面有什么进展呢？\x02\x03",

            "#1541F如果知道了什么的话，\x01",
            "请一定要来告诉我哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_3096")

    Jump("loc_38E8")

    label("loc_3099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_38E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367F")
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30BE")
    OP_4A(0x14, 255)

    label("loc_30BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30DB")
    OP_4A(0x13, 255)

    label("loc_30DB")

    SetChrFlags(0x19, 0x10)
    TalkBegin(0x19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3261")
    OP_51(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x105, 0)
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3181")
    Jump("loc_31C3")

    label("loc_3181")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_319D")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31C3")

    label("loc_319D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31B9")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31C3")

    label("loc_31B9")

    OP_51(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31C3")

    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(    #97
        0x105,
        (
            "#1382F奥利维特皇子，\x01",
            "自上次之后您好像没有什么变化呢。\x02\x03",

            "不过我倒是听说您在\x01",
            "帝国的社交界非常活跃……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32DC")

    label("loc_3261")

    SetChrSubChip(0x19, 0)

    ChrTalk(    #98
        0x17,
        (
            "#1382F奥利维特皇子，\x01",
            "自上次之后您好像没有什么变化呢。\x02\x03",

            "不过我倒是听说您在\x01",
            "帝国的社交界非常活跃……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DC")


    ChrTalk(    #99
        0x19,
        (
            "#1545F呵呵，\x01",
            "现在只是隐藏实力掩人耳目罢了。\x02\x03",

            "#1542F不过当一个优雅的贵公子\x01",
            "还真是累人。\x02\x03",

            "#1544F等时机一到，\x01",
            "我就会华丽地披露我的真实身份……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #100
        0x19,
        (
            "#1541F#3S──对！\x01",
            "作为『爱的福音使者』的真实身份！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x19, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(2000)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3474")
    OP_62(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3474")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3499")
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C9")
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_34C9")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F9")

    ChrTalk(    #101
        0x10D,
        "#274F白痴……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3513")

    label("loc_34F9")


    ChrTalk(    #102
        0x14,
        "#274F白痴……\x02",
    )

    CloseMessageWindow()

    label("loc_3513")


    ChrTalk(    #103
        0x109,
        "#1068F原来你是『爱的福音使者』啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_358B")

    ChrTalk(    #104
        0x102,
        (
            "#1508F听起来比那个『福音』\x01",
            "还要危险呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C1")

    label("loc_358B")


    ChrTalk(    #105
        0x16,
        (
            "#1508F听起来比那个『福音』\x01",
            "还要危险呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3604")

    ChrTalk(    #106
        0x105,
        (
            "#1165F呵呵……\x01",
            "看到您没变我就放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3636")

    label("loc_3604")


    ChrTalk(    #107
        0x17,
        (
            "#1165F呵呵……\x01",
            "看到您没变我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3636")

    OP_63(0x19)
    OP_4B(0x17, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364F")
    OP_4B(0x14, 255)

    label("loc_364F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_366C")
    OP_4B(0x13, 255)

    label("loc_366C")

    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x10)
    TalkEnd(0x19)
    OP_A2(0x2660)
    Jump("loc_38E8")

    label("loc_367F")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_370F")
    Jump("loc_3751")

    label("loc_370F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_372B")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3751")

    label("loc_372B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3747")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3751")

    label("loc_3747")

    OP_51(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3751")

    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384B")

    ChrTalk(    #108
        0x19,
        (
            "#1545F…………说起来，\x01",
            "那个女性幽灵还真是不错啊。\x02\x03",

            "孤身一人留在这『影之国』的\x01",
            "美丽亡灵……\x02\x03",

            "#1547F哦呵呵，\x01",
            "还真是让人雀跃不已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        "#1508F………………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_38E0")

    label("loc_384B")


    ChrTalk(    #110
        0x19,
        (
            "#1540F说起来，\x01",
            "那个女性幽灵还真是不错啊。\x02\x03",

            "这样富有幻想风格的『庭院』\x01",
            "说不定也是她的兴趣呢。\x02\x03",

            "#1541F呵呵，不觉得很美妙吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E0")

    SetChrSubChip(0x19, 0)
    TalkEnd(0x19)

    label("loc_38E8")

    Return()

    # Function_5_2566 end

    def Function_6_38E9(): pass

    label("Function_6_38E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_3EAC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B25")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3998")
    Jump("loc_39DA")

    label("loc_3998")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39B4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DA")

    label("loc_39B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DA")

    label("loc_39D0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39DA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #111
        0x17,
        (
            "#1383F约修亚…………\x02\x03",

            "#1382F……你和那个人道过别了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x102,
        (
            "#1513F……嗯，托大家的福。\x02\x03",

            "#1514F话说回来……\x01",
            "科洛丝，你的感觉也太敏锐了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x17,
        (
            "#1165F啊哈哈………\x02\x03",

            "#1168F因为，\x01",
            "你现在的表情看起来很释然呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2669)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3EA9")

    label("loc_3B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CBE")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BCB")
    Jump("loc_3C0D")

    label("loc_3BCB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BE7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C0D")

    label("loc_3BE7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C03")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C0D")

    label("loc_3C03")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C0D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #114
        0x17,
        (
            "#1164F啊，那个……\x02\x03",

            "#1382F我不知不觉就热衷于\x01",
            "读这书架上面的书了……\x02\x03",

            "#1165F呵呵，\x01",
            "现在要稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3D36")

    label("loc_3CBE")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #115
        0x17,
        (
            "#1165F啊、啊哈哈……\x01",
            "不好意思，乔丝特。\x02\x03",

            "我经常会像这样\x01",
            "埋头于一件事而顾不得其它……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_3D36")

    OP_A2(0xC)
    Jump("loc_3EA9")

    label("loc_3D3C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DCC")
    Jump("loc_3E0E")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DE8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E0E")

    label("loc_3DE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E04")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E0E")

    label("loc_3E04")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E0E")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #116
        0x17,
        (
            "#1168F说起来，\x01",
            "这里真是让人感到平静的地方。\x02\x03",

            "#1168F刚来到这里的时候，\x01",
            "倒是让我吃惊不小……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_3EA9")

    Jump("loc_51C7")

    label("loc_3EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_4A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F5F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x17, 0x110, 400)

    ChrTalk(    #117
        0x17,
        (
            "#1164F啊，玲……？\x02\x03",

            "#1165F啊哈哈，那个……\x02\x03",

            "出去探索的时候\x01",
            "要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4798")

    label("loc_3F5F")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    TurnDirection(0x16, 0x101, 0)
    TurnDirection(0x17, 0x101, 0)
    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_438E")

    ChrTalk(    #118
        0x101,
        (
            "#1000F……科洛丝？\x02\x03",

            "在这里\x01",
            "做什么呢……\x02",
        )
    )

    Jump("loc_401D")

    label("loc_401D")

    CloseMessageWindow()

    ChrTalk(    #119
        0x17,
        (
            "#1164F啊，那个……\x02\x03",

            "#1382F我有点担心\x01",
            "玲的情况……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58040, 1000, -58350, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D0")
    SetChrPos(0x105, 59050, 1000, -59340, 129)

    label("loc_40D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40EF")
    SetChrPos(0x102, 59020, 1000, -59390, 81)

    label("loc_40EF")

    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x10F, 0x8)
    TurnDirection(0x102, 0x17, 0)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #120
        0x17,
        (
            "#1382F你们离开利贝尔之后，\x01",
            "是为了去找玲吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1503F嗯，在中枢塔上\x01",
            "没能和她好好谈谈，所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1011F所以，就想找到她，\x01",
            "告诉她一直以来想说的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x102, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #123
        0x101,
        (
            "#1016F呵呵，\x01",
            "不过现在的她看起来好多了呢。\x02\x03",

            "#1017F……嗯，\x01",
            "就这样继续在一旁守护着她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1501F…………是啊。\x02\x03",

            "#1513F着急是没有用的。\x01",
            "作出最后决定的\x01",
            "只能是玲自己……\x02\x03",

            "……她被吸进\x01",
            "这个世界里面……\x02\x03",

            "#1500F在这里与大家见面，\x01",
            "对玲来说也许会\x01",
            "产生不错的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "#1168F……嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4737")

    label("loc_438E")


    ChrTalk(    #126
        0x101,
        (
            "#1000F……约修亚和科洛丝？\x02\x03",

            "在这里\x01",
            "做什么呢……\x02",
        )
    )

    Jump("loc_43DC")

    label("loc_43DC")

    CloseMessageWindow()

    ChrTalk(    #127
        0x17,
        (
            "#1164F啊，艾丝蒂尔。\x02\x03",

            "#1382F有点在意玲的情况……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58260, 1000, -58840, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_448E")
    SetChrPos(0x105, 59050, 1000, -59340, 129)

    label("loc_448E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A6")
    SetChrFlags(0x102, 0x8)
    ClearChrFlags(0x16, 0x80)

    label("loc_44A6")

    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x10F, 0x8)
    TurnDirection(0x16, 0x17, 0)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #128
        0x17,
        (
            "#1382F艾丝蒂尔，\x01",
            "你们离开利贝尔出去旅行，\x01",
            "是为了去找玲吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1003F嗯，因为当时\x01",
            "在中枢塔没能好好说明白……\x02\x03",

            "#1007F还有一些\x01",
            "要告诉玲的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x16, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #130
        0x101,
        (
            "#1016F呵呵，\x01",
            "不过现在的她看起来好多了呢。\x02\x03",

            "#1017F……嗯，\x01",
            "就这样继续在一旁守护着她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x16,
        (
            "#1501F…………是啊。\x02\x03",

            "#1513F着急是没有用的。\x01",
            "作出最后决定的\x01",
            "只能是玲自己……\x02\x03",

            "……她被吸进\x01",
            "这个世界里面……\x02\x03",

            "#1500F在这里与大家见面，\x01",
            "对玲来说也许会\x01",
            "产生不错的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        "#1168F……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4737")

    Sleep(500)
    Fade(500)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_51(0x0, 0x1, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x2, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x3, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x4, (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_51(0x16, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2666)
    EventEnd(0x6)

    label("loc_4798")

    Jump("loc_4A72")

    label("loc_479B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4981")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4895")

    ChrTalk(    #133
        0x17,
        (
            "#1162F这世界能够反映人的想法……\x02\x03",

            "那么，把我们集合在这里\x01",
            "也许也是某个人的意志在起作用。\x02\x03",

            "#1169F如果是这样的话……\x01",
            "是『影之王』，还是那个女性的幽灵呢……\x02\x03",

            "#1167F或许……是我们自身也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_497B")

    label("loc_4895")


    ChrTalk(    #134
        0x17,
        (
            "#1167F虽然我觉得正面\x01",
            "向玲传达心意很不容易……\x02\x03",

            "#1168F不过，艾丝蒂尔和约修亚\x01",
            "你们一定没问题的。\x02\x03",

            "因为你们之间拥有如此强大的羁绊，\x01",
            "所以一定能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1008F啊哈哈……\x02\x03",

            "#1006F谢谢你，科洛丝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_497B")

    OP_A2(0xC)
    Jump("loc_4A6F")

    label("loc_4981")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A06")

    ChrTalk(    #136
        0x17,
        (
            "#1167F虽然解决了一些谜题，\x01",
            "但新的问题又随之而来。\x02\x03",

            "#1162F……原来如此。\x01",
            "的确是计划周全的游戏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6F")

    label("loc_4A06")


    ChrTalk(    #137
        0x17,
        (
            "#1383F我也想尽力\x01",
            "帮你们为玲\x01",
            "做一些事情。\x02\x03",

            "#1382F如果有用的上我的地方，\x01",
            "请随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6F")

    TalkEnd(0xFE)

    label("loc_4A72")

    Jump("loc_51C7")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_4BE0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5A")

    ChrTalk(    #138
        0x17,
        (
            "#1160F自从理查德先生\x01",
            "从军队退役之后，\x01",
            "我还没有机会和他见面……\x02\x03",

            "#1161F不过倒是听说过好几次\x01",
            "他开的公司的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1004F哎，是这样啊……\x02\x03",

            "#1015F好像生意很红火的样子……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4BDA")

    label("loc_4B5A")


    ChrTalk(    #140
        0x17,
        (
            "#1160F我经常听人提起\x01",
            "理查德先生的公司。\x02\x03",

            "#1383F『Ｒ＆Ａ Research』公司……\x01",
            "我记得杂志上也刊登过\x01",
            "小型的广告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BDA")

    TalkEnd(0xFE)
    Jump("loc_51C7")

    label("loc_4BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_4D86")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA0")

    ChrTalk(    #141
        0x17,
        (
            "#1167F应该还有人\x01",
            "被封印石困在里面。\x02\x03",

            "#1167F不知道是在异界化的\x01",
            "卢·洛克尔训练场，\x01",
            "还是接下来的『第五星层』……\x02\x03",

            "#1162F……现在只能继续前进了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4D80")

    label("loc_4CA0")


    ChrTalk(    #142
        0x17,
        (
            "#1162F我很担心\x01",
            "被封印之人的安全。\x01",
            "但现在也只能继续前进了。\x02\x03",

            "#1167F虽然莉丝小姐的事情\x01",
            "也很让人在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x109,
        (
            "#1840F（唔…………\x01",
            "  好像被看穿了……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        "#1514F（不愧是科洛丝，感觉真敏锐……）\x02",
    )

    CloseMessageWindow()

    label("loc_4D80")

    TalkEnd(0xFE)
    Jump("loc_51C7")

    label("loc_4D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_4F7D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E25")
    Jump("loc_4E67")

    label("loc_4E25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E41")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E67")

    label("loc_4E41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E5D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E67")

    label("loc_4E5D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E67")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(    #145
        0x17,
        (
            "#1164F啊，\x01",
            "正好基库说它有点饿了……\x02\x03",

            "#1165F呵呵，没关系的。\x01",
            "马上就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4F6D")

    label("loc_4EF4")


    ChrTalk(    #146
        0x17,
        (
            "#1160F话说回来，\x01",
            "能够方便取得水和食物真是太好了。\x02\x03",

            "这也许都是\x01",
            "那位女性幽灵……\x01",
            "『庭院之主』的功劳呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6D")

    SetChrSubChip(0xFE, 1)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_51C7")

    label("loc_4F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_509A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_503E")

    ChrTalk(    #147
        0x17,
        (
            "#1167F没想到亚妮拉丝小姐\x01",
            "也被卷了进来……\x02\x03",

            "………………………………\x02\x03",

            "#1162F……约修亚，\x01",
            "我们必须尽快进行探索。\x02\x03",

            "我也会尽力\x01",
            "援助大家的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5094")

    label("loc_503E")


    ChrTalk(    #148
        0x17,
        (
            "#1162F……约修亚，\x01",
            "我们必须尽快进行探索。\x02\x03",

            "我也会尽力\x01",
            "援助大家的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5094")

    TalkEnd(0xFE)
    Jump("loc_51C7")

    label("loc_509A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_51C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50BB")
    Call(5, 5)
    Jump("loc_51C7")

    label("loc_50BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5146")

    ChrTalk(    #149
        0x17,
        (
            "#1383F这个庭院似乎\x01",
            "和那位女性幽灵有关。\x02\x03",

            "#1160F说起来，这里与其它异空间不同，\x01",
            "有种被保护起来的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_51C4")

    label("loc_5146")


    ChrTalk(    #150
        0x17,
        (
            "#1160F这个庭院\x01",
            "也许本来就是和那位\x01",
            "女性幽灵有关的地方。\x02\x03",

            "#1168F呵呵，\x01",
            "这么一想，\x01",
            "就有种被保护起来的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51C4")

    TalkEnd(0xFE)

    label("loc_51C7")

    Return()

    # Function_6_38E9 end

    def Function_7_51C8(): pass

    label("Function_7_51C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5D32")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5836")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B0")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5288")
    Jump("loc_52CA")

    label("loc_5288")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52A4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52CA")

    label("loc_52A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52CA")

    label("loc_52C0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52CA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #151
        0x101,
        (
            "#1015F咦，阿加特……\x01",
            "你没跟提妲在一起吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53AF")

    ChrTalk(    #152
        0x1D,
        (
            "#551F哎呀，\x01",
            "我又不是那家伙的监护人。\x02\x03",

            "#053F……那家伙已经不是小孩了。\x02\x03",

            "她知道自己\x01",
            "该做些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5413")

    label("loc_53AF")


    ChrTalk(    #153
        0x1D,
        (
            "#551F哎呀，\x01",
            "我又不是那家伙的监护人。\x02\x03",

            "#051F而且她正和朋友在一起，\x01",
            "不是也挺好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5413")


    ChrTalk(    #154
        0x101,
        "#1028F……呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1D,
        "#555F……怎么，想发什么牢骚吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54AD")

    ChrTalk(    #156
        0x104,
        "#1541F别害羞，别害羞㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    label("loc_54AD")

    Jump("loc_5830")

    label("loc_54B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F1")
    OP_51(0x10F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x10F, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5559")
    Jump("loc_559B")

    label("loc_5559")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5575")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_559B")

    label("loc_5575")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5591")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_559B")

    label("loc_5591")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_559B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #157
        0x10F,
        (
            "#1936F…………那个。\x02\x03",

            "#1938F要找提妲的话，\x01",
            "她就在那边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x1D,
        (
            "#052F嗯，啊啊……\x02\x03",

            "#051F那又怎么样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10F,
        (
            "#1938F没什么，\x01",
            "你们之前总是在一起。\x02\x03",

            "#1937F我还以为你们走散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1D,
        "#055F……我又没有迷路……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56EE")

    ChrTalk(    #161
        0x110,
        "#261F嘻嘻…………\x02",
    )

    CloseMessageWindow()

    label("loc_56EE")

    Jump("loc_5830")

    label("loc_56F1")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5781")
    Jump("loc_57C3")

    label("loc_5781")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_579D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57C3")

    label("loc_579D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57B9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57C3")

    label("loc_57B9")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57C3")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #162
        0x1D,
        (
            "#053F……终于要结束了。\x02\x03",

            "#051F趁现在好好锻炼一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5830")

    OP_A2(0x5)
    Jump("loc_5D25")

    label("loc_5836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59EE")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58DF")
    Jump("loc_5921")

    label("loc_58DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58FB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5921")

    label("loc_58FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5917")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5921")

    label("loc_5917")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5921")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #163
        0x1D,
        (
            "#053F那家伙已经不是小孩了。\x02\x03",

            "#051F必要的时候我会跟着她的。\x01",
            "……不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1028F哎呀～………☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x1D,
        "#055F……到底要怎么样 ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D25")

    label("loc_59EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BC1")
    OP_51(0x10F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x10F, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A97")
    Jump("loc_5AD9")

    label("loc_5A97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AB3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AD9")

    label("loc_5AB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ACF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AD9")

    label("loc_5ACF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AD9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #166
        0x1D,
        (
            "#551F……我可不是说\x01",
            "要一直在一起。\x02\x03",

            "#051F那家伙\x01",
            "已经不是小孩子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1930F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x1D,
        (
            "#055F……你、你那一脸\x01",
            "不可思议的表情是什么意思！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D25")

    label("loc_5BC1")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C51")
    Jump("loc_5C93")

    label("loc_5C51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C6D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C93")

    label("loc_5C6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C89")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C93")

    label("loc_5C89")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C93")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #169
        0x1D,
        (
            "#050F从现在开始，\x01",
            "已经没有什么时间\x01",
            "让我们停滞不前了。\x02\x03",

            "#051F你们也趁现在\x01",
            "好好锻炼一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D25")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5D32")

    Return()

    # Function_7_51C8 end

    def Function_8_5D33(): pass

    label("Function_8_5D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_60BD")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6061")

    ChrTalk(    #170
        0x12,
        (
            "#060F靠埃尔赛尤号的速度，\x01",
            "超越『星层』\x01",
            "应该不会用很长时间的。\x02\x03",

            "#067F上个月妈妈刚改造过，\x01",
            "速度已经有很大提升了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EC0")

    ChrTalk(    #171
        0x101,
        (
            "#1001F啊哈哈，是这样啊。\x02\x03",

            "#1006F唔，提妲的妈妈吗。\x01",
            "我也想见见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x12,
        (
            "#067F嘿嘿…………\x02\x03",

            "#560F嗯，爸爸妈妈都说\x01",
            "要和姐姐你们见一面呢。\x02\x03",

            "#061F等你们回利贝尔之后\x01",
            "我一定会把你们介绍给他们的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_605B")

    label("loc_5EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FB1")

    ChrTalk(    #173
        0x102,
        (
            "#1504F提妲的母亲\x01",
            "是叫做艾莉卡吧。\x02\x03",

            "#1500F父亲的名字……\x01",
            "是丹对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x12,
        (
            "#067F嘿嘿………没错。\x02\x03",

            "#560F他们两人都说\x01",
            "想见哥哥你们一面呢……\x02\x03",

            "#061F等你们回利贝尔之后\x01",
            "我一定会介绍给他们的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_605B")

    label("loc_5FB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_605B")

    ChrTalk(    #175
        0x106,
        (
            "#552F（说起来，\x01",
            "  这次会受到什么样的招待呢……）\x02\x03",

            "#551F（我去的时候就突然\x01",
            "  受到了螺丝扳手的袭击……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x12,
        "#565F哎………………？\x02",
    )

    CloseMessageWindow()

    label("loc_605B")

    OP_A2(0x0)
    Jump("loc_60B7")

    label("loc_6061")


    ChrTalk(    #177
        0x12,
        (
            "#062F好、好的…………\x02\x03",

            "为了早日回到爸爸妈妈身边，\x01",
            "我也要加油……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B7")

    TalkEnd(0xFE)
    Jump("loc_797D")

    label("loc_60BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_6874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65FB")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x12)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611F")

    ChrTalk(    #178
        0x1B,
        "#1314F……是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_613E")

    label("loc_611F")


    ChrTalk(    #179
        0x11,
        "#1445F是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_613E")


    ChrTalk(    #180
        0x12,
        (
            "#060F……嗯。\x02\x03",

            "#563F我也不清楚\x01",
            "详细的情况，\x01",
            "不过莱维哥哥果然……\x02\x03",

            "我觉得他肯定\x01",
            "一直很担心\x01",
            "约修亚哥哥的情况。\x02\x03",

            "所以才会专门来和\x01",
            "约修亚哥哥道别……\x02\x03",

            "约修亚哥哥\x01",
            "能有和他道别的机会……\x02\x03",

            "#066F……真的是太好了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6267")

    ChrTalk(    #181
        0x1B,
        "#816F嗯。是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6267")


    ChrTalk(    #182
        0x11,
        "#1448F…………嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64F0")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x110, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6329")
    Jump("loc_636B")

    label("loc_6329")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6345")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_636B")

    label("loc_6345")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6361")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_636B")

    label("loc_6361")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_636B")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 4)), scpexpr(EXPR_END)), "loc_63D7")

    ChrTalk(    #183
        0x11,
        (
            "#1962F……玲能和他见最后一面，\x01",
            "也是件好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6426")

    label("loc_63D7")


    ChrTalk(    #184
        0x11,
        (
            "#1802F对了，玲……\x02\x03",

            "#1445F你也和他道了别，\x01",
            "也算是件好事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6426")


    ChrTalk(    #185
        0x110,
        (
            "#269F呵呵……\x01",
            "这话由教会的姐姐说出来\x01",
            "还真是有点奇怪呢。\x02\x03",

            "#263F……不过…………\x02\x03",

            "……难得你在这里，\x01",
            "能为莱维讲一些\x01",
            "圣典中的故事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x11,
        "#1448F……嗯，我很荣幸。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Jump("loc_65E4")

    label("loc_64F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 4)), scpexpr(EXPR_END)), "loc_6562")

    ChrTalk(    #187
        0x11,
        (
            "#1447F……玲………\x01",
            "你能和他道别真是太好了。\x02\x03",

            "#1806F和别人分离，\x01",
            "是件十分痛苦的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E4")

    label("loc_6562")


    ChrTalk(    #188
        0x11,
        (
            "#1806F……如果………\x01",
            "能让玲也和他见最后一面就好了。\x02\x03",

            "#1445F虽然这也许是件很痛苦的事，\x01",
            "……不过毕竟是家人………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E4")

    OP_A2(0x2664)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4B(0x1B, 255)
    TalkEnd(0x12)
    Jump("loc_6871")

    label("loc_65FB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_668B")
    Jump("loc_66CD")

    label("loc_668B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_66A7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66CD")

    label("loc_66A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66C3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66CD")

    label("loc_66C3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66CD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BD")

    ChrTalk(    #189
        0x12,
        (
            "#060F我也不清楚\x01",
            "详细的情况……\x02\x03",

            "#563F不过我觉得莱维哥哥\x01",
            "一定一直很挂念\x01",
            "约修亚哥哥的情况。\x02\x03",

            "#066F而且，还有玲……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67B7")

    ChrTalk(    #190
        0x110,
        "#263F……呵呵，也许吧。\x02",
    )

    CloseMessageWindow()

    label("loc_67B7")

    OP_A2(0x0)
    Jump("loc_6856")

    label("loc_67BD")


    ChrTalk(    #191
        0x12,
        (
            "#060F以前在拉文努村的时候，\x01",
            "我和莱维哥哥\x01",
            "见过一次面。\x02\x03",

            "#564F那个时候，\x01",
            "他的眼神十分寂寞……\x02\x03",

            "#067F嘿嘿，现在已经完全不同了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6856")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6871")
    SetChrSubChip(0xFE, 2)

    label("loc_6871")

    Jump("loc_797D")

    label("loc_6874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_7166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EED")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_692D")
    Jump("loc_696F")

    label("loc_692D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6949")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_696F")

    label("loc_6949")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6965")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_696F")

    label("loc_6965")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_696F")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(    #192
        0x12,
        (
            "#064F菲利普先生\x01",
            "好像是公爵大人的管家吧。\x02\x03",

            "#063F为、为什么\x01",
            "『影之王』先生要把\x01",
            "毫无关系的人卷进来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A9B")

    ChrTalk(    #193
        0x110,
        (
            "#263F呵呵，我觉得这也不错。\x02\x03",

            "#260F……我啊，\x01",
            "对『影之王』很感兴趣呢。\x02\x03",

            "#261F真想早点跟他一决胜负。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C0F")

    label("loc_6A9B")

    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x20)
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x12, 0)
    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B2B")
    Jump("loc_6B6D")

    label("loc_6B2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B47")
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6D")

    label("loc_6B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B63")
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6D")

    label("loc_6B63")

    OP_51(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6D")

    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    ChrTalk(    #194
        0x20,
        (
            "#263F呵呵，我觉得这也不错。\x02\x03",

            "#260F……我啊，\x01",
            "对『影之王』很感兴趣呢。\x02\x03",

            "#261F真想早点跟他一决胜负。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C0F")


    ChrTalk(    #195
        0x109,
        (
            "#1066F哈哈，\x01",
            "你可不要单独行动哦……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D47")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x110, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CDD")
    Jump("loc_6D1F")

    label("loc_6CDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CF9")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D1F")

    label("loc_6CF9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D15")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D1F")

    label("loc_6D15")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D1F")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    Jump("loc_6E3E")

    label("loc_6D47")

    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x20, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DD7")
    Jump("loc_6E19")

    label("loc_6DD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DF3")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E19")

    label("loc_6DF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E0F")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E19")

    label("loc_6E0F")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E19")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    label("loc_6E3E")


    ChrTalk(    #196
        0x12,
        (
            "#562F是、是啊，玲……\x02\x03",

            "外面很危险的，\x01",
            "不能一个人随便跑出去哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6ECD")

    ChrTalk(    #197
        0x10F,
        "#1440F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_6ECD")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    TalkEnd(0xFE)
    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x8, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7163")

    label("loc_6EED")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FFD")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x110, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F93")
    Jump("loc_6FD5")

    label("loc_6F93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FAF")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FD5")

    label("loc_6FAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FCB")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FD5")

    label("loc_6FCB")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FD5")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    Jump("loc_70F4")

    label("loc_6FFD")

    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x20, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_708D")
    Jump("loc_70CF")

    label("loc_708D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70A9")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70CF")

    label("loc_70A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70C5")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70CF")

    label("loc_70C5")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70CF")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    label("loc_70F4")


    ChrTalk(    #198
        0x12,
        (
            "#562F真、真的很危险……\x02\x03",

            "玲，\x01",
            "你可不要单独行动哦。\x02",
        )
    )

    Jump("loc_713F")

    label("loc_713F")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7156")
    SetChrSubChip(0xFE, 0)
    Jump("loc_715B")

    label("loc_7156")

    SetChrSubChip(0xFE, 1)

    label("loc_715B")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_7163")

    Jump("loc_797D")

    label("loc_7166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_73CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72FD")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_720B")
    Jump("loc_724D")

    label("loc_720B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7227")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724D")

    label("loc_7227")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7243")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724D")

    label("loc_7243")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_724D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #199
        0x12,
        (
            "#064F啊，玲。\x01",
            "#061F嘿嘿，一会儿再聊吧。\x02\x03",

            "刚才还没说完呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x110,
        "#261F嘻嘻，好啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72FA")
    SetChrSubChip(0xFE, 1)

    label("loc_72FA")

    Jump("loc_73C9")

    label("loc_72FD")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #201
        0x12,
        (
            "#061F那么，\x01",
            "给那孩子起个名字吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x20,
        (
            "#261F嘻嘻，\x01",
            "玲以前也养过一只猫。\x02\x03",

            "#265F博士把它叫做\x01",
            "装甲猎豹……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #203
        0x12,
        "#065F这、这个不行吧！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_73C9")

    Jump("loc_797D")

    label("loc_73CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_797D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_754C")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #204
        0x12,
        "#064F啊，玲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x110,
        (
            "#264F提妲，\x01",
            "你在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x12,
        (
            "#060F嗯……\x02\x03",

            "#061F之前，\x01",
            "我们不是一起去购过物吗？\x02\x03",

            "我想起那次\x01",
            "买了一只很漂亮的\x01",
            "胸针的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x110,
        (
            "#260F嘻嘻，是有这么一回事。\x02\x03",

            "#267F对了……#1480W \x01",
            "#20W我之前在一家很小的店里\x01",
            "看到了同一种胸针。\x02\x03",

            "#261F不过中间的宝石是红色的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75B5")

    label("loc_754C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #208
        0x20,
        (
            "#261F……在那家店里看到\x01",
            "和上次买的同一种胸针。\x02\x03",

            "#265F不过中间的宝石是红色的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75B5")


    ChrTalk(    #209
        0x12,
        (
            "#064F啊，真不错……\x02\x03",

            "王都的百货店\x01",
            "已经都卖完了……\x02\x03",

            "#562F唉，\x01",
            "我也想要红色的啊……\x02",
        )
    )

    Jump("loc_7627")

    label("loc_7627")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76AC")

    ChrTalk(    #210
        0x110,
        (
            "#265F那么，\x01",
            "下次我就带你去\x01",
            "那家很远的店转转吧？\x02\x03",

            "#269F在共和国的东方人街里\x01",
            "转一天都不会觉得烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771F")

    label("loc_76AC")


    ChrTalk(    #211
        0x20,
        (
            "#265F那么，\x01",
            "下次我就带你去\x01",
            "那家很远的店转转吧？\x02\x03",

            "#269F在共和国的东方人街里\x01",
            "转一天都不会觉得烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771F")


    ChrTalk(    #212
        0x12,
        (
            "#064F是、是这样啊……\x02\x03",

            "#061F嘿嘿，\x01",
            "如果能再找到可爱的小玩意就好了～\x02\x03",

            "#560F听我说，\x01",
            "之前我买的那个挂饰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1016F（……唔，\x01",
            "  好像聊得很热闹嘛。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2662)
    TalkEnd(0xFE)
    Jump("loc_797D")

    label("loc_77E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78C6")
    TalkBegin(0xFE)
    TurnDirection(0x12, 0x110, 0)

    ChrTalk(    #214
        0x12,
        (
            "#061F玲，\x01",
            "下次我们再一起去购物吧。\x02",
        )
    )

    Jump("loc_7839")

    label("loc_7839")

    CloseMessageWindow()

    ChrTalk(    #215
        0x110,
        (
            "#260F……我倒无所谓。\x02\x03",

            "#263F不过在那之前，\x01",
            "我们必须要想办法\x01",
            "从这个世界逃出去不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        "#064F啊，没错……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_7914")

    label("loc_78C6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #217
        0x12,
        (
            "#065F哇……\x02\x03",

            "#067F我、我也想见识一下呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_7914")

    OP_A2(0x0)
    Jump("loc_797D")

    label("loc_791A")

    TalkBegin(0xFE)

    ChrTalk(    #218
        0x12,
        (
            "#560F玲，\x01",
            "你去过的店还真不少啊……\x02\x03",

            "#067F我、我也想去见识一下呢……\x02",
        )
    )

    Jump("loc_7979")

    label("loc_7979")

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_797D")

    Return()

    # Function_8_5D33 end

    def Function_9_797E(): pass

    label("Function_9_797E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_79DC")
    TalkBegin(0xFE)

    ChrTalk(    #219
        0x1B,
        (
            "#814F哎……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x109,
        "#1075F不，没什么要紧的。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_8D74")

    label("loc_79DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_7DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C43")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B52")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #221
        0x1B,
        (
            "#1316F那个，\x01",
            "我并不知道详细的情况……\x02\x03",

            "#816F不过，我可以这样断言。\x02\x03",

            "#811F……现在的约修亚，\x01",
            "表情相当释然呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        (
            "#1504F亚妮拉丝小姐……\x02\x03",

            "#1513F……谢谢你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B4C")
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)

    ChrTalk(    #223
        0x1B,
        (
            "#816F对了……\x01",
            "艾丝蒂尔也是！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1017F啊、啊哈哈……是吗？\x02",
    )

    CloseMessageWindow()

    label("loc_7B4C")

    OP_A2(0x9)
    Jump("loc_7C3D")

    label("loc_7B52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BC7")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #225
        0x1B,
        (
            "#816F约修亚，\x01",
            "你好像越过了一道巨大的障碍呢。\x02\x03",

            "#811F嗯，现在的表情很不错！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3D")

    label("loc_7BC7")


    ChrTalk(    #226
        0x1B,
        (
            "#817F那个，\x01",
            "我并不知道详细的情况……\x02\x03",

            "#1314F可以断定的是……\x01",
            "约修亚他好像\x01",
            "越过了一道巨大的障碍呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C3D")

    TalkEnd(0xFE)
    Jump("loc_7DA4")

    label("loc_7C43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C63")
    Call(5, 8)
    Jump("loc_7DA4")

    label("loc_7C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D13")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #227
        0x1B,
        (
            "#1314F唔，\x01",
            "我对相关的事情不是很了解……\x02\x03",

            "#813F莱维先生……\x01",
            "是约修亚的哥哥吧。\x02\x03",

            "#817F不过，在浮游都市的那次事件中……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_7DA4")

    label("loc_7D13")

    TalkBegin(0xFE)

    ChrTalk(    #228
        0x1B,
        (
            "#817F莱维先生……\x02\x03",

            "好像是\x01",
            "约修亚的哥哥吧。\x02\x03",

            "#813F唔，\x01",
            "我没有到浮游都市去，\x01",
            "所以不清楚详细情况……\x02",
        )
    )

    Jump("loc_7DA0")

    label("loc_7DA0")

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7DA4")

    Jump("loc_8D74")

    label("loc_7DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_8152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #229
        0x1B,
        (
            "#814F啊，咦……！？\x02\x03",

            "#1317F大家都到哪里去了！？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x9)
    TalkEnd(0xFE)
    Jump("loc_814F")

    label("loc_7E0F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F60")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x107, 500)

    ChrTalk(    #230
        0x1B,
        (
            "#1310F啊，\x01",
            "你们两个竟然躲在这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x107,
        "#067F哎，嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x110,
        (
            "#263F我们马上\x01",
            "就要出发了。\x02\x03",

            "#260F姐姐，\x01",
            "一会儿再聊吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F5D")

    ChrTalk(    #233
        0x1B,
        (
            "#818F嗯嗯～…………\x02\x03",

            "#1311F那，\x01",
            "一会儿莉丝也要来……㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x10F,
        "#1802F啊，唉…………\x02",
    )

    CloseMessageWindow()

    label("loc_7F5D")

    Jump("loc_8147")

    label("loc_7F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8032")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x107, 500)

    ChrTalk(    #235
        0x1B,
        (
            "#1310F啊，找到提妲了！\x02\x03",

            "#811F好，\x01",
            "让姐姐来抱抱你……！\x02",
        )
    )

    Jump("loc_7FDB")

    label("loc_7FDB")

    CloseMessageWindow()

    ChrTalk(    #236
        0x107,
        (
            "#067F哎，嘿嘿……\x02\x03",

            "#560F那个，亚妮拉丝姐姐。\x01",
            "待、待会儿再聊吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8147")

    label("loc_8032")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80E1")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x110, 500)

    ChrTalk(    #237
        0x1B,
        "#1310F啊，找到玲了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x110,
        (
            "#263F嘻嘻……\x01",
            "我们马上\x01",
            "就要出发了。\x02\x03",

            "#260F姐姐，\x01",
            "一会儿再聊吧。\x02",
        )
    )

    Jump("loc_80DD")

    label("loc_80DD")

    CloseMessageWindow()
    Jump("loc_8147")

    label("loc_80E1")


    ChrTalk(    #239
        0x1B,
        (
            "#1316F提妲和玲\x01",
            "都不在啊……\x02\x03",

            "#818F嗯，\x01",
            "也许睡得迷迷糊糊的，\x01",
            "就能梦到了吧……\x02",
        )
    )

    Jump("loc_8146")

    label("loc_8146")

    CloseMessageWindow()

    label("loc_8147")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_814F")

    Jump("loc_8D74")

    label("loc_8152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_831B")
    SetChrFlags(0x21, 0x10)
    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8294")
    OP_A2(0x9)

    ChrTalk(    #240
        0x21,
        (
            "#1311F#60W唔，嗯……#20W\x02\x03",

            "#819F#60W啊哈哈，等等我～……#20W\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81EE")

    ChrTalk(    #241
        0x101,
        "#1016F亚、亚妮拉丝……？\x02",
    )

    CloseMessageWindow()

    label("loc_81EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8220")

    ChrTalk(    #242
        0x102,
        "#1514F好像睡着了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8291")

    label("loc_8220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8269")

    ChrTalk(    #243
        0x103,
        (
            "#1526F真是的，\x01",
            "这孩子竟然在这种地方睡觉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8291")

    label("loc_8269")


    ChrTalk(    #244
        0x109,
        (
            "#1068F她到底在\x01",
            "追什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8291")

    Jump("loc_8310")

    label("loc_8294")

    OP_9E(0x21, 0x14, 0x0, 0xC8, 0xBB8)
    Sleep(300)
    OP_9E(0x21, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(200)

    ChrTalk(    #245
        0x21,
        (
            "#1311F#60W好，抓到啦……\x02\x03",

            "这样我就可以去玩偶王国了……⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8310")

    ClearChrFlags(0x21, 0x10)
    TalkEnd(0x21)
    Jump("loc_8D74")

    label("loc_831B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_877D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_END)), "loc_858D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850F")

    ChrTalk(    #246
        0x1B,
        (
            "#814F啊，大家。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x109,
        "#1078F啊，是这么回事……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #248
        (
            "\x07\x05凯文把琥耀石石碑上\x01",
            "记述的语句向亚妮拉丝作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_83D5")

    label("loc_83D5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0x1B,
        (
            "#814F『剑道之少女』……是说我吗！？\x02\x03",

            "#818F唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x109,
        (
            "#1066F没关系，不试试看怎么知道呢。\x02\x03",

            "能陪我们去看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1B,
        (
            "#814F嗯，当然了。\x01",
            "这点小事倒不要紧……\x02\x03",

            "#810F只要做好准备，\x01",
            "我随时都可以加入队伍哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Jump("loc_8587")

    label("loc_850F")


    ChrTalk(    #252
        0x1B,
        (
            "#818F虽然不明白到底怎么回事，\x01",
            "不过似乎是在召唤我……\x02\x03",

            "#810F我已经做好准备了，\x01",
            "随时都可以加入队伍哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8587")

    TalkEnd(0xFE)
    Jump("loc_877A")

    label("loc_858D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 7)), scpexpr(EXPR_END)), "loc_861B")

    ChrTalk(    #253
        0x1B,
        (
            "#1317F没、没想到\x01",
            "竟然有这样强的人……\x02\x03",

            "#1316F唔唔，那招到底是什么啊……\x02\x03",

            "#815F真的是剑技吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_869E")

    label("loc_861B")


    ChrTalk(    #254
        0x1B,
        (
            "#814F菲利普先生，\x01",
            "好像是那个公爵的管家吧。\x02\x03",

            "#818F唔……\x01",
            "之前也和他见过几面……\x02\x03",

            "没想到是这样强的人啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869E")

    OP_A2(0x9)
    Jump("loc_8777")

    label("loc_86A4")


    ChrTalk(    #255
        0x1B,
        (
            "#1316F唉，\x01",
            "我的修行还远远不够……\x02\x03",

            "#812F这样的话……\x01",
            "就再和理查德先生\x01",
            "切磋一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8777")
    TurnDirection(0x1B, 0x10C, 400)
    Sleep(500)

    ChrTalk(    #256
        0x1B,
        (
            "#815F理查德先生，\x01",
            "请你多多指教！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10C,
        "#111F哈哈……我考虑一下。\x02",
    )

    CloseMessageWindow()

    label("loc_8777")

    TalkEnd(0xFE)

    label("loc_877A")

    Jump("loc_8D74")

    label("loc_877D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_8D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89DA")
    TalkBegin(0xFE)

    ChrTalk(    #258
        0x1B,
        (
            "#817F『影之国』──\x02\x03",

            "可以实现人们的愿望，\x01",
            "并根据独立的法则不断进行\x01",
            "自我组织和创建的高位空间……\x02\x03",

            "……………………………………………\x01",
            "……………………………………………\x01",
            "……………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x1B, 0x14, 0x0, 0x320, 0xBB8)
    Sleep(1000)

    ChrTalk(    #259
        0x1B,
        "#819F………呜………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88FC")

    ChrTalk(    #260
        0x101,
        "#1004F啊，崩溃了！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_89D7")

    label("loc_88FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8943")

    ChrTalk(    #261
        0x102,
        (
            "#1512F……亚妮拉丝小姐，\x01",
            "请不要勉强自己。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89D7")

    label("loc_8943")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_898C")

    ChrTalk(    #262
        0x103,
        (
            "#1525F……亚妮拉丝，\x01",
            "不懂的话就不要勉强了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89D7")

    label("loc_898C")


    ChrTalk(    #263
        0x107,
        "#065F啊，亚妮拉丝姐姐……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x109,
        "#1068F哎呀，头晕了……\x02",
    )

    CloseMessageWindow()

    label("loc_89D7")

    Jump("loc_8BDC")

    label("loc_89DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A7E")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #265
        0x1B,
        (
            "#816F呵呵，\x01",
            "玲也很喜欢布娃娃吧。\x02\x03",

            "#811F好，\x01",
            "一会儿来和姐姐聊聊吧。\x02\x03",

            "我要亲自确认一下\x01",
            "你的热爱程度！\x02",
        )
    )

    Jump("loc_8A7A")

    label("loc_8A7A")

    CloseMessageWindow()
    Jump("loc_8BDC")

    label("loc_8A7E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #266
        0x1B,
        (
            "#814F哎，\x01",
            "玲竟然有兰德摩尔的\x01",
            "限定版布娃娃吗！？\x02\x03",

            "#1317F我、我也好想要啊……\x02",
        )
    )

    Jump("loc_8AEA")

    label("loc_8AEA")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B23")

    ChrTalk(    #267
        0x101,
        "#1016F（亚、亚妮拉丝……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B98")

    label("loc_8B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B63")

    ChrTalk(    #268
        0x102,
        "#1512F（我说啊，亚妮拉丝小姐……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B98")

    label("loc_8B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B98")

    ChrTalk(    #269
        0x103,
        "#1525F（这孩子真是的……）\x02",
    )

    CloseMessageWindow()

    label("loc_8B98")


    ChrTalk(    #270
        0x109,
        (
            "#1068F（从某种意义上来说，\x01",
            "  是最没有紧张感的人了……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BDC")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x9)
    TalkEnd(0xFE)
    Jump("loc_8D74")

    label("loc_8BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C79")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #271
        0x1B,
        (
            "#817F到底要怎么做\x01",
            "才能够变出布娃娃啊…………\x02\x03",

            "嗯～…………\x02\x03",

            "#1312F唔…………！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D6C")

    label("loc_8C79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CF9")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #272
        0x1B,
        (
            "#816F玲，\x01",
            "一会儿来和姐姐聊聊吧。\x02\x03",

            "#811F我要亲自确认一下\x01",
            "你的热爱程度！\x02",
        )
    )

    Jump("loc_8CF5")

    label("loc_8CF5")

    CloseMessageWindow()
    Jump("loc_8D6C")

    label("loc_8CF9")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #273
        0x1B,
        (
            "#812F我、我也\x01",
            "看中了那个呢……\x02\x03",

            "#1316F呜呜，那一天突然接到了任务，\x01",
            "所以没来得及去买……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D6C")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_8D74")

    Return()

    # Function_9_797E end

    def Function_10_8D75(): pass

    label("Function_10_8D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_8FC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E47")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DEC")

    ChrTalk(    #274
        0x15,
        (
            "#416F……唔，是这样吗。\x02\x03",

            "#210F还是偶尔把它拆开\x01",
            "清洗一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E39")

    label("loc_8DEC")


    ChrTalk(    #275
        0x15,
        (
            "#213F哎呀，不要勉强了。\x02\x03",

            "#212F总之，\x01",
            "休息一下喝点水吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E39")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x4)
    TalkEnd(0xFE)
    Jump("loc_8FC1")

    label("loc_8E47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F08")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #276
        0x15,
        (
            "#213F啊，约修亚……\x02\x03",

            "#215F那、那个…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x102,
        (
            "#1513F嗯，没关系的。\x02\x03",

            "#1501F谢谢你的担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x15,
        "#414F啊，嗯…………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_8FBE")

    label("loc_8F08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F5D")

    ChrTalk(    #279
        0x15,
        (
            "#210F导力枪内部结构十分精细，\x01",
            "偶尔也要拆开清洗一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FBE")

    label("loc_8F5D")


    ChrTalk(    #280
        0x15,
        (
            "#416F公主殿下，请别累着自己了。\x02\x03",

            "#212F有这么多伙伴在，\x01",
            "没必要一个人去调查……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FBE")

    TalkEnd(0xFE)

    label("loc_8FC1")

    Return()

    # Function_10_8D75 end

    def Function_11_8FC2(): pass

    label("Function_11_8FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_90F6")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9064")

    ChrTalk(    #281
        0x13,
        (
            "#175F这只是我自己的看法……\x02\x03",

            "#170F洛伦斯少尉\x01",
            "是不是也对上校\x01",
            "有过敬佩的感觉呢。\x02\x03",

            "#179F虽然这种想法没什么根据……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_90F0")

    label("loc_9064")


    ChrTalk(    #282
        0x13,
        (
            "#176F我觉得洛伦斯少尉\x01",
            "并不只是单纯地\x01",
            "在利用情报部。\x02\x03",

            "#170F虽然这种想法没什么根据……\x01",
            "不过他实际上\x01",
            "应该是个很诚实的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90F0")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_90F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_9100")
    Jump("loc_A1B2")

    label("loc_9100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_927C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 2)), scpexpr(EXPR_END)), "loc_917E")

    ChrTalk(    #283
        0x13,
        (
            "#179F雾香小姐――\x01",
            "我以前也想过\x01",
            "要和她见一面……\x02\x03",

            "#178F没想到她是那么强的人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F9")

    label("loc_917E")


    ChrTalk(    #284
        0x13,
        (
            "#178F说到雾香小姐，\x01",
            "我听说她一个人\x01",
            "登上了那座里塔……\x02\x03",

            "#179F呼，如果她还在利贝尔，\x01",
            "一定要见上一面才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F9")

    OP_A2(0x2)
    Jump("loc_9276")

    label("loc_91FF")


    ChrTalk(    #285
        0x13,
        (
            "#175F说起来，到达雾香小姐那里\x01",
            "仅仅是试炼的一半吗……\x02\x03",

            "#176F我们最好还是\x01",
            "重新评估一下\x01",
            "当前的战斗力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9276")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_927C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_9554")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9345")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #286
        0x104,
        (
            "#1541F……尤莉亚小姐。\x02\x03",

            "我回国的时候，\x01",
            "真是受你多方照顾了。\x02\x03",

            "#1547F怎么样，\x01",
            "待会儿一起去喝一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x13,
        "#172F哈啊………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_9345")


    ChrTalk(    #288
        0x13,
        (
            "#175F……其实刚才，\x01",
            "奥利维特皇子\x01",
            "邀请我去喝一杯……\x02\x03",

            "#176F唔唔………\x01",
            "到底要不要接受呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9412")

    ChrTalk(    #289
        0x101,
        (
            "#1007F那个皇子真是的……\x02\x03",

            "#1009F尤莉亚小姐，\x01",
            "你最好别理他！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_9412")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9451")

    ChrTalk(    #290
        0x102,
        (
            "#1512F不管怎么说，\x01",
            "还是拒绝了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_9451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9487")

    ChrTalk(    #291
        0x105,
        (
            "#1165F啊哈哈……\x01",
            "唔，嗯……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9487")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94C2")

    ChrTalk(    #292
        0x10D,
        (
            "#272F……上尉，\x01",
            "请一定不要接受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94C2")

    OP_A2(0x2)
    Jump("loc_954E")

    label("loc_94C8")


    ChrTalk(    #293
        0x13,
        (
            "#176F咳、咳……\x02\x03",

            "#178F没想到连菲利普大人\x01",
            "都被再现了出来……\x02\x03",

            "#175F如果可能的话，\x01",
            "我还想向现实中的他讨教呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954E")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_9554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_968C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9612")

    ChrTalk(    #294
        0x13,
        (
            "#179F那位女性幽灵\x01",
            "竟然是利贝尔王家始祖\x01",
            "赛雷斯托大人……\x02\x03",

            "#171F呵呵，这样我就放心了。\x02\x03",

            "#170F借助她的力量，\x01",
            "我们就一定能与\x01",
            "『影之王』对抗了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_9686")

    label("loc_9612")


    ChrTalk(    #295
        0x13,
        (
            "#170F虽然现在还不到\x01",
            "感到乐观的时候……\x02\x03",

            "但如果能借助她的力量，\x01",
            "我们就一定能与\x01",
            "『影之王』对抗了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9686")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_968C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_98E7")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9723")
    Jump("loc_9765")

    label("loc_9723")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_973F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9765")

    label("loc_973F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_975B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9765")

    label("loc_975B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9765")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9856")

    ChrTalk(    #296
        0x13,
        (
            "#176F能够实现人的意念的世界……\x02\x03",

            "#175F唔，\x01",
            "我还觉得有些半信半疑……\x02\x03",

            "不过如果现在的情况\x01",
            "是『影之王』所期望的……\x02\x03",

            "#170F那我们决不能\x01",
            "任他这样妄为下去。\x02",
        )
    )

    Jump("loc_984F")

    label("loc_984F")

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_98DC")

    label("loc_9856")


    ChrTalk(    #297
        0x13,
        (
            "#176F嗯，\x01",
            "我还觉得有些半信半疑……\x02\x03",

            "『影之王』……\x02\x03",

            "#170F他所期望的事情，\x01",
            "我们决不能任其\x01",
            "就这样发生。\x02",
        )
    )

    Jump("loc_98DB")

    label("loc_98DB")

    CloseMessageWindow()

    label("loc_98DC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_98E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_9B76")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF1")

    ChrTalk(    #298
        0x13,
        (
            "#170F理查德大人退役的时候，\x01",
            "摩尔根将军和卡西乌斯准将\x01",
            "都极力挽留他。\x02\x03",

            "虽然理查德大人\x01",
            "曾经不幸误入歧途，\x01",
            "但他的确是位非常优秀的军人。\x02\x03",

            "#179F我还听说卡西乌斯准将\x01",
            "准备采取一些措施\x01",
            "把他请回军队。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A3B")

    ChrTalk(    #299
        0x105,
        "#1165F呵呵，真像卡西乌斯先生的作风。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#1007F果然很爱使唤人啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEB")

    label("loc_9A3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AA3")

    ChrTalk(    #301
        0x102,
        (
            "#1508F……好像又要\x01",
            "把工作推给别人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        "#1007F真是爱使唤人啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEB")

    label("loc_9AA3")


    ChrTalk(    #303
        0x101,
        (
            "#1019F哇，那个不良中年……\x02\x03",

            "#1007F真是爱使唤人啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AEB")

    OP_A2(0x2)
    Jump("loc_9B70")

    label("loc_9AF1")


    ChrTalk(    #304
        0x13,
        (
            "#178F没想到理查德大人\x01",
            "也被卷入了异世界……\x02\x03",

            "#176F唔……\x01",
            "看来将『协力者』牵连进来\x01",
            "是所谓『规则』的一部分吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B70")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_9B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_9C7A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C25")

    ChrTalk(    #305
        0x13,
        (
            "#176F……我之前已经知道\x01",
            "凯文先生的身份\x01",
            "其实是星杯骑士……\x02\x03",

            "#175F但他竟然是守护骑士第五位……\x02\x03",

            "真是没想到是这么厉害的人物……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_9C74")

    label("loc_9C25")


    ChrTalk(    #306
        0x13,
        (
            "#176F守护骑士……\x02\x03",

            "#175F没想到凯文先生\x01",
            "是这么厉害的人物……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C74")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_9C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_9D83")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2C")

    ChrTalk(    #307
        0x13,
        (
            "#178F这样一来，\x01",
            "『庭院之主』所说的\x01",
            "三个修炼场都已经通过了。\x02\x03",

            "接下来应该\x01",
            "去『第五星层』了吧。\x02\x03",

            "#176F那里到底是什么样的地方呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_9D7D")

    label("loc_9D2C")


    ChrTalk(    #308
        0x13,
        (
            "#178F接下来应该是『第五星层』吧……\x02\x03",

            "到底是什么样的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D7D")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_9D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_9F31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E45")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DFB")
    TalkBegin(0xFE)

    ChrTalk(    #309
        0x13,
        (
            "#176F呼，\x01",
            "明天有军队司令部的内部会议……\x02\x03",

            "不能缺席啊……\x02",
        )
    )

    Jump("loc_9DF4")

    label("loc_9DF4")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_9E3F")

    label("loc_9DFB")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #310
        0x13,
        (
            "#178F殿下，\x01",
            "请您也稍微\x01",
            "休息一下吧……？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_9E3F")

    OP_A2(0x2)
    Jump("loc_9F2E")

    label("loc_9E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EEA")
    TalkBegin(0xFE)

    ChrTalk(    #311
        0x13,
        (
            "#172F不，\x01",
            "也许是今天……？\x02\x03",

            "#175F唔，\x01",
            "现在已经没有时间的概念了……\x02\x03",

            "说不定至今为止\x01",
            "已经经过了很多天……\x02",
        )
    )

    Jump("loc_9EE3")

    label("loc_9EE3")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_9F2E")

    label("loc_9EEA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #312
        0x13,
        (
            "#178F殿下，\x01",
            "请您也稍微\x01",
            "休息一下吧……？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_9F2E")

    Jump("loc_A1B2")

    label("loc_9F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_A0A6")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A002")

    ChrTalk(    #313
        0x13,
        (
            "#178F从之前的情况来看，\x01",
            "『影之王』对我们大家的情况\x01",
            "似乎做了很详细的调查。\x02\x03",

            "#175F不过，竟然还再现了\x01",
            "利贝尔之外的地点……\x02\x03",

            "『影之王』……\x01",
            "他到底是什么人…………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_A0A0")

    label("loc_A002")


    ChrTalk(    #314
        0x13,
        (
            "#178F『影之王』对我们大家的情况\x01",
            "似乎做了很详细的调查。\x02\x03",

            "#176F而且还能够操纵『恶魔』……\x02\x03",

            "#175F『影之王』……\x01",
            "他到底是什么人…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0A0")

    TalkEnd(0xFE)
    Jump("loc_A1B2")

    label("loc_A0A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_A1B2")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A142")

    ChrTalk(    #315
        0x13,
        (
            "#176F炼狱的镜子和战车……\x01",
            "和圣典中描绘的一模一样。\x02\x03",

            "#175F敌人能够伪造整个王都。\x01",
            "这种程度的事情就跟把戏一样吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_A1AF")

    label("loc_A142")


    ChrTalk(    #316
        0x13,
        (
            "#178F我听过大司教的讲义，\x01",
            "也知道一些\x01",
            "关于圣典的内容……\x02\x03",

            "#175F没想到会出现\x01",
            "那样的东西……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1AF")

    TalkEnd(0xFE)

    label("loc_A1B2")

    Return()

    # Function_11_8FC2 end

    def Function_12_A1B3(): pass

    label("Function_12_A1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_A383")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A26B")

    ChrTalk(    #317
        0x14,
        (
            "#270F……看来已经\x01",
            "找到了前进的方向。\x02\x03",

            "#270F就算是为了逝去的人们，\x01",
            "我们也必须前进。\x02\x03",

            "#278F『第七星层』……\x01",
            "去拜访一下\x01",
            "这世界的根源吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_A37D")

    label("loc_A26B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A31B")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #318
        0x14,
        (
            "#277F……看来已经\x01",
            "找到了前进的方向。\x02\x03",

            "#276F奥利维尔，要小心行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x104,
        "#1541F呵，遵命大哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x14,
        "#274F……谁是大哥啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A37D")

    label("loc_A31B")


    ChrTalk(    #321
        0x14,
        (
            "#277F……看来已经\x01",
            "找到了前进的方向。\x02\x03",

            "#278F差不多该把\x01",
            "奥利维尔那家伙拽过来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A37D")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_A383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_A45B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 2)), scpexpr(EXPR_END)), "loc_A3FD")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #322
        0x14,
        (
            "#276F那就是将自己的路贯彻到底的人物吗……\x02\x03",

            "#278F呼……\x01",
            "我还差得很远。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_A458")

    label("loc_A3FD")

    TalkBegin(0xFE)

    ChrTalk(    #323
        0x14,
        (
            "#272F传说中的『剑圣』之技……\x02\x03",

            "#277F嗯……\x01",
            "我也想亲眼见识一下呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_A458")

    Jump("loc_B6A1")

    label("loc_A45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_A56C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A500")

    ChrTalk(    #324
        0x14,
        (
            "#276F『影之王』那小子……\x01",
            "看来手段还真不简单。\x02\x03",

            "#272F话说回来，\x01",
            "已经见过两名『守护者』……\x02\x03",

            "呼，还会有谁出场呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_A566")

    label("loc_A500")


    ChrTalk(    #325
        0x14,
        (
            "#270F『影之王』的手段\x01",
            "看来还真不简单。\x02\x03",

            "#276F对了，\x01",
            "那个『黑骑士』也自称守护者……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A566")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_A56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_A782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A652")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #326
        0x14,
        (
            "#272F……奥利维尔，别引起麻烦。\x02\x03",

            "虽然这里是异空间，\x01",
            "但你的奇怪行动也会造成国际问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x104,
        "#1541F哈哈哈，你还真是爱操心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x14,
        "#274F……给我老实听着。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_A6A5")

    label("loc_A652")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #329
        0x14,
        (
            "#274F…………这个赖皮蛋\x02\x03",

            "就交给我来教训一下吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_A6A5")

    OP_A2(0x3)
    Jump("loc_A77F")

    label("loc_A6AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A730")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #330
        0x14,
        (
            "#272F……奥利维尔，别引起麻烦。\x02\x03",

            "虽然这里是异空间，\x01",
            "但你的奇怪行动也会造成国际问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A77C")

    label("loc_A730")


    ChrTalk(    #331
        0x14,
        (
            "#272F……请不要理睬\x01",
            "这个家伙。\x02\x03",

            "#270F我会好好\x01",
            "看着他的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A77C")

    TalkEnd(0xFE)

    label("loc_A77F")

    Jump("loc_B6A1")

    label("loc_A782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_A929")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A870")

    ChrTalk(    #332
        0x14,
        (
            "#276F那个『方石』，\x01",
            "原来是这么一个来头啊……\x02\x03",

            "这样一来，\x01",
            "就可以说明我们\x01",
            "怎么会被吸进『影之国』了。\x02\x03",

            "#270F但是做出这件事的\x01",
            "似乎是『影之王』。\x02\x03",

            "#272F哼，\x01",
            "真想早点把他揪出来……\x02",
        )
    )

    Jump("loc_A869")

    label("loc_A869")

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_A923")

    label("loc_A870")


    ChrTalk(    #333
        0x14,
        (
            "#272F『雷克鲁斯方石』……\x01",
            "这样就可以说明我们\x01",
            "怎么会被吸进『影之国』了。\x02\x03",

            "#276F……但是做出这件事的\x01",
            "似乎是『影之王』。\x02\x03",

            "哼，\x01",
            "真想早点把他揪出来……\x02",
        )
    )

    Jump("loc_A922")

    label("loc_A922")

    CloseMessageWindow()

    label("loc_A923")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_A929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_AA59")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9EE")

    ChrTalk(    #334
        0x14,
        (
            "#272F……事态似乎比\x01",
            "想像中还要严重。\x02\x03",

            "#276F如果这个世界\x01",
            "以及那些奇怪的『规则』\x01",
            "是『影之王』制造出来的……\x02\x03",

            "那么说不定我们\x01",
            "永远也无法逃出这个空间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_AA53")

    label("loc_A9EE")


    ChrTalk(    #335
        0x14,
        (
            "#272F……唯一的希望是那位女性幽灵。\x02\x03",

            "#276F『影之王』的力量\x01",
            "似乎还达不到这座庭院。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA53")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_AA59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_AB88")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB1D")

    ChrTalk(    #336
        0x14,
        (
            "#277F原王国军情报部上校\x01",
            "亚兰·理查德……\x02\x03",

            "我听说他的剑法是师从『剑圣』，\x01",
            "并且在智力战、谍报战上\x01",
            "也有相当的水准。\x02\x03",

            "#278F呼……不能轻易与之为敌啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_AB82")

    label("loc_AB1D")


    ChrTalk(    #337
        0x14,
        (
            "#277F原王国军情报部上校\x01",
            "亚兰·理查德……\x02\x03",

            "有他加入的话，\x01",
            "真是再强不过的战斗力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB82")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_AB88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_ADA5")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC1F")
    Jump("loc_AC61")

    label("loc_AC1F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC3B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC61")

    label("loc_AC3B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC57")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC61")

    label("loc_AC57")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC61")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD40")

    ChrTalk(    #338
        0x14,
        (
            "#272F星杯骑士团吗……\x02\x03",

            "奥利维尔曾经凭一时热心\x01",
            "调查过相关的资料，\x01",
            "但详细情况还是不太清楚。\x02\x03",

            "#276F不过见识过那种力量后，\x01",
            "我也理解他为什么要调查了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_AD9A")

    label("loc_AD40")


    ChrTalk(    #339
        0x14,
        (
            "#276F能够一瞬间\x01",
            "打倒那种『恶魔』的能力……\x02\x03",

            "叫做『异能』更为恰当吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD9A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_ADA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_AFB4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE52")

    ChrTalk(    #340
        0x14,
        (
            "#276F……说起来，\x01",
            "奥利维尔那家伙到哪里去了呢。\x02\x03",

            "#272F真是的，\x01",
            "一不注意就……\x02\x03",

            "在异空间里面\x01",
            "也不知道老实一点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AED7")

    label("loc_AE52")


    ChrTalk(    #341
        0x14,
        (
            "#276F在协会设施里的封印石角色就是游击士……吗 。\x02\x03",

            "原来如此，还真是遵守规则啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#1503F…………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_AED7")

    OP_A2(0x3)
    Jump("loc_AFAE")

    label("loc_AEDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF46")

    ChrTalk(    #343
        0x14,
        (
            "#272F哼……\x01",
            "暂时休息一下吧。\x02\x03",

            "不拿着『方石』\x01",
            "就走出庭院\x01",
            "是很危险的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFAE")

    label("loc_AF46")


    ChrTalk(    #344
        0x14,
        (
            "#270F那些带着面具的……\x01",
            "还真是遵守规则啊。\x02\x03",

            "#276F……如果能从这一点上\x01",
            "找到他们的弱点就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFAE")

    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_AFB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_B1D0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B04B")
    Jump("loc_B08D")

    label("loc_B04B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B067")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B08D")

    label("loc_B067")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B083")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B08D")

    label("loc_B083")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B08D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B142")

    ChrTalk(    #345
        0x14,
        (
            "#276F拥有武装的魔兽和『兽人』……\x01",
            "这也是『影之王』的爱好吗。\x02\x03",

            "#272F…………真无聊啊。\x02\x03",

            "赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_B1C5")

    label("loc_B142")


    ChrTalk(    #346
        0x14,
        (
            "#272F不知道『影之王』\x01",
            "到底在打什么算盘……\x02\x03",

            "不过我可没有一直\x01",
            "和他玩下去的闲工夫。\x02\x03",

            "#270F赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C5")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_B6A1")

    label("loc_B1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_B4A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40E")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B27D")
    Jump("loc_B2BF")

    label("loc_B27D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B299")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2BF")

    label("loc_B299")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2B5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2BF")

    label("loc_B2B5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2BF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3CF")

    ChrTalk(    #347
        0x14,
        "#272F……奥利维尔，一会儿来找我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x104,
        (
            "#1540F呵呵，怎么了穆拉君。\x02\x03",

            "#1541F难不成，\x01",
            "是要向我告白吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x14,
        (
            "#270F别说废话了。\x01",
            "是要确认你周围的情况。\x02\x03",

            "#276F包括被吸进\x01",
            "异空间之前的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_B3FE")

    label("loc_B3CF")


    ChrTalk(    #350
        0x14,
        (
            "#272F……奥利维尔，\x01",
            "可别得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3FE")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_B4A1")

    label("loc_B40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B41D")
    Call(5, 5)
    Jump("loc_B4A1")

    label("loc_B41D")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #351
        0x14,
        (
            "#276F我们被困在这里，\x01",
            "外面的世界还不知道变成什么样呢……\x02\x03",

            "#272F……一定得赶快\x01",
            "找到逃出去的办法。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_B4A1")

    Jump("loc_B6A1")

    label("loc_B4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_B6A1")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B621")

    ChrTalk(    #352
        0x14,
        (
            "#270F……从大家所说的情况来看，\x01",
            "每个人都是在同一时刻被吸进来的。\x02\x03",

            "#272F我还一直在担心\x01",
            "如果只有我先被吸进来，\x01",
            "那个赖皮蛋会在外面如何肆意妄为呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x102,
        "#1505F……我很理解这种心情。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61B")

    ChrTalk(    #354
        0x104,
        (
            "#1542F……真没礼貌。\x02\x03",

            "#1541F顶多也就是好好享受一下\x01",
            "整个晚上的甜美宴会而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x14,
        "#274F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_B61B")

    OP_A2(0x3)
    Jump("loc_B69E")

    label("loc_B621")


    ChrTalk(    #356
        0x14,
        (
            "#272F看来我们大家是在\x01",
            "同一时刻被吸进来的。\x02\x03",

            "虽然这么说有些对不起被吸进来的人，\x01",
            "但我觉得真是不幸中的万幸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B69E")

    TalkEnd(0xFE)

    label("loc_B6A1")

    Return()

    # Function_12_A1B3 end

    def Function_13_B6A2(): pass

    label("Function_13_B6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_B8DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B841")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B74F")
    TalkBegin(0xFE)

    ChrTalk(    #357
        0x20,
        (
            "#265F埃尔赛尤\x01",
            "是那艘漂亮的白色飞船吧？\x02\x03",

            "#261F嘻嘻，\x01",
            "玲以前也很想乘坐看看呢。\x02\x03",

            "从甲板上眺望的话\x01",
            "肯定非常舒服吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B83B")

    label("loc_B74F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x11, 400)
    Sleep(300)

    ChrTalk(    #358
        0x20,
        (
            "#264F哎呀，姐姐……\x02\x03",

            "#260F偷吃可是不好的哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x11, 255)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)
    TurnDirection(0x11, 0x20, 600)
    Sleep(200)

    ChrTalk(    #359
        0x11,
        (
            "#1933F刚、刚刚\x01",
            "我才没有偷吃。\x02\x03",

            "#1940F……只是试试味道而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)

    label("loc_B83B")

    OP_A2(0x6)
    Jump("loc_B8D1")

    label("loc_B841")

    TalkBegin(0xFE)

    ChrTalk(    #360
        0x20,
        (
            "#265F玲啊，\x01",
            "好想赶快乘坐埃尔赛尤号啊。\x02\x03",

            "#261F嘻嘻，\x01",
            "赶快做好准备出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8D1")

    ChrTalk(    #361
        0x109,
        "#1066F是要去露营吗……\x02",
    )

    CloseMessageWindow()

    label("loc_B8D1")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_EF95")

    label("loc_B8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_DECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDFC")
    EventBegin(0x0)
    OP_4A(0x20, 255)
    OP_4A(0x11, 255)
    OP_4A(0x1E, 255)
    SetChrPos(0x11, 93410, -14000, -52280, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD37")
    Fade(500)
    OP_6D(97110, -14000, -51710, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(48000, 0)
    OP_6E(476, 0)
    SetChrPos(0xEE, 95350, -14000, -52580, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9AF")
    SetChrPos(0xEF, 94630, -14000, -54700, 45)
    SetChrPos(0xF0, 94280, -14000, -51660, 90)
    SetChrPos(0xF1, 93340, -14000, -53740, 90)
    Jump("loc_BA34")

    label("loc_B9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F3")
    SetChrPos(0xF0, 94630, -14000, -54700, 45)
    SetChrPos(0xEF, 94280, -14000, -51660, 90)
    SetChrPos(0xF1, 93340, -14000, -53740, 90)
    Jump("loc_BA34")

    label("loc_B9F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA34")
    SetChrPos(0xF1, 94630, -14000, -54700, 45)
    SetChrPos(0xEF, 94280, -14000, -51660, 90)
    SetChrPos(0xF0, 93340, -14000, -53740, 90)

    label("loc_BA34")

    TurnDirection(0x20, 0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0x109,
        (
            "#1079F#6P哎呀，玲。\x01",
            "在这种地方做什么呢……？\x02\x03",

            "#1066F啊，难道，\x01",
            "是在推测下一个『守护者』的身份？\x02\x03",

            "#1068F唔，\x01",
            "要是能推算出他的技能和特性\x01",
            "就真是帮大忙了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x20,
        (
            "#263F#11P嘻嘻，是啊。\x02\x03",

            "#269F『影之王』的人选\x01",
            "也真是有趣……\x02\x03",

            "#265F在下一个童话王国中\x01",
            "到底会有谁登场呢。\x02\x03",

            "#261F真期待⊙ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x109,
        (
            "#1061F#6P期、期待…………\x02\x03",

            "#1066F不是在推测吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x20,
        (
            "#264F#11P哎呀，要是这样做了的话\x01",
            "多无聊啊。\x02\x03",

            "#1305F本来童话就是要怀着\x01",
            "期待的心情才有意思嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)

    ChrTalk(    #366
        0x10F,
        (
            "#1446F#12P……从刚才起\x01",
            "我就想说了。\x02\x03",

            "#1805F你是不是有点太不谨慎了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_BCD0():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BCD0)

    def lambda_BCDE():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BCDE)

    def lambda_BCEC():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BCEC)

    def lambda_BCFA():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BCFA)
    TurnDirection(0x20, 0x10F, 400)
    Sleep(200)

    ChrTalk(    #367
        0x20,
        "#264F#11P不谨慎…………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7F8")

    label("loc_BD37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_C099")
    Fade(500)
    OP_6D(88090, -14000, -51890, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(47000, 0)
    OP_6E(512, 0)
    SetChrPos(0xEE, 84050, -14000, -53200, 90)
    SetChrPos(0xEF, 84000, -14000, -51820, 90)
    SetChrPos(0xF0, 82700, -14000, -53630, 90)
    SetChrPos(0xF1, 82660, -14000, -51800, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #368
        0x11,
        (
            "#1446F#6P……从刚才起\x01",
            "我就想说了。\x02\x03",

            "#1805F你是不是有点太不谨慎了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x20,
        "#264F#12P不谨慎…………？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6E")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BED5")

    label("loc_BE6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE96")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BED5")

    label("loc_BE96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEBE")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BED5")

    label("loc_BEBE")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_BED5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF02")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BF69")

    label("loc_BF02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2A")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BF69")

    label("loc_BF2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF52")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BF69")

    label("loc_BF52")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_BF69")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF96")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BFFD")

    label("loc_BF96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFBE")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BFFD")

    label("loc_BFBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE6")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BFFD")

    label("loc_BFE6")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_BFFD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C02A")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C091")

    label("loc_C02A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C052")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C091")

    label("loc_C052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C07A")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C091")

    label("loc_C07A")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C091")

    Sleep(1000)
    Jump("loc_C7F8")

    label("loc_C099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_C440")
    Fade(500)
    OP_6D(93730, -14000, -51100, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(51000, 0)
    OP_6E(394, 0)
    SetChrPos(0xEE, 87290, -14000, -53260, 270)
    SetChrPos(0xEF, 87420, -14000, -51850, 270)
    SetChrPos(0xF0, 88980, -14000, -53460, 270)
    SetChrPos(0xF1, 89350, -14000, -52010, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #370
        0x11,
        (
            "#1446F#6P……从刚才起\x01",
            "我就想说了。\x02\x03",

            "#1805F你是不是有点太不谨慎了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x20,
        "#264F#11P不谨慎…………？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1D0")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C237")

    label("loc_C1D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1F8")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C237")

    label("loc_C1F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C220")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C237")

    label("loc_C220")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C237")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C264")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C2CB")

    label("loc_C264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28C")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C2CB")

    label("loc_C28C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2B4")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C2CB")

    label("loc_C2B4")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C2CB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2F8")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C35F")

    label("loc_C2F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C320")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C35F")

    label("loc_C320")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C348")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C35F")

    label("loc_C348")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C35F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C38C")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C3F3")

    label("loc_C38C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3B4")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C3F3")

    label("loc_C3B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3DC")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C3F3")

    label("loc_C3DC")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C3F3")

    Sleep(1000)

    def lambda_C3FE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_C3FE)
    Sleep(50)

    def lambda_C411():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C411)
    Sleep(50)

    def lambda_C424():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_C424)
    Sleep(50)
    OP_8C(0xF1, 90, 400)
    Sleep(300)
    Jump("loc_C7F8")

    label("loc_C440")

    Fade(500)
    OP_6D(97110, -14000, -51710, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(48000, 0)
    OP_6E(476, 0)
    SetChrPos(0xEE, 95350, -14000, -52580, 90)
    SetChrPos(0xEF, 94480, -14000, -51660, 90)
    SetChrPos(0xF0, 94630, -14000, -54700, 45)
    SetChrPos(0xF1, 93370, -14000, -53970, 90)
    SetChrPos(0x11, 93000, -14000, -52320, 90)
    TurnDirection(0x20, 0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #372
        0x109,
        (
            "#1079F#6P哎呀，玲。\x01",
            "在这种地方做什么呢……？\x02\x03",

            "#1066F啊，难道，\x01",
            "是在推测下一个『守护者』的身份？\x02\x03",

            "#1068F唔，\x01",
            "要是能推算出他的技能和特性\x01",
            "就真是帮大忙了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x20,
        (
            "#263F#11P嘻嘻，是啊。\x02\x03",

            "#269F『影之王』的人选\x01",
            "也真是有趣……\x02\x03",

            "#265F在下一个童话王国中\x01",
            "到底会有谁登场呢。\x02\x03",

            "#261F真期待⊙ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x109,
        (
            "#1061F#6P期、期待…………\x02\x03",

            "#1066F不是在推测吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x20,
        (
            "#264F#11P哎呀，要是这样做了的话\x01",
            "多无聊啊。\x02\x03",

            "#1305F本来童话就是要怀着\x01",
            "期待的心情才有意思嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C6E9():
        OP_6D(96000, -14000, -51710, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_C6E9)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)
    WaitChrThread(0xEE, 0x3)

    ChrTalk(    #376
        0x11,
        (
            "#1446F#6P……从刚才起\x01",
            "我就想说了。\x02\x03",

            "#1805F你是不是有点太不谨慎了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_C78F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C78F)

    def lambda_C79D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C79D)

    def lambda_C7AB():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C7AB)

    def lambda_C7B9():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C7B9)
    TurnDirection(0x20, 0x11, 400)
    Sleep(400)

    ChrTalk(    #377
        0x20,
        "#264F#11P不谨慎…………？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    label("loc_C7F8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x20, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C822")
    SetChrFlags(0x10F, 0x8)
    ClearChrFlags(0x11, 0x80)

    label("loc_C822")

    SetChrPos(0x11, 94850, -14000, -52390, 90)
    SetChrPos(0xEE, 93550, -14000, -53440, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8EE")
    SetChrPos(0xEF, 94850, -14000, -52390, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C896")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)
    Jump("loc_C8EB")

    label("loc_C896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C9")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    Jump("loc_C8EB")

    label("loc_C8C9")

    SetChrPos(0xF0, 91700, -14000, -52850, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)

    label("loc_C8EB")

    Jump("loc_CB41")

    label("loc_C8EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C998")
    SetChrPos(0xF0, 94630, -14000, -54700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C940")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)
    Jump("loc_C995")

    label("loc_C940")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C973")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    Jump("loc_C995")

    label("loc_C973")

    SetChrPos(0xEF, 91700, -14000, -52850, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)

    label("loc_C995")

    Jump("loc_CB41")

    label("loc_C998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA42")
    SetChrPos(0xF1, 94630, -14000, -54700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9EA")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    Jump("loc_CA3F")

    label("loc_C9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA1D")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    Jump("loc_CA3F")

    label("loc_CA1D")

    SetChrPos(0xEF, 91700, -14000, -52850, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)

    label("loc_CA3F")

    Jump("loc_CB41")

    label("loc_CA42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA86")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)
    Jump("loc_CB41")

    label("loc_CA86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CACA")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)
    Jump("loc_CB41")

    label("loc_CACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB0E")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    SetChrPos(0xF0, 91700, -14000, -52850, 90)
    Jump("loc_CB41")

    label("loc_CB0E")

    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)

    label("loc_CB41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB71")
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 92780, -14000, -51830, 90)
    OP_44(0x1E, 0xFF)
    Jump("loc_CB82")

    label("loc_CB71")

    SetChrPos(0x1E, 80540, -13100, -52040, 90)

    label("loc_CB82")

    OP_6D(94920, -14000, -51020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(315000, 0)
    OP_6E(406, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #378
        0x11,
        (
            "#1446F#5P从之前的情况来看，\x01",
            "『影之王』明显是我们的敌人。\x02\x03",

            "虽然只是虚拟人格，\x01",
            "但『影之王』还利用了那么多人。\x02\x03",

            "#1443F面对这样的事态，\x01",
            "你还能够用开玩笑的语气说话，\x01",
            "是不是有点弄错形势了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #379
        0x109,
        "#1079F#5P莉、莉丝…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x20,
        (
            "#262F#12P……………………………………\x02\x03",

            "#268F这位姐姐，你为什么要生气呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x11,
        (
            "#1446F#5P……我并没有\x01",
            "生什么气。\x02\x03",

            "#1445F只不过是想说\x01",
            "『王』是我们的敌人。\x02\x03",

            "#1443F肯定那家伙做法的言论\x01",
            "我是无法认同的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x20,
        (
            "#263F#12P呼………………\x02\x03",

            "#260F说起来，\x01",
            "『影之王』也一直在挑衅呢……\x02\x03",

            "#261F嘻嘻，这是不是\x01",
            "让姐姐变得如此焦躁不安的原因呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #383
        0x11,
        "#1441F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x20,
        (
            "#263F#12P……对了，『影之王』似乎对\x01",
            "『异端制裁者』很感兴趣呢。\x02\x03",

            "但好像姐姐你\x01",
            "对这些事情并不是很清楚……\x02\x03",

            "#1306F嘻嘻……\x01",
            "是不是因为这个才发怒的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x109,
        "#1067F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x11,
        (
            "#1443F#5P………………………………\x02\x03",

            "#1446F我只是想请你不要忘了。\x01",
            "这可不是闹着玩的。\x02\x03",

            "#1805F就算你是天才，\x01",
            "以为自己什么都懂\x01",
            "那也只不过是自鸣得意而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x1E, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D23D")

    NpcTalk(    #387
        0x1E,
        "声音",
        (
            "#4P……好了好了，\x01",
            "你们俩都给我打住。\x02",
        )
    )

    Jump("loc_D084")

    label("loc_D084")

    CloseMessageWindow()

    def lambda_D08B():
        OP_6D(90000, -14000, -51430, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D08B)
    OP_43(0x1E, 0x0, 0x5, 0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0C3")
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_D0C3")

    OP_62(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0F9")
    OP_62(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_D0F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D118")
    OP_62(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_D118")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D13C")
    OP_62(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_D13C")

    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D159():

        label("loc_D159")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D159")

    QueueWorkItem2(0x0, 0, lambda_D159)

    def lambda_D16A():

        label("loc_D16A")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D16A")

    QueueWorkItem2(0x1, 0, lambda_D16A)

    def lambda_D17B():

        label("loc_D17B")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D17B")

    QueueWorkItem2(0x2, 0, lambda_D17B)

    def lambda_D18C():

        label("loc_D18C")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D18C")

    QueueWorkItem2(0x3, 0, lambda_D18C)

    def lambda_D19D():

        label("loc_D19D")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D19D")

    QueueWorkItem2(0x11, 0, lambda_D19D)

    def lambda_D1AE():

        label("loc_D1AE")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D1AE")

    QueueWorkItem2(0x20, 0, lambda_D1AE)
    WaitChrThread(0xEE, 0x3)
    Sleep(1000)

    def lambda_D1C9():
        OP_6D(95010, -14000, -50480, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D1C9)

    def lambda_D1E1():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_D1E1)

    def lambda_D1F9():
        OP_6B(2160, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_D1F9)

    def lambda_D209():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_D209)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0xEE, 0x3)
    OP_44(0x20, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    OP_44(0x2, 0x0)
    OP_44(0x3, 0x0)
    Sleep(200)
    Jump("loc_D388")

    label("loc_D23D")


    def lambda_D243():
        OP_6D(94660, -14000, -50260, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D243)

    def lambda_D25B():
        OP_67(0, 5350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_D25B)

    def lambda_D273():
        OP_6B(2160, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_D273)

    def lambda_D283():
        OP_6C(327000, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_D283)
    SetChrFlags(0x1E, 0x40)

    def lambda_D298():
        OP_8E(0xFE, 0x16F12, 0xFFFFC950, 0xFFFF38A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_D298)
    WaitChrThread(0x1E, 0x0)

    def lambda_D2B8():
        OP_8E(0xFE, 0x17552, 0xFFFFC950, 0xFFFF3936, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_D2B8)

    def lambda_D2D3():

        label("loc_D2D3")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D2D3")

    QueueWorkItem2(0x0, 0, lambda_D2D3)

    def lambda_D2E4():

        label("loc_D2E4")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D2E4")

    QueueWorkItem2(0x1, 0, lambda_D2E4)

    def lambda_D2F5():

        label("loc_D2F5")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D2F5")

    QueueWorkItem2(0x2, 0, lambda_D2F5)

    def lambda_D306():

        label("loc_D306")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_D306")

    QueueWorkItem2(0x3, 0, lambda_D306)
    WaitChrThread(0x1E, 0x0)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    OP_44(0x2, 0x0)
    OP_44(0x3, 0x0)
    OP_8C(0x1E, 180, 800)
    ClearChrFlags(0x1E, 0x40)
    WaitChrThread(0xEE, 0x3)

    ChrTalk(    #388
        0x1E,
        (
            "#1007F#5P……好了好了，\x01",
            "你们俩都给我打住。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D374():
        TurnDirection(0xFE, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D374)
    Sleep(100)
    TurnDirection(0x11, 0x1E, 400)

    label("loc_D388")


    ChrTalk(    #389
        0x1E,
        (
            "#1009F#11P你们两个……\x01",
            "该适可而止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 135, 400)
    Sleep(300)

    ChrTalk(    #390
        0x1E,
        (
            "#1019F#5P玲，\x01",
            "莉丝小姐她也有自己的隐情，\x01",
            "别再用这种口气和她说话了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 180, 400)
    Sleep(300)

    ChrTalk(    #391
        0x1E,
        (
            "#1007F#11P莉丝小姐也是。\x02\x03",

            "#1002F总说天才什么的，\x01",
            "玲只不过是个\x01",
            "普通的女孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #392
        0x20,
        "#264F#12P…………哎……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x11,
        (
            "#1443F#6P………………………………\x02\x03",

            "#1446F我不明白\x01",
            "你想说什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x1E,
        (
            "#1003F#11P那个，莉丝小姐。\x02\x03",

            "#1002F玲的确很聪明，\x01",
            "又拥有了不起的力量。\x02\x03",

            "但是我认为这和她\x01",
            "是不是一个普通的女孩子\x01",
            "没有关系。\x02\x03",

            "#1007F又任性又得意，\x01",
            "总爱学大人装成熟，\x01",
            "把什么都看得很有趣……\x02\x03",

            "#1006F但是却很会照顾人，\x01",
            "也会为别人担心。\x02\x03",

            "#1016F看，不就是和主日学校的\x01",
            "普通女孩子一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x11,
        "#1802F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x20,
        "#1307F#12P………艾丝蒂尔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x1E,
        (
            "#1025F#11P所以……\x01",
            "请不要武断地认为\x01",
            "玲是特别的。\x02\x03",

            "#1007F如果你觉得为了这些事情\x01",
            "值得去教训一个普通孩子，\x01",
            "那倒也无所谓……\x02\x03",

            "#1003F但我听了莉丝小姐的说法以后，\x01",
            "只觉得你有些过于片面了…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x11,
        (
            "#1445F#6P…………………………………\x02\x03",

            "#1446F是啊……\x01",
            "也许正如你说的，\x01",
            "我的确对她有些偏见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x20, 400)
    Sleep(300)

    ChrTalk(    #399
        0x11,
        "#1446F#5P……对不起，玲。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x11, 400)
    Sleep(300)

    ChrTalk(    #400
        0x20,
        (
            "#269F#12P哎呀……\x01",
            "姐姐，你还真直率。\x02\x03",

            "#263F……不过看来\x01",
            "你还是有一堆话要和玲说对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x11,
        (
            "#1447F#5P当然。\x02\x03",

            "#1448F教育不明事理的孩子\x01",
            "是年长者的义务。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x20, 400)
    Sleep(300)

    ChrTalk(    #402
        0x1E,
        (
            "#1006F#5P啊，那我也同意。\x02\x03",

            "只要玲还在这里，\x01",
            "那我们就算是她的监护人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x20,
        (
            "#266F#12P哼……\x01",
            "随你们怎么想。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x1E, 400)
    Sleep(300)

    ChrTalk(    #404
        0x20,
        (
            "#262F#12P……对了，艾丝蒂尔。\x02\x03",

            "你刚才说\x01",
            "玲就像主日学校里的\x01",
            "普通孩子对吧。\x02",
        )
    )

    Jump("loc_D9FB")

    label("loc_D9FB")

    CloseMessageWindow()

    ChrTalk(    #405
        0x1E,
        "#1011F#5P啊……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x20,
        (
            "#266F#12P虽然怎么想\x01",
            "是艾丝蒂尔自己的事情……\x02\x03",

            "不过我还是要纠正一点。\x02\x03",

            "#269F……玲可不是被教育的对象，\x01",
            "而是教育别人的身份哦。\x02\x03",

            "因为，\x01",
            "我已经有三个博士学位啦。\x02",
        )
    )

    Jump("loc_DAE7")

    label("loc_DAE7")

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #407
        0x1E,
        "#1004F#5P#3S…………哎。#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #408
        0x11,
        "#1444F#5P………什么………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x20,
        (
            "#263F#12P化学、数学和情报理论……\x01",
            "而且我还会定期发表论文哦。\x02\x03",

            "#1305F只不过因为害怕引起轰动\x01",
            "而都是让代理人去发表的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x1E,
        (
            "#1016F#5P哈、哈哈……\x01",
            "是吗……\x02",
        )
    )

    Jump("loc_DC5E")

    label("loc_DC5E")

    CloseMessageWindow()

    ChrTalk(    #411
        0x11,
        (
            "#1446F#5P（这样吗……\x01",
            "  看来要教育她还真是挺难的。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_30(0x1)
    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCDF")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrFlags(0x1E, 0x80)
    Jump("loc_DCE2")

    label("loc_DCDF")

    OP_85(0x1E)

    label("loc_DCE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCF5")
    ClearChrFlags(0x10F, 0x8)

    label("loc_DCF5")

    SetChrFlags(0x11, 0x80)
    SetChrPos(0x20, 97450, -14000, -47720, 37)
    OP_4B(0x20, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x11, 255)
    OP_43(0x20, 0x0, 0x6, 0x2)
    OP_43(0x1E, 0x0, 0x6, 0x2)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_6D(95860, -14000, -52680, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 95860, -14000, -52680, 90)
    SetChrPos(0x1, 95860, -14000, -52680, 90)
    SetChrPos(0x2, 95860, -14000, -52680, 90)
    SetChrPos(0x3, 95860, -14000, -52680, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    SetMapFlags(0x80)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x80)
    OP_A2(0x2668)
    Jump("loc_DEC7")

    label("loc_DDFC")

    TalkBegin(0xFE)

    ChrTalk(    #412
        0x20,
        (
            "#266F呼……\x01",
            "可不要小看玲哦。\x02\x03",

            "#262F如果没有玲帮忙的话，\x01",
            "不管过多长时间\x01",
            "你们也可能无法逃出这里哦？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEC4")

    ChrTalk(    #413
        0x101,
        (
            "#1007F啊，我知道啦。\x02\x03",

            "#1006F那就拜托你了，玲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC4")

    TalkEnd(0xFE)

    label("loc_DEC7")

    Jump("loc_EF95")

    label("loc_DECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_E332")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFEA")
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF80")
    Jump("loc_DFC2")

    label("loc_DF80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF9C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFC2")

    label("loc_DF9C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFB8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFC2")

    label("loc_DFB8")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFC2")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jump("loc_E0E1")

    label("loc_DFEA")

    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x12, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E07A")
    Jump("loc_E0BC")

    label("loc_E07A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E096")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E0BC")

    label("loc_E096")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0B2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E0BC")

    label("loc_E0B2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E0BC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_E0E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E28B")

    ChrTalk(    #414
        0x20,
        (
            "#263F竟然还再现了\x01",
            "那位细眼的爷爷……\x02\x03",

            "#269F呵呵，\x01",
            "『影之王』还真是懂得游戏的乐趣啊。\x02\x03",

            "……真想早点跟他决一胜负呢。\x02\x03",

            "#261F干脆偷偷地\x01",
            "抢先一步行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1FC")

    ChrTalk(    #415
        0x107,
        (
            "#562F真、真是的……\x02\x03",

            "外面很危险的，\x01",
            "千万不要单独出去哦？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E248")

    label("loc_E1FC")


    ChrTalk(    #416
        0x12,
        (
            "#562F真、真是的……\x02\x03",

            "外面很危险的，\x01",
            "千万不要单独出去哦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E248")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E285")

    ChrTalk(    #417
        0x10F,
        "#1440F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_E285")

    OP_A2(0x0)
    Jump("loc_E31E")

    label("loc_E28B")


    ChrTalk(    #418
        0x20,
        (
            "#266F玲啊，\x01",
            "觉得看家最无聊了。\x02\x03",

            "#265F干脆偷偷地\x01",
            "抢先一步行动吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E31E")

    ChrTalk(    #419
        0x10F,
        "#1440F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_E31E")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF95")

    label("loc_E332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_E44D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3DD")

    ChrTalk(    #420
        0x20,
        (
            "#260F要说布娃娃的话，\x01",
            "玲也有很多呢。\x02\x03",

            "房间里到处都堆满了，\x01",
            "就像被埋起来一样。\x02\x03",

            "#261F嘻嘻，真想让\x01",
            "提妲和姐姐看看呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_E442")

    label("loc_E3DD")


    ChrTalk(    #421
        0x20,
        (
            "#260F嘻嘻，\x01",
            "玲的房间已经被\x01",
            "布娃娃埋起来了。\x02\x03",

            "#261F嘻嘻，真想让\x01",
            "提妲和姐姐看看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E442")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_EF95")

    label("loc_E44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_EF95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EABF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8AA")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E502")
    Jump("loc_E544")

    label("loc_E502")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E51E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E544")

    label("loc_E51E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E53A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E544")

    label("loc_E53A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E544")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #422
        0x107,
        "#560F啊，玲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x20,
        (
            "#264F哎，\x01",
            "提妲和艾丝蒂尔都要出去吗？\x02\x03",

            "#266F玲一个人好无聊啊。\x02",
        )
    )

    Jump("loc_E5D9")

    label("loc_E5D9")

    CloseMessageWindow()

    ChrTalk(    #424
        0x107,
        (
            "#065F对、对不起……\x02\x03",

            "#066F那个，\x01",
            "要不下次我们一起去购物吧。\x02\x03",

            "#067F嘿嘿，\x01",
            "之前在百货店里\x01",
            "买到了好漂亮的胸针……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x20,
        (
            "#260F嘻嘻，是有这么一回事。\x02\x03",

            "#267F对了……#1400W \x01",
            "#20W我之前在一家很小的店里\x01",
            "看到了同一种胸针。\x02\x03",

            "#261F不过中间的宝石是红色的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x107,
        (
            "#064F啊，真不错……\x02\x03",

            "王都的百货店\x01",
            "已经都卖完了……\x02\x03",

            "#562F唉，\x01",
            "我也想要红色的啊……\x02",
        )
    )

    Jump("loc_E76E")

    label("loc_E76E")

    CloseMessageWindow()

    ChrTalk(    #427
        0x20,
        (
            "#265F那么，\x01",
            "下次我就带你去\x01",
            "那家很远的店转转吧？\x02\x03",

            "#269F在共和国的东方人街里\x01",
            "转一天都不会觉得烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x107,
        (
            "#064F是、是这样啊……\x02\x03",

            "#061F嘿嘿，\x01",
            "如果能再找到可爱的小玩意就好了～\x02\x03",

            "#560F听我说，\x01",
            "之前我买的那个挂饰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        (
            "#1016F（……唔，\x01",
            "  好像聊得很热闹嘛。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_EAB9")

    label("loc_E8AA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #430
        0x20,
        (
            "#261F……在那家店里看到\x01",
            "和上次买的同一种胸针。\x02\x03",

            "#265F不过中间的宝石是红色的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x12,
        (
            "#064F啊，真不错……\x02\x03",

            "王都的百货店\x01",
            "已经都卖完了……\x02\x03",

            "#562F唉，\x01",
            "我也想要红色的啊……\x02",
        )
    )

    Jump("loc_E985")

    label("loc_E985")

    CloseMessageWindow()

    ChrTalk(    #432
        0x20,
        (
            "#265F那么，\x01",
            "下次我就带你去\x01",
            "那家很远的店转转吧？\x02\x03",

            "#269F在共和国的东方人街里\x01",
            "转一天都不会觉得烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x12,
        (
            "#064F是、是这样啊……\x02\x03",

            "#061F嘿嘿，\x01",
            "如果能再找到可爱的小玩意就好了～\x02\x03",

            "#560F听我说，\x01",
            "之前我买的那个挂饰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        (
            "#1016F（……唔，\x01",
            "  好像聊得很热闹嘛。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_EAB9")

    OP_A2(0x2662)
    Jump("loc_EF95")

    label("loc_EABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC8C")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB6D")
    Jump("loc_EBAF")

    label("loc_EB6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EB89")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EBAF")

    label("loc_EB89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBA5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EBAF")

    label("loc_EBA5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EBAF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #435
        0x20,
        (
            "#261F嘻嘻……\x01",
            "玲之前可是在帝国的商店里\x01",
            "看到了这么大的布偶熊。\x02\x03",

            "#265F就像成年人那般大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x107,
        (
            "#065F哇……\x02\x03",

            "#067F我、我也想见识一下呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_ED69")

    label("loc_EC8C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #437
        0x20,
        (
            "#260F对了，\x01",
            "帝国也有很多大型商店呢。\x02\x03",

            "#261F嘻嘻，玲之前可是在帝国的商店里\x01",
            "看到了这么大的布偶熊。\x02\x03",

            "就像成年人那般大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x12,
        (
            "#065F哇……\x02\x03",

            "#067F我、我也想见识一下呢……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_ED69")

    OP_A2(0x6)
    Jump("loc_EF95")

    label("loc_ED6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF1B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE15")
    Jump("loc_EE57")

    label("loc_EE15")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EE31")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EE57")

    label("loc_EE31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE4D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EE57")

    label("loc_EE4D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EE57")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #439
        0x20,
        (
            "#260F对了，\x01",
            "帝国也有很多大型商店呢。\x02\x03",

            "#261F嘻嘻，玲之前可是在帝国的商店里\x01",
            "看到了这么大的布偶熊。\x02\x03",

            "就像成年人那般大。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_EF95")

    label("loc_EF1B")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #440
        0x20,
        (
            "#261F嘻嘻……\x01",
            "玲之前可是在帝国的商店里\x01",
            "看到了这么大的布偶熊。\x02\x03",

            "#265F就像成年人那般大。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_EF95")

    Return()

    # Function_13_B6A2 end

    def Function_14_EF96(): pass

    label("Function_14_EF96")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1603A, 0xFFFFC950, 0xFFFF3508, 0xBB8, 0x0)
    OP_8E(0xFE, 0x169CC, 0xFFFFC950, 0xFFFF3ADA, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17552, 0xFFFFC950, 0xFFFF3936, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x40)
    Return()

    # Function_14_EF96 end

    def Function_15_EFE4(): pass

    label("Function_15_EFE4")

    SetChrFlags(0x18, 0x10)
    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F06E")

    ChrTalk(    #441
        0x18,
        "#311F……啾☆\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 1200, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x18)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #442
        (
            "\x07\x05基库啄起了\x01",
            "科洛丝手里的食物。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xF)
    Jump("loc_F0C8")

    label("loc_F06E")

    OP_62(0x18, 0x0, 1200, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x18)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #443
        (
            "\x07\x05基库啄起了\x01",
            "科洛丝手里的食物。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_F0C8")

    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x18)
    Return()

    # Function_15_EFE4 end

    SaveToFile()

Try(main)
