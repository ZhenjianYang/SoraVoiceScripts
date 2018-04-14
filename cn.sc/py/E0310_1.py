from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0310_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0310   ._SN',
            'ED6_DT21/E0310_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_1335",         # 02, 2
        "Function_3_2B03",         # 03, 3
        "Function_4_3DB5",         # 04, 4
        "Function_5_4852",         # 05, 5
        "Function_6_4F90",         # 06, 6
        "Function_7_5053",         # 07, 7
        "Function_8_506F",         # 08, 8
        "Function_9_5639",         # 09, 9
        "Function_10_57CE",        # 0A, 10
        "Function_11_595D",        # 0B, 11
        "Function_12_5F8A",        # 0C, 12
        "Function_13_6D8D",        # 0D, 13
        "Function_14_75A2",        # 0E, 14
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_182")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114")

    ChrTalk(    #0
        0xFE,
        "右舷，飞翔引擎……回路连接完成。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "从预想输出功率的５０％\x01",
            "开始进行模拟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_17C")

    label("loc_114")


    ChrTalk(    #2
        0xFE,
        (
            "在输出功率的５０％到７０％之间\x01",
            "通过增加负荷来测试电路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "如果舷外支架有异常，\x01",
            "就立即停止测试。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C")

    TalkEnd(0xFE)
    Jump("loc_1334")

    label("loc_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_18C")
    Jump("loc_1334")

    label("loc_18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_196")
    Jump("loc_1334")

    label("loc_196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3B8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F")

    ChrTalk(    #4
        0xFE,
        "啊，殿下……您辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "刚刚先完成了\x01",
            "各项机能的检查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "正如拉赛尔博士所说，\x01",
            "损伤出奇地轻微。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这种程度靠我们自己\x01",
            "就足以进行修复。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2A3")

    label("loc_24F")


    ChrTalk(    #8
        0xFE,
        (
            "正如拉赛尔博士所说，\x01",
            "损伤出奇地轻微。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "这种程度靠我们自己\x01",
            "就足以进行修复。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3")

    Jump("loc_3B2")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C")

    ChrTalk(    #10
        0xFE,
        (
            "刚刚先完成了\x01",
            "各项机能的检查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "正如博士所说，\x01",
            "损伤比想象中的要小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "舵总算还没问题，\x01",
            "导力机关也平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "努力一下的话应该\x01",
            "可以靠我们自己来修复。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_3B2")

    label("loc_35C")


    ChrTalk(    #14
        0xFE,
        (
            "正如博士所说，\x01",
            "损伤比想象中的要小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "努力一下的话应该\x01",
            "可以靠我们自己来修复。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2")

    TalkEnd(0xFE)
    Jump("loc_1334")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_5ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_457")
    Jump("loc_499")

    label("loc_457")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_473")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_499")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_499")

    label("loc_48F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_499")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6")

    ChrTalk(    #16
        0xFE,
        (
            "离这次作战结束\x01",
            "就只剩下那座塔了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F")

    label("loc_4F6")


    ChrTalk(    #17
        0xFE,
        (
            "离这次作战结束\x01",
            "就只剩下那座塔了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #18
        0xFE,
        (
            "呼，埃尔赛尤号啊。\x01",
            "你也辛苦了。\x01",
            "总是四处奔波，一定累了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "我们很快就能回王都了。\x01",
            "拜托你再坚持一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_5EA")

    label("loc_5A1")

    TalkBegin(0xFE)

    ChrTalk(    #20
        0xFE,
        (
            "埃尔赛尤号啊。\x01",
            "拜托你再坚持一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "我们很快就能回王都了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_5EA")

    Jump("loc_1334")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_7BE")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_684")
    Jump("loc_6C6")

    label("loc_684")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C6")

    label("loc_6A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C6")

    label("loc_6BC")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C6")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #22
        0xFE,
        (
            "嗯……？　你是谁？\x01",
            "不好意思，请别跟我说话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "海风很强啊。\x01",
            "保持姿势很困难哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "要让这么大的船\x01",
            "悬停在空中\x01",
            "不容易呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7B3")

    label("loc_779")


    ChrTalk(    #25
        0xFE,
        (
            "可恶…\x01",
            "风会使船不安定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "所以我不喜欢\x01",
            "沿海地区。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1334")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_9CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_884")
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(    #27
        0xE,
        (
            "这个塔也一样被\x01",
            "黑色的障壁笼罩着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        (
            "博士正在调查……\x01",
            "……目前还没有结论。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        "……不过接近它一定很危险。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        (
            "嗯，我有同感。\x01",
            "总之要保持距离。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x0)
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Jump("loc_9C7")

    label("loc_884")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_914")
    Jump("loc_956")

    label("loc_914")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_930")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_956")

    label("loc_930")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_956")

    label("loc_94C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_956")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #31
        0xE,
        (
            "这个塔也一样被\x01",
            "黑色的障壁笼罩着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "那东西\x01",
            "究竟是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_9C7")

    Jump("loc_1334")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC")
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(    #33
        0xF,
        (
            "塔的导力场有异常……\x01",
            "………别太靠近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xF,
        (
            "还有风……\x01",
            "……注意别被卷走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "没问题的。\x01",
            "我们和塔有一段距离。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        (
            "不过，究竟是什么呢？\x01",
            "那个像黑色墙壁一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "你说的导力场异常也是\x01",
            "那东西所造成的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        "………不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xF,
        "不过……得小心。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x0)
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Jump("loc_C41")

    label("loc_AFC")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B8C")
    Jump("loc_BCE")

    label("loc_B8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BA8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCE")

    label("loc_BA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCE")

    label("loc_BC4")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BCE")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #40
        0xE,
        (
            "当然，小心\x01",
            "总是没有坏处的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xE,
        (
            "总之要好好保持\x01",
            "和塔之间的距离。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_C41")

    Jump("loc_1334")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_D93")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CDB")
    Jump("loc_D1D")

    label("loc_CDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF7")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D1D")

    label("loc_CF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D13")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D1D")

    label("loc_D13")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D1D")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #42
        0xFE,
        (
            "呼，看来\x01",
            "被干掉了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "操控技术不错吧？\x01",
            "嘿嘿，不愧是本大爷。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1334")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E32")
    Jump("loc_E74")

    label("loc_E32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E4E")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E74")

    label("loc_E4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6A")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E74")

    label("loc_E6A")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E74")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #44
        0xFE,
        (
            "哟，你们就是\x01",
            "那帮游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "我是舵手勒克司。\x01",
            "现在负责操舵这艘船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "抱歉，这次恐怕\x01",
            "没有你们的出场的机会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "才一两头龙而已……\x01",
            "根本不是『埃尔赛尤』的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "总之你们就尽管放心，\x01",
            "好好地参观一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x1A6A)
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1334")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1127")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_101C")
    Jump("loc_105E")

    label("loc_101C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1038")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105E")

    label("loc_1038")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1054")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105E")

    label("loc_1054")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105E")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #49
        0xFE,
        (
            "总之你们就尽管放心，\x01",
            "好好地参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "另外，旁边那个叫艾柯的家伙\x01",
            "请你们别和她计较。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "虽然看起来傲慢又失礼，\x01",
            "不过本性是相当善良的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x1)
    OP_A2(0x2)
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1334")

    label("loc_1127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1284")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11BE")
    Jump("loc_1200")

    label("loc_11BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11DA")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1200")

    label("loc_11DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11F6")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1200")

    label("loc_11F6")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1200")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #52
        0xFE,
        (
            "总之你们就尽管放心，\x01",
            "好好地参加一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "另外，请你们别和\x01",
            "艾柯那家伙计较。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1334")

    label("loc_1284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F3")
    TalkBegin(0xFE)

    ChrTalk(    #54
        0xFE,
        "１号、３号弹库开放测试ＯＫ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "继续准备开放２号、４号。\x01",
            "结晶回路，依序进行连接……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    TalkEnd(0xFE)
    Jump("loc_1334")

    label("loc_12F3")

    TalkBegin(0xFE)

    ChrTalk(    #56
        0xFE,
        (
            "１号、３号弹库开放测试ＯＫ。\x01",
            "继续准备开放２号、４号。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1334")

    Return()

    # Function_1_AB end

    def Function_2_1335(): pass

    label("Function_2_1335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_161B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13CC")
    Jump("loc_140E")

    label("loc_13CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13E8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_140E")

    label("loc_13E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1404")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_140E")

    label("loc_1404")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_140E")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(    #57
        0xFE,
        (
            "现在正要展开\x01",
            "飞翔引擎的测试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "如果这个成功的话，\x01",
            "就只剩等待殿下归舰了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "请让我最后……\x01",
            "再祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1516")

    label("loc_14C6")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #60
        0xFE,
        (
            "控制系统，导力压正常……\x01",
            "各接应系统也无异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "……测试准备完成。\x02",
    )

    CloseMessageWindow()

    label("loc_1516")

    Jump("loc_1610")

    label("loc_1519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C0")

    ChrTalk(    #62
        0xFE,
        (
            "现在正要开始进行\x01",
            "飞翔引擎的测试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "不过，中枢塔的探索，\x01",
            "和舷外支架的回收……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "……这些难题还没有解决。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "请让我最后……\x01",
            "再祈祷一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1610")

    label("loc_15C0")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #66
        0xFE,
        (
            "控制系统，导力压正常……\x01",
            "各接应系统也无异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "……测试准备完成。\x02",
    )

    CloseMessageWindow()

    label("loc_1610")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_161B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_16F4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A3")

    ChrTalk(    #68
        0xFE,
        "照明终于恢复了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "接下来还有飞行系统的维修\x01",
            "和操舵系统的调整……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "或许可以让它飞起来\x01",
            "也说不定……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_16EE")

    label("loc_16A3")


    ChrTalk(    #71
        0xFE,
        "照明终于恢复了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "接下来还有飞行系统的修理\x01",
            "和操舵系统的调整……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EE")

    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_16F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1B51")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_178B")
    Jump("loc_17CD")

    label("loc_178B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17A7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17CD")

    label("loc_17A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17C3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17CD")

    label("loc_17C3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A19")

    ChrTalk(    #73
        0xFE,
        (
            "我听大尉说了……\x01",
            "你是空贼团的那个女孩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "别妨碍我工作……\x01",
            "……这一点我得事先声明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10B,
        (
            "#211F哈哈，真是个无知的家伙～\x02\x03",

            "完全不知道\x01",
            "我能帮上多大的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "……是吗……\x01",
            "那我就拭目以待了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "……那么，你能不能\x01",
            "赶紧消失到别处去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10B,
        "#213F……什………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "……你妨碍到我工作了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "我一开始就说过\x01",
            "别妨碍我的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10B,
        "#216F……唔～～～……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1016F（算、算了算了……\x01",
            "  克制一下啊。)\x02\x03",

            "（你打算和别人\x01",
            "  一见面就吵架吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1052F（乔丝特……\x01",
            "  这回你得认输了。 ）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10B,
        "#215F（呜～～～～～～……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x229F)
    Jump("loc_1B46")

    label("loc_1A19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AA0")

    ChrTalk(    #85
        0xFE,
        "可别妨碍我的工作啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "只要遵守到这一点，\x01",
            "什么都不做也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10B,
        "#216F（这、这个女人，真让人讨厌……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B46")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B10")

    ChrTalk(    #88
        0xFE,
        (
            "空贼团和我们的\x01",
            "情况好像也差不多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "我们也会尽可能地\x01",
            "帮助他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "因为这是命令……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1B46")

    label("loc_1B10")


    ChrTalk(    #91
        0xFE,
        (
            "我们也会帮助\x01",
            "空贼团的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "因为这是\x01",
            "命令……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B46")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_1B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1D17")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE8")
    Jump("loc_1C2A")

    label("loc_1BE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C04")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2A")

    label("loc_1C04")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C20")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2A")

    label("loc_1C20")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C2A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #93
        0xFE,
        (
            "迫降之后，探测器\x01",
            "一直出现反应……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "都是一些超乎常识的\x01",
            "强力导力反应……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "……这里到底有什么呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1D0C")

    label("loc_1CC9")


    ChrTalk(    #96
        0xFE,
        (
            "迫降之后，探测器\x01",
            "一直出现反应……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "……这里到底有什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_1D0C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_1F99")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DAE")
    Jump("loc_1DF0")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DCA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DF0")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DF0")

    label("loc_1DE6")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF0")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE7")

    ChrTalk(    #98
        0xFE,
        (
            "导力场的混乱\x01",
            "变得越来越大了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "目前塔上\x01",
            "还没有变化……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(    #100
        0xFE,
        (
            "公主殿下也请……\x01",
            "……多多保重……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB8")

    label("loc_1E95")


    ChrTalk(    #101
        0xFE,
        (
            "你们也要……\x01",
            "……多加小心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB8")


    ChrTalk(    #102
        0xFE,
        (
            "这种现象……\x01",
            "说不定也许是某种前兆。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1F8E")

    label("loc_1EE7")


    ChrTalk(    #103
        0xFE,
        (
            "导力场的混乱\x01",
            "变得越来越大了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "这种现象……\x01",
            "说不定也许是某种前兆。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6B")

    ChrTalk(    #105
        0xFE,
        (
            "公主殿下也请……\x01",
            "……多多保重……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8E")

    label("loc_1F6B")


    ChrTalk(    #106
        0xFE,
        (
            "你们也要……\x01",
            "……多加小心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_219E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2030")
    Jump("loc_2072")

    label("loc_2030")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_204C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2072")

    label("loc_204C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2068")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2072")

    label("loc_2068")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2072")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(    #107
        0xFE,
        (
            "哎呀…………………\x01",
            "……辛苦了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "导力场异常的原因\x01",
            "目前还没掌握……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "要是知道了原因……\x01",
            "早就能拟定对策了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "看来麻烦还要……\x01",
            "持续一阵子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2193")

    label("loc_2147")


    ChrTalk(    #111
        0xFE,
        (
            "导力场异常的原因\x01",
            "目前还没掌握……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "看来麻烦还要……\x01",
            "持续一阵子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2193")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_219E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_229A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2259")

    ChrTalk(    #113
        0xE,
        (
            "这个塔也一样被\x01",
            "黑色的障壁笼罩着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xF,
        (
            "博士正在调查……\x01",
            "……目前还没有结论。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xF,
        "……不过接近它一定很危险。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xE,
        (
            "嗯，我有同感。\x01",
            "总之要保持距离。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x3)
    Jump("loc_2294")

    label("loc_2259")


    ChrTalk(    #117
        0xF,
        (
            "塔周边的导力场\x01",
            "现在依然异常……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        "还不能够接近……\x02",
    )

    CloseMessageWindow()

    label("loc_2294")

    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_240A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C3")

    ChrTalk(    #119
        0xF,
        (
            "塔的导力场很不寻常……\x01",
            "………别太靠近了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xF,
        (
            "还有风……\x01",
            "……注意别被吹走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xE,
        (
            "没问题的。\x01",
            "我们和塔有一段距离。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xE,
        (
            "不过，究竟是什么呢？\x01",
            "那个像黑色墙壁一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xE,
        (
            "你说的导力场异常也是\x01",
            "那个东西造成的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xF,
        "………不知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xF,
        "不过……得小心。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x3)
    Jump("loc_2404")

    label("loc_23C3")


    ChrTalk(    #126
        0xF,
        (
            "如果继续接近的话\x01",
            "风险就太高了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xF,
        "调查队伍从地面接近，\x02",
    )

    CloseMessageWindow()

    label("loc_2404")

    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_240A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_25FC")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24A1")
    Jump("loc_24E3")

    label("loc_24A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24BD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E3")

    label("loc_24BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24D9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E3")

    label("loc_24D9")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24E3")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(    #128
        0xFE,
        "……赶快去观察一下龙的情况如何。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "战果的确认\x01",
            "对士兵来说也是重要的任务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "……你们也不想被已经\x01",
            "打倒了的敌人从背后偷袭吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_25F1")

    label("loc_259E")


    ChrTalk(    #131
        0xFE,
        "……赶快去观察一下龙的情况如何！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "战果的确认\x01",
            "对士兵来说也是重要的任务啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_25FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_2B02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2793")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_269B")
    Jump("loc_26DD")

    label("loc_269B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26B7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26DD")

    label("loc_26B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26D3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26DD")

    label("loc_26D3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26DD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #133
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "我听说了……\x01",
            "你们是担任观察员的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "可别妨碍我们的作战……\x01",
            "……我想说的只有这些。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1A6B)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_2793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_28E2")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_282A")
    Jump("loc_286C")

    label("loc_282A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2846")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_286C")

    label("loc_2846")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2862")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_286C")

    label("loc_2862")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_286C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #136
        0xFE,
        "寒暄应该也已经结束了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "……你们该返回工作岗位了吧？\x02",
    )

    CloseMessageWindow()
    OP_A3(0x4)
    OP_A2(0x5)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_28E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2A29")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2979")
    Jump("loc_29BB")

    label("loc_2979")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2995")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29BB")

    label("loc_2995")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29B1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29BB")

    label("loc_29B1")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29BB")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #138
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "……你们就没别的事可做了？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_2A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABD")
    TalkBegin(0xFE)

    ChrTalk(    #140
        0xFE,
        "……周围空域没有导力反应……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "……重复……\x01",
            "周围空域没有导力反应……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "……各巡逻艇接下来\x01",
            "继续进行指定的巡逻任务……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    TalkEnd(0xFE)
    Jump("loc_2B02")

    label("loc_2ABD")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        (
            "周围空域没有导力反应……\x01",
            "各巡逻艇继续进行指定的巡逻任务。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_2B02")

    Return()

    # Function_2_1335 end

    def Function_3_2B03(): pass

    label("Function_3_2B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2D0F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B9A")
    Jump("loc_2BDC")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BB6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDC")

    label("loc_2BB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDC")

    label("loc_2BD2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BDC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA4")

    ChrTalk(    #144
        0xFE,
        (
            "『山猫号』的修理工作\x01",
            "似乎也进行得很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "由于飞行系统的修复\x01",
            "全都仰赖博士所提供的建议……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "空贼团的各位也\x01",
            "坦率地表达了自己的敬意哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2D04")

    label("loc_2CA4")


    ChrTalk(    #147
        0xFE,
        (
            "『山猫号』的修理工作\x01",
            "似乎也进行得很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "看来拉赛尔博士的建议\x01",
            "提供了相当大的帮助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D04")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_2EDB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E77")

    ChrTalk(    #149
        0x10,
        (
            "\x07\x00#1P这里是埃尔赛尤号……\x01",
            "……山猫号，请回答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x10,
        "\x07\x00#1P……重复一次，山猫号请回答。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x1B,
        "\x07\x05#2P#1S啊啊，这里是山猫号……\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x1B,
        (
            "\x07\x05#2P#1S接收信号良好……\x01",
            "埃尔赛尤号，你们那里听得清楚吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        (
            "\x07\x00#1P埃尔赛尤呼叫山猫号……\x01",
            "我们这边的信号也很好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10,
        (
            "\x07\x00#1P贵舰现在有\x01",
            "什么物资不足吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x10,
        (
            "\x07\x00#1P重复……\x01",
            "山猫号，有什么物资不足吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2ED5")

    label("loc_2E77")


    ChrTalk(    #156
        0x10,
        (
            "\x07\x00#1P山猫号，你们那边有什么\x01",
            "物资不足吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        (
            "\x07\x00#1P重复……\x01",
            "山猫号，有什么物资不足吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED5")

    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_2EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_322B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F72")
    Jump("loc_2FB4")

    label("loc_2F72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F8E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FB4")

    label("loc_2F8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FAA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FB4")

    label("loc_2FAA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FB4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30F6")

    ChrTalk(    #158
        0xFE,
        "你就是空贼小姑娘吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "客套话就不说了，空贼艇的\x01",
            "通讯器材没有问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10B,
        (
            "#210F应该没问题。\x02\x03",

            "操舵室也没受到\x01",
            "什么严重损伤……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "这样啊，那么我们也\x01",
            "进行一下通讯的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "等你的哥哥们平安返回\x01",
            "后就可以马上联系到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10B,
        (
            "#211F啊，嗯！\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x22CF)
    Jump("loc_3220")

    label("loc_30F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_314F")

    ChrTalk(    #164
        0xFE,
        (
            "我们也在准备和\x01",
            "空贼艇进行通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "你哥哥他们\x01",
            "要是没事就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3220")

    label("loc_314F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C8")

    ChrTalk(    #166
        0xFE,
        (
            "有空贼团在说明\x01",
            "他们的船也在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "嗯，也许还可以用导力通讯\x01",
            "和他们取得联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "有空的话\x01",
            "试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3220")

    label("loc_31C8")


    ChrTalk(    #169
        0xFE,
        (
            "有空贼团在就代表\x01",
            "他们的船应该也在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "顺利的话，或许可以通过\x01",
            "导力通讯取得联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3220")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_322B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3388")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3324")

    ChrTalk(    #171
        0xFE,
        (
            "通讯设备都正常呢。\x01",
            "任何地方都没有异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "比起这些，我倒是更在意\x01",
            "那些有时候会串线过来的信号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "虽然很遗憾，因为经过了加密\x01",
            "无法得知内容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "不过那些似乎是\x01",
            "『结社』的通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "说不定他们也在\x01",
            "探索着这座城市。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3382")

    label("loc_3324")


    ChrTalk(    #176
        0xFE,
        (
            "有时候会串线过来的信号，\x01",
            "似乎是结社他们之间的联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "说不定他们也在\x01",
            "探索着浮游都市。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3382")

    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_3388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_368F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_341F")
    Jump("loc_3461")

    label("loc_341F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_343B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3461")

    label("loc_343B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3457")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3461")

    label("loc_3457")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3461")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CD")

    ChrTalk(    #178
        0xFE,
        (
            "看来各地遭受的攻击\x01",
            "也逐渐在平息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3536")

    ChrTalk(    #179
        0xFE,
        (
            "接下来只要压制住最后的塔，\x01",
            "就能让事件告一段落了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "盼望大家凯旋归来……\x01",
            "我们全体乘务员都在为你们祈祷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C7")

    label("loc_3536")


    ChrTalk(    #181
        0xFE,
        (
            "接下来各位只要压制住最后的塔，\x01",
            "就能让事件告一段落了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "……但不知为什么，总觉得\x01",
            "心中不太舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "看来还是因为不知道\x01",
            "敌人的目的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C7")

    OP_A2(0x6)
    Jump("loc_3684")

    label("loc_35CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(    #184
        0xFE,
        (
            "明明是最后的塔了，\x01",
            "心里还是堵得慌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "看来还是因为不知道\x01",
            "敌人的目的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3684")

    label("loc_362E")


    ChrTalk(    #186
        0xFE,
        (
            "明明终于到最后的塔了，\x01",
            "心里还是堵得慌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "看来还是因为不知道\x01",
            "敌人的目的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3684")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_368F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_37B3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3721")

    ChrTalk(    #188
        0xFE,
        (
            "埃尔赛尤号呼叫守备队……\x01",
            "玛诺利亚守备队，请报告情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "重复一次，这里是埃尔赛尤号。\x01",
            "玛诺利亚守备队，请报告情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_37AD")

    label("loc_3721")


    ChrTalk(    #190
        0xFE,
        (
            "玛诺利亚守备队，这里是埃尔赛尤号。\x01",
            "支援的警备艇正在向你们接近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "支援部队不久后即将到达玛诺利亚。\x01",
            "重复，即将到达玛诺利亚上空……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AD")

    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3866")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3816")

    ChrTalk(    #192
        0xFE,
        (
            "蔡斯的战斗\x01",
            "好像仍然很激烈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "一旦有新的情报，\x01",
            "我会立刻告知的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3860")

    label("loc_3816")


    ChrTalk(    #194
        0xFE,
        (
            "蔡斯的战斗\x01",
            "好像仍然很激烈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "有什么新的情报，\x01",
            "我会马上告知的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3860")

    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_3866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3950")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DE")

    ChrTalk(    #196
        0xFE,
        (
            "埃尔赛尤号呼叫司令部……\x01",
            "埃尔赛尤号呼叫司令部……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "到达目标上空……\x01",
            "重复，到达目标……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_394A")

    label("loc_38DE")


    ChrTalk(    #198
        0xFE,
        (
            "在目标上空发现可疑影子。\x01",
            "目前判断无法直接降落……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "将由地面派遣调查队。\x01",
            "重复，由地面派遣调查队……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394A")

    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_3950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_3AB2")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39E7")
    Jump("loc_3A29")

    label("loc_39E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A03")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A29")

    label("loc_3A03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A1F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A29")

    label("loc_3A1F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A29")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #200
        0xFE,
        "龙看来已完全进入睡眠状态。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "现在即便是整个人跳上去，\x01",
            "也应该不会有任何危险才对。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3DB4")

    label("loc_3AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_3DB4")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B49")
    Jump("loc_3B8B")

    label("loc_3B49")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B65")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B8B")

    label("loc_3B65")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B81")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B8B")

    label("loc_3B81")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B8B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C36")

    ChrTalk(    #202
        0xFE,
        (
            "啊，辛苦了……\x01",
            "你们是观察员吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "我是主管本舰通讯的\x01",
            "报务员利昂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "虽然只是短期合作，\x01",
            "不过还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x1A6C)
    Jump("loc_3DAC")

    label("loc_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3C89")

    ChrTalk(    #205
        0xFE,
        (
            "虽然只是短期合作，\x01",
            "不过还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "也让我们竭尽彼此所能吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DAC")

    label("loc_3C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D38")

    ChrTalk(    #207
        0xFE,
        (
            "埃尔赛尤呼叫科尔波０１……\x01",
            "……埃尔赛尤呼叫科尔波０１。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "周围空域没有反应……\x01",
            "……重复，周围没有反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "贵舰请继续巡逻……\x01",
            "……重复，贵舰请继续……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3DAC")

    label("loc_3D38")


    ChrTalk(    #210
        0xFE,
        (
            "埃尔赛尤呼叫戈尔斯０２……\x01",
            "……埃尔赛尤呼叫戈尔斯０２。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "戈尔斯02，我是埃尔赛尤。\x01",
            "……请报告状况，重复……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_3DB4")

    Return()

    # Function_3_2B03 end

    def Function_4_3DB5(): pass

    label("Function_4_3DB5")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_3F0B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E16")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #212
        0xFE,
        "等候各位归舰！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "愿女神赐福各位！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_3F08")

    label("loc_3E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9E")

    ChrTalk(    #214
        0xFE,
        "各位，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "现在要进行左舷舷外支架的\x01",
            "回收和修复工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "由于结社也有可能发动袭击，\x01",
            "因此现在还不能松懈哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3F08")

    label("loc_3E9E")


    ChrTalk(    #217
        0xFE,
        (
            "我们现在要进行左舷舷外支架的\x01",
            "回收和修复工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "由于结社也有可能发动袭击，\x01",
            "因此现在还不能松懈哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F08")

    Jump("loc_484E")

    label("loc_3F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4069")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4008")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA9")

    ChrTalk(    #219
        0xFE,
        (
            "出现在『琥珀之塔』上的，\x01",
            "似乎是一个很小的孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "结社真是一个\x01",
            "让人摸不清的组织啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "请殿下也\x01",
            "一定要格外小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4005")

    label("loc_3FA9")


    ChrTalk(    #222
        0xFE,
        (
            "虽说是小孩子，\x01",
            "但也一定是结社的手下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "虽然也许是我多操心了，\x01",
            "不过也请殿下要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4005")

    Jump("loc_4066")

    label("loc_4008")


    ChrTalk(    #224
        0xFE,
        (
            "出现在『琥珀之塔』上的，\x01",
            "似乎是一个很小的孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "结社真是一个\x01",
            "让人摸不清的组织啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4066")

    Jump("loc_484E")

    label("loc_4069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_42F5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_420F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B0")

    ChrTalk(    #226
        0xFE,
        (
            "啊……\x01",
            "殿下也要前往塔那边吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "请殿下一定要\x01",
            "凡事谨慎行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "要是有什么万一的话，\x01",
            "我们的队长也有可能会上塔支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x105,
        (
            "#045F是、是这样吗……\x02\x03",

            "不过请不必担心。\x01",
            "因为我和大家在一起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "是这样子吗……\x01",
            "那就太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x101, 400)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #231
        0xFE,
        (
            "那么，各位游击士，\x01",
            "殿下就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x1E40)
    Jump("loc_420C")

    label("loc_41B0")


    ChrTalk(    #232
        0xFE,
        (
            "请殿下也一定要\x01",
            "凡事谨慎行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "要是有什么万一的话，\x01",
            "我们的队长也有可能会上塔支援。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420C")

    Jump("loc_42F2")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4296")

    ChrTalk(    #234
        0xFE,
        (
            "好像有一名女性只身\x01",
            "登上了『红莲之塔』呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "哎呀～\x01",
            "真是一位巾帼英雄呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "不过，我们的队长也\x01",
            "有可能这么做的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_42F2")

    label("loc_4296")


    ChrTalk(    #237
        0xFE,
        (
            "竟然一个人登上塔顶，\x01",
            "真是一位了不起的女性啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "不过，我们的队长也\x01",
            "有可能这么做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F2")

    Jump("loc_484E")

    label("loc_42F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_456E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441C")

    ChrTalk(    #239
        0xFE,
        (
            "在笼罩塔顶的黑色障壁之中，\x01",
            "还有延伸在内部的另一个空间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "看来『四轮之塔』\x01",
            "并不是单纯的塔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "殿下也请多加小心。\x01",
            "前方不知还有多少\x01",
            "危险在等待着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x105,
        (
            "#040F嗯，我明白。\x02\x03",

            "那么，这段时间\x01",
            "请你们好好留守。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #243
        0xFE,
        "是！　祝您旗开得胜。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xA)
    Jump("loc_445F")

    label("loc_441C")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #244
        0xFE,
        (
            "舰艇的事就交给我们吧。\x01",
            "殿下也请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_445F")

    Jump("loc_456B")

    label("loc_4462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4505")

    ChrTalk(    #245
        0xFE,
        (
            "在笼罩塔顶的黑色障壁之中，\x01",
            "还有延伸在内部的另一个空间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "看来『四轮之塔』\x01",
            "并不是单纯的塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "可能有我们所想象不到的\x01",
            "特殊用途也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_456B")

    label("loc_4505")


    ChrTalk(    #248
        0xFE,
        (
            "在笼罩塔顶的黑色障壁之中，\x01",
            "还有延伸在内部的另一个空间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "看来『四轮之塔』\x01",
            "并不是单纯的塔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456B")

    Jump("loc_484E")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4727")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CA")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #250
        0xFE,
        "辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "目前\x01",
            "舰内没有异常！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xA)
    Jump("loc_45FB")

    label("loc_45CA")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #252
        0xFE,
        (
            "辛苦了！\x01",
            "舰内没有异常！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_45FB")

    Jump("loc_4724")

    label("loc_45FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C4")

    ChrTalk(    #253
        0xFE,
        (
            "诸位，辛苦了。\x01",
            "舰内的构造已经掌握了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "降落用的升降机\x01",
            "是设置在货舱里面哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "从那边的楼梯一路走到底，\x01",
            "靠船尾那一侧的就是货舱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "附近还有工房室，\x01",
            "你们最好也能去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_4724")

    label("loc_46C4")


    ChrTalk(    #257
        0xFE,
        (
            "降落用的升降机\x01",
            "是设置在货舱里面哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "从那边的楼梯一路走到底，\x01",
            "靠船尾那一侧的就是货舱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4724")

    Jump("loc_484E")

    label("loc_4727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_476A")

    ChrTalk(    #259
        0xFE,
        "诸位，请抓紧时间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "龙掉落在\x01",
            "舰首旁的水面上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_484E")

    label("loc_476A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_484E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4800")

    ChrTalk(    #261
        0xFE,
        (
            "啊，游击士们。\x01",
            "各位工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "从这里往上走就是舰桥，\x01",
            "往下则是作战室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "由于舰内相当宽广，\x01",
            "新来的人经常会迷路哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_484E")

    label("loc_4800")


    ChrTalk(    #264
        0xFE,
        (
            "往上走就是舰桥，\x01",
            "往下则是作战室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "从左右两边的舱门\x01",
            "可以前往上甲板。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_484E")

    TalkEnd(0xFE)
    Return()

    # Function_4_3DB5 end

    def Function_5_4852(): pass

    label("Function_5_4852")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4A70")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4920")

    ChrTalk(    #266
        0xFE,
        (
            "距离完成陛下的命令\x01",
            "就只剩下一座塔了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "我们全体乘务员都在衷心祈祷\x01",
            "殿下能够微笑归来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x105,
        (
            "#040F谢谢。\x01",
            "拜托你们留守了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #269
        0xFE,
        "是！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xC)
    Jump("loc_4985")

    label("loc_4920")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #270
        0xFE,
        (
            "我们全体乘务员都在衷心祈祷\x01",
            "殿下能够旗开得胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "请您一定要带着微笑归舰。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_4985")

    Jump("loc_4A6D")

    label("loc_4988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A19")

    ChrTalk(    #272
        0xFE,
        (
            "各位，辛苦了。\x01",
            "终于只剩最后一座塔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "不过在完成陛下的命令之前，\x01",
            "请千万不要放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "我们也希望各位\x01",
            "能够好运常在。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4A6D")

    label("loc_4A19")


    ChrTalk(    #275
        0xFE,
        (
            "虽然是最后一座塔了，\x01",
            "但请千万不要放松警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "我们也希望各位\x01",
            "能够好运常在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6D")

    Jump("loc_4F8C")

    label("loc_4A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4BC9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE1")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #277
        0xFE,
        (
            "为了回应守备队的奋战，\x01",
            "我们也在竭尽全力！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "请殿下也多加小心。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_4BC6")

    label("loc_4AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B70")

    ChrTalk(    #279
        0xFE,
        (
            "在卢安近郊也有\x01",
            "『结社』的部队袭来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "看来他们的手下，\x01",
            "一直潜伏在王国中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "我们今后也要\x01",
            "更进一步加强警戒才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4BC6")

    label("loc_4B70")


    ChrTalk(    #282
        0xFE,
        (
            "看来『结社』的手下\x01",
            "一直潜伏在王国中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "我们今后也要\x01",
            "更进一步加强警戒才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC6")

    Jump("loc_4F8C")

    label("loc_4BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4DA7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C56")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #284
        0xFE,
        "辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "在殿下外出期间，\x01",
            "我们会好好守护本舰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "请放心地\x01",
            "完成您的使命吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xC)
    Jump("loc_4CB4")

    label("loc_4C56")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #287
        0xFE,
        (
            "在殿下外出期间，\x01",
            "我们会好好守护本舰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "请放心地\x01",
            "完成您的使命吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_4CB4")

    Jump("loc_4DA4")

    label("loc_4CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3A")

    ChrTalk(    #289
        0xFE,
        (
            "看来蔡斯的\x01",
            "情况非常不妙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "不过，守备队\x01",
            "一定能支撑下去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "因为在危急的情况下，\x01",
            "应该能得到要塞的支援。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4DA4")

    label("loc_4D3A")


    ChrTalk(    #292
        0xFE,
        (
            "蔡斯的情况虽然也不容乐观，\x01",
            "不过暂且应该还支撑得住吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "毕竟在危急的情况下\x01",
            "应该能得到要塞的支援。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA4")

    Jump("loc_4F8C")

    label("loc_4DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4F8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6A")

    ChrTalk(    #294
        0xFE,
        (
            "刚才科洛蒂娅殿下\x01",
            "上了甲板……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "不知是不是我的心理作用，\x01",
            "她的脸色似乎不像平时那么好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "看来殿下还是在为祖国的困境\x01",
            "而伤神劳心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "啊，好可怜……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4EC4")

    label("loc_4E6A")


    ChrTalk(    #298
        0xFE,
        (
            "科洛蒂娅殿下的脸色\x01",
            "似乎不像平时那么好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "看来殿下还在为祖国的困境\x01",
            "而伤神劳心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC4")

    Jump("loc_4F8C")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F41")

    ChrTalk(    #300
        0xFE,
        (
            "诸位游击士，\x01",
            "请你们好好保护\x01",
            "科洛蒂娅殿下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x105, 400)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #301
        0xFE,
        (
            "也请殿下……\x01",
            "多加保重贵体。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xD)
    Jump("loc_4F8C")

    label("loc_4F41")


    ChrTalk(    #302
        0xFE,
        (
            "请你们好好保护\x01",
            "科洛蒂娅殿下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x105, 400)

    ChrTalk(    #303
        0xFE,
        (
            "也请殿下……\x01",
            "多加保重贵体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8C")

    TalkEnd(0xFE)
    Return()

    # Function_5_4852 end

    def Function_6_4F90(): pass

    label("Function_6_4F90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5004")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #304
        0xFE,
        (
            "殿下……\x01",
            "请您一定要平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "全体乘务员都在祈祷\x01",
            "殿下能够旗开得胜。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_504F")

    label("loc_5004")

    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #306
        0xFE,
        "辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "为了准备飞翔引擎的测试，\x01",
            "大家都聚集到舰桥了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504F")

    TalkEnd(0xFE)
    Return()

    # Function_6_4F90 end

    def Function_7_5053(): pass

    label("Function_7_5053")

    TalkBegin(0xFE)

    ChrTalk(    #308
        0xFE,
        "#160F◆无台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5053 end

    def Function_8_506F(): pass

    label("Function_8_506F")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_52E3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516A")

    ChrTalk(    #309
        0x15,
        (
            "#270F说实话我真没想到能在\x01",
            "这么短的时间内修复。\x02\x03",

            "不愧是利贝尔王国……\x01",
            "技术人员的水平也很高啊。\x02\x03",

            "维修员中好像也有人\x01",
            "受到过拉赛尔博士的熏陶……\x02\x03",

            "#272F身为有心促进祖国的技术力\x01",
            "却力有未遂的军人，\x01",
            "实在是羡慕至极啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_51C5")

    label("loc_516A")


    ChrTalk(    #310
        0x15,
        (
            "#277F维修员中好像也有人\x01",
            "受到过拉赛尔博士的熏陶……\x02\x03",

            "如果可以的话\x01",
            "真想带两三个人回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51C5")

    Jump("loc_52E0")

    label("loc_51C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5283")

    ChrTalk(    #311
        0x15,
        (
            "#272F哎呀，竟然在这么短的时间内\x01",
            "修复到如此程度……\x02\x03",

            "#270F不愧是利贝尔王国……\x01",
            "技术人员的水平也很高啊。\x02\x03",

            "维修员中好像也有人\x01",
            "受到过拉赛尔博士的熏陶……\x02\x03",

            "真是令人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_52E0")

    label("loc_5283")


    ChrTalk(    #312
        0x15,
        (
            "#276F维修员中好像也有人\x01",
            "受到过拉赛尔博士的熏陶……\x02\x03",

            "如果可以的话\x01",
            "真想就这样带回帝国去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E0")

    Jump("loc_5635")

    label("loc_52E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_52ED")
    Jump("loc_5635")

    label("loc_52ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_52F7")
    Jump("loc_5635")

    label("loc_52F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_5635")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A1")

    ChrTalk(    #313
        0x15,
        (
            "#270F首先应该从恢复舰内照明\x01",
            "以及确保通路方面开始作业吧。\x02\x03",

            "因为要动员兵力，\x01",
            "就必须先有运输通道。\x02\x03",

            "在正式的工程展开之前\x01",
            "整顿好这些是非常重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5635")

    label("loc_53A1")


    ChrTalk(    #314
        0x15,
        (
            "#270F应该优先进行恢复照明\x01",
            "以及确保通路的作业吧。\x02\x03",

            "因为要动员兵力，\x01",
            "就必须先整备好运输通道。\x02\x03",

            "在正式的工程展开之前，\x01",
            "我打算尽可能地做好准备。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5635")
    TurnDirection(0x15, 0x104, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EF")

    ChrTalk(    #315
        0x15,
        (
            "#272F所以说，不好意思，\x01",
            "这个吊儿郎当的家伙就交给你们了。\x02\x03",

            "把他丢在舰内的话，\x01",
            "老实说我会感到非常为难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x104,
        (
            "#032F你找了这么多借口……\x01",
            "其实只是想和尤莉亚上尉\x01",
            "两人独处吧？\x02\x03",

            "你明明已经有我了，\x01",
            "却还要去追求女性……\x02\x03",

            "#039F啊～你这个没良心的！！\x01",
            "难道你想要的只是我的身体！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #317
        0x15,
        (
            "#274F……………………………\x02\x03",

            "……我要说的\x01",
            "你们都明白了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x101,
        "#1002F……嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x102,
        "#1035F我们会负责看管他的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22AD)
    Jump("loc_5635")

    label("loc_55EF")

    TurnDirection(0x15, 0x104, 400)
    Sleep(400)

    ChrTalk(    #320
        0x15,
        (
            "#272F那么，各位……\x01",
            "这个吊儿郎当的家伙就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5635")

    TalkEnd(0xFE)
    Return()

    # Function_8_506F end

    def Function_9_5639(): pass

    label("Function_9_5639")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_57CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5750")

    ChrTalk(    #321
        0x16,
        (
            "#140F虽然我之前还担心了一阵子，\x01",
            "不过船的维修看来进行得很顺利呢。\x02\x03",

            "多亏有了拉赛尔博士，\x01",
            "这下子总算是得救了……\x02\x03",

            "#141F接下来如果能阻止结社的企图，\x01",
            "就是真正圆满的大结局了。\x02\x03",

            "我会把特刊的\x01",
            "头条位置空出来的。\x02\x03",

            "希望你们能带来让整个王国沸腾的\x01",
            "华丽大结局啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_57CA")

    label("loc_5750")


    ChrTalk(    #322
        0x16,
        (
            "#141F如果能阻止『结社』的企图，\x01",
            "就是真正圆满的大结局了。\x02\x03",

            "我会把特刊的\x01",
            "头条位置空出来的。\x01",
            "期待你们上演的华丽活跃剧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CA")

    TalkEnd(0xFE)
    Return()

    # Function_9_5639 end

    def Function_10_57CE(): pass

    label("Function_10_57CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_5959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_590C")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #323
        0x17,
        (
            "#150F呀呵～！\x01",
            "小艾你们好啊。\x02\x03",

            "看起来你们好像要去\x01",
            "一个很麻烦的地方……\x02\x03",

            "不过，希望你们能\x01",
            "一起回到这里来哦。\x02\x03",

            "我会为你们拍下\x01",
            "打倒坏人的纪念照的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x101,
        "#1008F纪、纪念照……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x102,
        "#1054F好像是去旅游一样呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x17,
        (
            "#151F嘿嘿～我的想法不错吧？\x02\x03",

            "我希望大家都能永远记得\x01",
            "我们曾经一起来过这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_5959")

    label("loc_590C")


    ChrTalk(    #327
        0x17,
        (
            "#150F最后大家在一起\x01",
            "拍张纪念照吧～\x02\x03",

            "所以，希望大家能\x01",
            "一起回到这里来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5959")

    TalkEnd(0xFE)
    Return()

    # Function_10_57CE end

    def Function_11_595D(): pass

    label("Function_11_595D")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59BE"),
        (1, "loc_5F58"),
        (2, "loc_5F80"),
        (SWITCH_DEFAULT, "loc_5F83"),
    )


    label("loc_59BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BCE")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #328
        0x8,
        (
            "#021F哎呀，好久不见。\x02\x03",

            "#021F呵呵，想不到会以\x01",
            "这种方式重逢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x10B,
        (
            "#214F这话是我要说的才对。\x02\x03",

            "真是的，一有什么事\x01",
            "你就拿出鞭子来抽人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x8,
        (
            "#027F我只是稍微\x01",
            "疼爱你一下而已嘛。\x02\x03",

            "#525F如果你喜欢被抽的话，\x01",
            "下次要不要再用力一点呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x10B,
        (
            "#216F从、从你嘴里说出来，\x01",
            "就不像是在开玩笑了呢……\x02\x03",

            "#416F总、总之……\x01",
            "既然已经到了这个地步，\x01",
            "我们就没什么好说的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x8,
        (
            "#020F若是互相仇视的话，\x01",
            "只是在帮结社的忙而已呢。\x02\x03",

            "不如我们暂时停战吧。\x02\x03",

            "就让我期待\x01",
            "你的作战能力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x10B,
        (
            "#210F哼哼……\x01",
            "你、你等着瞧好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_A2(0x22A0)
    Jump("loc_5F55")

    label("loc_5BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3F")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #334
        0x8,
        (
            "#020F嗯嗯，既然如此，\x01",
            "从前的事情就不必再提。\x02\x03",

            "我们就彼此合作，\x01",
            "一起对抗结社吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F55")

    label("loc_5C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC4")

    ChrTalk(    #335
        0x8,
        (
            "#020F呼，照明总算\x01",
            "顺利恢复了。\x02\x03",

            "但愿工程能够\x01",
            "因此有所进展……\x02\x03",

            "那么，我也该去找一些\x01",
            "力所能及的事情来做了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_5D00")

    label("loc_5CC4")


    ChrTalk(    #336
        0x8,
        (
            "#020F照明顺利恢复了呢。\x02\x03",

            "但愿工程能够\x01",
            "因此有所进展……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D00")

    Jump("loc_5F55")

    label("loc_5D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_5F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F08")

    ChrTalk(    #337
        0x101,
        (
            "#1011F雪拉姐\x01",
            "在这里帮忙修理吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #338
        0x8,
        (
            "#020F拉赛尔博士托我\x01",
            "检查照明设备。\x02\x03",

            "看来似乎很快就能\x01",
            "换回正常的照明了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E39")

    ChrTalk(    #339
        0x107,
        (
            "#561F对、对不起，雪拉姐。\x02\x03",

            "这种事原本\x01",
            "应该是我来做的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #340
        0x8,
        (
            "#021F呵呵，不用客气\x02\x03",

            "#525F提妲你就集中精力\x01",
            "进行探索去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x107,
        "#560F是、是的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F02")

    label("loc_5E39")


    ChrTalk(    #342
        0x101,
        "#1018F啊，已经亮起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        "#1040F看来修理进行得很顺利呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x8,
        (
            "#021F嗯，大家都在努力。\x02\x03",

            "#525F你们不好好努力的话\x01",
            "也会没有面子的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        "#1006F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x102,
        "#1040F我们会尽快进行探索的。\x02",
    )

    CloseMessageWindow()

    label("loc_5F02")

    OP_A2(0x22C4)
    Jump("loc_5F55")

    label("loc_5F08")


    ChrTalk(    #347
        0x8,
        (
            "#020F舰内似乎很快就能\x01",
            "明亮起来了哦。\x02\x03",

            "目前修复工作\x01",
            "看来进行得很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F55")

    Jump("loc_5F86")

    label("loc_5F58")


    ChrTalk(    #348
        0x8,
        "#020F哎呀？要更换成员了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_5F86")

    label("loc_5F80")

    Jump("loc_5F86")

    label("loc_5F83")

    Jump("loc_5F86")

    label("loc_5F86")

    TalkEnd(0xFE)
    Return()

    # Function_11_595D end

    def Function_12_5F8A(): pass

    label("Function_12_5F8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x7A)
    OP_D2(0x270009, 0x27000D, 0x5)
    OP_D2(0x70065, 0x7006D, 0x6)
    OP_D2(0x26015F, 0x260164, 0x1D)
    OP_D2(0x270019, 0x27001D, 0x1E)
    OP_D2(0x70025, 0x7002D, 0x1F)
    OP_D2(0x70035, 0x7003D, 0x20)
    OP_D2(0x2703A1, 0x2703A5, 0x21)
    OP_D2(0x70055, 0x7005D, 0x22)
    OP_D2(0x26001F, 0x260024, 0x23)
    OP_D2(0x70075, 0x7007D, 0x24)
    OP_D2(0x270089, 0x27008D, 0x25)
    OP_D2(0x600AC, 0x600B1, 0x26)
    OP_D2(0x2600AA, 0x2600AF, 0x27)
    OP_D2(0x600CC, 0x600D1, 0x28)
    OP_D2(0x60035, 0x6003A, 0x29)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 30)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 34)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 35)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 36)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 37)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x16, 38)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 39)
    SetChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 24)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x15, 0x2)
    SetChrSubChip(0x15, 24)
    SetChrChipByIndex(0x15, 19)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrFlags(0xE, 0x2)
    SetChrSubChip(0xE, 24)
    SetChrChipByIndex(0xE, 10)
    SetChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 24)
    SetChrChipByIndex(0xF, 8)
    SetChrFlags(0x10, 0x2)
    SetChrSubChip(0x10, 24)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(790, 2000, 90690, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0xC, 0x0)
    OP_4A(0xA, 255)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x16, 1300, 2000, 88300, 90)
    SetChrPos(0x17, 2000, 1900, 87630, 180)
    SetChrPos(0xC, -1960, 2000, 93000, 180)
    SetChrPos(0xA, -2110, 2000, 92110, 0)
    SetChrPos(0x9, 0, 2000, 88300, 0)
    SetChrPos(0x8, -1200, 2000, 88440, 45)
    SetChrPos(0x13, -2800, 2000, 89500, 90)
    SetChrPos(0x12, -2600, 2000, 88360, 0)
    SetChrPos(0xB, -2100, 2000, 86560, 0)
    SetChrPos(0x101, -300, 1500, 90550, 270)
    SetChrPos(0x102, -400, 2000, 91290, 180)
    SetChrPos(0x14, 600, 2000, 90100, 270)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x1)
    SetChrSubChip(0x101, 4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("少年的声音")

    AnonymousTalk(    #349
        (
            "\x07\x00……………艾………蒂尔…………\x02\x03",

            "……艾丝……尔………醒醒………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 120, -1, -1)
    SetChrName("青年的声音")

    AnonymousTalk(    #350
        (
            "\x07\x00……你没事吧……\x01",
            "………艾丝……蒂尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 200, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #351
        "\x07\x00#1003F……嗯…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x101, 7)
    Sleep(500)

    ChrTalk(    #352
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x14,
        "#1062F#2P太好了……你醒了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x102,
        (
            "#1043F#5P你没事吧？\x01",
            "有没有受伤？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xBB8)
    SetChrSubChip(0x101, 5)
    Sleep(700)

    ChrTalk(    #355
        0x101,
        "#1013F#4P啊……嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrPos(0x101, -340, 2000, 90400, 270)
    SetChrFlags(0x101, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    OP_8C(0x101, 270, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 45, 400)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    Fade(250)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #356
        0x101,
        (
            "#1025F#6P……只是膝盖\x01",
            "稍微擦伤而已……\x02\x03",

            "#1003F………大家呢………？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6502():
        OP_6D(-230, 2000, 89260, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6502)

    def lambda_651A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_651A)
    Sleep(100)

    def lambda_652D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_652D)
    Sleep(100)

    def lambda_6540():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6540)
    WaitChrThread(0x101, 0x1)
    OP_9E(0x12, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_0D()
    Sleep(300)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #357
        0x12,
        "#552F#6P嗯，总算都没事……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x13, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 6)
    OP_8C(0x13, 90, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x13, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 16)
    OP_8C(0x13, 90, 0)
    OP_0D()

    ChrTalk(    #358
        0x13,
        "#562F#6P……呼、呼………\x02",
    )

    CloseMessageWindow()
    OP_9E(0xA, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 20)
    TurnDirection(0x13, 0x101, 400)
    OP_0D()
    OP_8C(0xA, 180, 400)
    Sleep(200)
    OP_8C(0xC, 180, 400)

    ChrTalk(    #359
        0xA,
        "#1381F我、我……没事……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(300)
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #360
        0x9,
        (
            "#034F哎呀呀……\x01",
            "好惊险啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    OP_0D()
    Sleep(300)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #361
        0x8,
        (
            "#025F#6P呼……\x01",
            "还以为没救了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    ClearChrFlags(0xB, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0xB,
        (
            "#572F#6P可以说是\x01",
            "九死一生呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0xFFFFFED4, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #363
        0x17,
        (
            "#151F#5P……嘿嘿……\x02\x03",

            "这么多东西……\x01",
            "我怎么吃得完嘛……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x96, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #364
        0x16,
        (
            "#145F#6P唉……真是的。\x02\x03",

            "#144F喂，朵洛希！\x01",
            "已经是早上了！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x17, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(500)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 23)
    SetChrPos(0x17, 2430, 2000, 87860, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #365
        0x17,
        "#153F#2P啊……奈尔前辈……？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x16, 22)
    TurnDirection(0x16, 0x17, 0)
    OP_0D()
    Sleep(300)

    def lambda_689A():
        OP_6D(-1070, 2000, 94550, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_689A)

    def lambda_68B2():
        OP_67(0, 6250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68B2)

    def lambda_68CA():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_68CA)
    OP_8C(0xC, 0, 200)
    OP_8E(0xC, 0xFFFFF880, 0x7D0, 0x170AC, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #366
        0xC,
        "#178F#6P你们怎么样？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x15, 0x2)
    SetChrSubChip(0x15, 2)
    SetChrChipByIndex(0x15, 19)
    OP_0D()
    Sleep(300)

    ChrTalk(    #367
        0x15,
        "#272F#5P……没问题。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_9E(0x11, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #368
        0x11,
        "#102F#5P总、总算平安无事。\x02",
    )

    CloseMessageWindow()
    OP_9E(0xF, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 8)
    OP_0D()
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #369
        0xF,
        "#2P……没问题……\x02",
    )

    CloseMessageWindow()
    OP_9E(0xE, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0xE, 0x2)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 10)
    OP_0D()
    SetChrSubChip(0xE, 1)
    Sleep(300)

    ChrTalk(    #370
        0xE,
        "#5P我、我们这边也还好……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 9)
    OP_0D()
    SetChrSubChip(0x10, 2)
    Sleep(300)

    ChrTalk(    #371
        0x10,
        "#5P还、还以为要死了呢……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #372
        0xC,
        (
            "#176F#6P……简直是奇迹。\x02\x03",

            "#175F或者说……\x01",
            "只是对方手下留情了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #373
        0x101,
        "#1020F#5P对、对了！\x02",
    )

    CloseMessageWindow()

    def lambda_6B07():
        OP_6D(130, 2000, 91180, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B07)

    def lambda_6B1F():
        OP_67(0, 5740, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B1F)

    def lambda_6B37():
        OP_6B(3300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6B37)

    def lambda_6B47():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B47)
    Sleep(50)

    def lambda_6B5A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B5A)
    Sleep(50)

    def lambda_6B6D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6B6D)
    Sleep(50)

    def lambda_6B80():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6B80)
    Sleep(50)

    def lambda_6B93():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6B93)
    Sleep(50)
    OP_8C(0xC, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #374
        0x101,
        (
            "#1020F#6P刚才骑在攻击埃尔赛尤的\x01",
            "那个黑色家伙上的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x102,
        (
            "#1035F#5P……嗯。\x02\x03",

            "#1042F肯定是莱维没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x12,
        "#057F#6P……那家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xB,
        (
            "#074F#6P这样看来的话，\x01",
            "或许的确是手下留情了。\x02\x03",

            "#072F只要他愿意的话，\x01",
            "我们已经完全被击落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x101,
        "#1007F#6P……心情真复杂啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x102,
        "#1043F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #380
        0xA,
        (
            "#1163F#5P说起来……\x01",
            "我们坠落在哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xC,
        (
            "#176F#5P好像是在浮游都市的外围……\x02\x03",

            "#178F看来先到外面去\x01",
            "确认一下状况比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5900   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_5F8A end

    def Function_13_6D8D(): pass

    label("Function_13_6D8D")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_22(0x7A, 0x1, 0x50)
    OP_6F(0xC, 0)
    OP_6D(1350, 2000, 100510, 0)
    OP_67(0, 5430, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0x15, 19)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    SetChrPos(0x13, -1810, 2000, 91450, 0)
    SetChrPos(0x8, -420, 2000, 91880, 0)
    SetChrPos(0x12, -2780, 2000, 90100, 0)
    SetChrPos(0x9, 90, 2000, 90050, 0)
    SetChrPos(0x14, -1020, 2000, 90470, 0)
    SetChrPos(0xB, -2200, 2000, 88980, 0)
    SetChrPos(0x16, -990, 2000, 88600, 0)
    SetChrPos(0x17, 100, 2000, 88430, 0)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 9)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0xC, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_44(0x10, 0x0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x15, 255)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0xF, 2)
    OP_76(0x7, 0x0, 0x1, 0xFFFFFFF7, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)

    def lambda_6F9E():
        OP_6D(670, 2000, 94500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F9E)

    def lambda_6FB6():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FB6)

    def lambda_6FCE():
        OP_6B(3420, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6FCE)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #382
        0x8,
        "#023F#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x14,
        "#1067F#6P没、没赶得上吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x12,
        "#055F#6P不、不会吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x13,
        "#065F#5P讨、讨厌……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #386
        0x13,
        "#069F#5P#3S不要啊啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #387
        0xA,
        (
            "#1166F#6P尤莉亚小姐！\x01",
            "拜托了！\x02\x03",

            "从避难通道的方向来考虑\x01",
            "艾丝蒂尔她们\x01",
            "应该在西北边！\x02\x03",

            "请把埃尔赛尤号开往那里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xC,
        (
            "#175F#5P……非常抱歉……\x02\x03",

            "即便是殿下的命令，\x01",
            "也请恕我……无法遵命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x15,
        (
            "#272F#5P……埃尔赛尤号的动力\x01",
            "也没有完全恢复。\x02\x03",

            "如果现在再次接近浮游都市，\x01",
            "肯定会被卷入崩塌之中的。\x02\x03",

            "#276F是这样吧，拉赛尔博士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x11,
        "#102F#6P……没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xA,
        "#1169F#6P……怎、怎么会…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x9,
        (
            "#034F#6P哈哈……真失败……\x02\x03",

            "想要缓和气氛，\x01",
            "脑子里却一片空白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xB,
        "#572F#6P……嗯，我也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x16,
        (
            "#145F#6P这两个家伙……呜呜……\x02\x03",

            "都已经走到这一步了……\x01",
            "……竟然会变成这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x17,
        (
            "#156F#4P小艾……\x01",
            "……约修亚……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #396
        0x17,
        "#153F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_7337():
        OP_6D(890, 2000, 93900, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7337)

    def lambda_734F():
        OP_67(0, 5800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_734F)

    def lambda_7367():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7367)
    Sleep(50)

    def lambda_737A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_737A)
    Sleep(50)

    def lambda_738D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_738D)
    Sleep(50)

    def lambda_73A0():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_73A0)
    Sleep(50)

    def lambda_73B3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_73B3)
    Sleep(50)

    def lambda_73C6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_73C6)
    Sleep(50)

    def lambda_73D9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_73D9)
    Sleep(50)
    OP_8C(0x16, 90, 400)
    Sleep(500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #397
        0x16,
        (
            "#142F#6P喂……朵洛希……\x02\x03",

            "这种时候\x01",
            "……你就安静一点吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x17,
        (
            "#150F#4P不，那个……\x02\x03",

            "#151F基库好像\x01",
            "很高兴地飞出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x16,
        "#143F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #400
        0xC,
        "#173F#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_74C1():
        OP_6D(1350, 2000, 100510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74C1)

    def lambda_74D9():
        OP_67(0, 4000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_74D9)

    def lambda_74F1():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_74F1)

    def lambda_7501():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7501)
    Sleep(50)

    def lambda_7514():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7514)
    Sleep(50)

    def lambda_7527():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7527)
    Sleep(50)

    def lambda_753A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_753A)
    Sleep(50)

    def lambda_754D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_754D)
    Sleep(50)

    def lambda_7560():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7560)
    Sleep(50)

    def lambda_7573():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7573)
    Sleep(50)
    OP_8C(0x16, 0, 400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_6D8D end

    def Function_14_75A2(): pass

    label("Function_14_75A2")

    SetChrChipByIndex(0x18, 30)
    SetChrChipByIndex(0x19, 30)
    SetChrChipByIndex(0x1A, 30)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_4A(0x18, 0)
    OP_4A(0x19, 0)
    OP_4A(0x1A, 0)
    Sleep(2000)
    SetChrChipByIndex(0x18, 27)
    SetChrChipByIndex(0x19, 27)
    SetChrChipByIndex(0x1A, 27)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_4B(0x18, 0)
    OP_4B(0x19, 0)
    OP_4B(0x1A, 0)
    Return()

    # Function_14_75A2 end

    SaveToFile()

Try(main)
