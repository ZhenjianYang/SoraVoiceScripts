from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0111   ._SN',
        MapName             = 'Event',
        Location            = 'E0111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '乔丝特',                               # 9
        '多伦',                                 # 10
        '吉尔',                                 # 11
        '空贼雷古',                             # 12
        '通信员利昂',                           # 13
        '空贼阿伦',                             # 14
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
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT07/CH02110 ._CH',             # 01
        'ED6_DT07/CH02120 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT07/CH02110P._CP',             # 01
        'ED6_DT07/CH02120P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 51600,
        TriggerZ            = 0,
        TriggerY            = 74000,
        TriggerRange        = 1000,
        ActorX              = 51600,
        ActorZ              = 1000,
        ActorY              = 74000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_297",          # 01, 1
        "Function_2_351",          # 02, 2
        "Function_3_367",          # 03, 3
        "Function_4_B49",          # 04, 4
        "Function_5_F27",          # 05, 5
        "Function_6_121F",         # 06, 6
        "Function_7_147E",         # 07, 7
        "Function_8_1C58",         # 08, 8
        "Function_9_1CDF",         # 09, 9
        "Function_10_1D72",        # 0A, 10
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_208")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_275")

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_275")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -22620, 650, 5630, 135)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_296")
    Event(0, 6)

    label("loc_296")

    Return()

    # Function_0_1AE end

    def Function_1_297(): pass

    label("Function_1_297")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_31B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_345")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_D0(5000, 0)
    OP_51(0xA, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_350")

    label("loc_345")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)
    OP_71(0x1, 0x4)

    label("loc_350")

    Return()

    # Function_1_297 end

    def Function_2_351(): pass

    label("Function_2_351")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_366")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_351")

    label("loc_366")

    Return()

    # Function_2_351 end

    def Function_3_367(): pass

    label("Function_3_367")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674")
    OP_A2(0x22CA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_END)), "loc_4D4")

    ChrTalk(    #0
        0xA,
        (
            "#200F哟，是你们吗。\x02\x03",

            "航行控制的毛病\x01",
            "总算已经解决了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C")

    ChrTalk(    #1
        0x10B,
        (
            "#213F真、真的吗？\x02\x03",

            "#211F太棒了！\x01",
            "不愧是吉尔哥啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_43A")

    label("loc_40C")


    ChrTalk(    #2
        0x101,
        (
            "#1011F啊，真的吗？\x01",
            "那不是很好吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_43A")


    ChrTalk(    #3
        0xA,
        (
            "#200F其实，这全都多亏了\x01",
            "拉赛尔博士的建议。\x02\x03",

            "真是个了不起的老爷爷啊。\x01",
            "连看都没看过，就可以\x01",
            "马上说出故障的部位。\x02\x03",

            "果然不愧是世界著名的\x01",
            "导力学者啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_671")

    label("loc_4D4")


    ChrTalk(    #4
        0xA,
        (
            "#200F哟，是你们吗。\x02\x03",

            "航行控制方面出了一些毛病，\x01",
            "不过总算已经解决了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_576")

    ChrTalk(    #5
        0x10B,
        (
            "#211F嘿嘿，吉尔哥果然厉害。\x02\x03",

            "简直比导力技师\x01",
            "还要了不起呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_5D0")

    label("loc_576")


    ChrTalk(    #6
        0x101,
        (
            "#1011F哟～挺了不起的嘛。\x01",
            "居然可以自己一个人修理。\x02\x03",

            "真是没有辜负空贼的称号呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_5D0")


    ChrTalk(    #7
        0xA,
        (
            "#200F不，其实都多亏了\x01",
            "拉赛尔博士的建议。\x02\x03",

            "我们通过导力通信进行联络，\x01",
            "他马上就找到了原因。\x02\x03",

            "真是好厉害的老爷爷呢，\x01",
            "身为世界著名的导力学者，\x01",
            "果然是名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671")

    Jump("loc_6E6")

    label("loc_674")


    ChrTalk(    #8
        0xA,
        (
            "#200F拉赛尔博士\x01",
            "果然是个了不起的学者啊，\x02\x03",

            "只是听了一下症状，\x01",
            "马上就能找到故障部位……\x01",
            "真是个了不起的老爷子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E6")

    Jump("loc_B45")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_707")
    Call(0, 7)
    OP_A2(0x5)
    Return()

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_754")

    ChrTalk(    #9
        0xA,
        (
            "#200F终端的密码吗？\x01",
            "确实有这个可能。\x02\x03",

            "总之有试一试\x01",
            "的价值呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B45")

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2")

    ChrTalk(    #10
        0xA,
        "#203F呼，真是麻烦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B0")

    ChrTalk(    #11
        0x10B,
        "#213F吉尔哥，有什么麻烦吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_7D1")

    label("loc_7B0")


    ChrTalk(    #12
        0x101,
        "#1002F有什么问题吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_7D1")


    ChrTalk(    #13
        0xA,
        (
            "#207F嗯，航行控制这方面，\x01",
            "稍微出了点问题。\x02\x03",

            "虽然可以勉强起飞，\x01",
            "但飞行中的姿势无法稳定。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_856")

    ChrTalk(    #14
        0x10B,
        "#215F是、是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_887")

    label("loc_856")


    ChrTalk(    #15
        0x101,
        (
            "#1019F虽、虽然听不大懂\x01",
            "不过看起来很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_887")


    ChrTalk(    #16
        0xA,
        (
            "#206F船体的修复还算可以，\x01",
            "但精密仪器就无能为力了。\x02\x03",

            "不如和『埃尔赛尤』\x01",
            "联络一下寻求帮助吧。\x02\x03",

            "也不知道在通信中\x01",
            "能不能解决问题…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FB")

    ChrTalk(    #17
        0x101,
        (
            "#1015F嗯……\x01",
            "提妲不能帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#561F我、我虽然懂得一点……\x01",
            "不过最好还是让专业人员来做。\x02\x03",

            "因为飞翔引擎在飞船中\x01",
            "是最为复杂的部分了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #19
        0x101,
        "#1004F有、有那么复杂啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1043F看来只能够\x01",
            "询问一下了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    Jump("loc_AB6")

    label("loc_9FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A62")

    ChrTalk(    #21
        0x10B,
        (
            "#210F不过也只有试试看了。\x02\x03",

            "难得这次可以彼此携手合作，\x01",
            "要是不利用一下就太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB6")

    label("loc_A62")


    ChrTalk(    #22
        0x101,
        (
            "#1011F不过，还是有\x01",
            "试试看的必要吧？\x02\x03",

            "拉赛尔博士也在上面，\x01",
            "或许可以给点提示哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB6")


    ChrTalk(    #23
        0xA,
        (
            "#200F啊，说的也是啊……\x02\x03",

            "还是再耐心地\x01",
            "等一等吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2296)
    Jump("loc_B45")

    label("loc_AF2")


    ChrTalk(    #24
        0xA,
        (
            "#200F航行控制的问题\x01",
            "凭我们是解决不了的。\x02\x03",

            "毕竟这种精密仪器\x01",
            "可不能随便应付的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B45")

    TalkEnd(0xFE)
    Return()

    # Function_3_367 end

    def Function_4_B49(): pass

    label("Function_4_B49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_D31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")
    OP_A2(0x1)

    ChrTalk(    #25
        0xB,
        (
            "噢，小姐，\x01",
            "联络工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "多亏『埃尔赛尤』的帮忙，\x01",
            "飞翔引擎也修理好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "双方一起协力合作，\x01",
            "果然是有所价值啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C")

    label("loc_BEE")


    ChrTalk(    #28
        0xB,
        (
            "多亏『埃尔赛尤』的帮忙，\x01",
            "飞翔引擎也修理好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "呼，毕竟要是帮不上忙的话，\x01",
            "协力合作就没有什么价值了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5C")

    Jump("loc_D2E")

    label("loc_C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE0")
    OP_A2(0x2)

    ChrTalk(    #30
        0xB,
        (
            "控制装置的故障\x01",
            "似乎也已经解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "那么～我们也要\x01",
            "赶紧调整计量器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "再磨磨蹭蹭的话\x01",
            "会被老大骂的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2E")

    label("loc_CE0")


    ChrTalk(    #33
        0xB,
        (
            "控制装置的故障\x01",
            "似乎也已经解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "那么～我们也要\x01",
            "赶紧调整计量器了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2E")

    Jump("loc_F23")

    label("loc_D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA3")
    OP_A2(0x2)

    ChrTalk(    #35
        0xC,
        (
            "\x07\x05#2P#1S……这里是埃尔赛尤号……\x01",
            "……山猫号，请回答。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        "\x07\x05#2P#1S……重复，山猫号请回答。\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        "\x07\x00#1P嗯嗯，我是山猫号……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "\x07\x00#1P接收信号良好……\x01",
            "埃尔赛尤号，你们那里听得清楚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "\x07\x05#2P#1S埃尔赛尤呼叫山猫号……\x01",
            "我们这边的信号也很好。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        (
            "\x07\x05#2P#1S贵舰现在有\x01",
            "什么物资不足吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "\x07\x05#2P#1S重复……\x01",
            "山猫号，有什么物资不足吗……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F23")

    label("loc_EA3")


    ChrTalk(    #42
        0xB,
        (
            "\x07\x00#1P呃～其实我们的航行控制装置\x01",
            "出了点问题无法解决，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "\x07\x00#1P希望贵舰的维修人员能提供建议。\x01",
            "重复一次，希望贵舰的维修员…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F23")

    TalkEnd(0xFE)
    Return()

    # Function_4_B49 end

    def Function_5_F27(): pass

    label("Function_5_F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1080")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")
    OP_A2(0x3)
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #44
        0xD,
        (
            "啊，小姐……\x01",
            "你辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "飞翔引擎也修好了，\x01",
            "现在已经完全恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "『山猫号』马上\x01",
            "就能完全复原了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1024")

    label("loc_FC7")

    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #47
        0xD,
        (
            "飞翔引擎也修好了，\x01",
            "现在已经完全恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "『山猫号』马上\x01",
            "就能完全复原了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1024")

    Jump("loc_107D")

    label("loc_1027")


    ChrTalk(    #49
        0xFE,
        (
            "飞翔引擎修复完毕\x01",
            "可真是个好消息啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "这样看来的话，\x01",
            "就可以从这里逃出去了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107D")

    Jump("loc_121B")

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_121B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F8")
    TurnDirection(0xD, 0x10B, 0)
    OP_A2(0x3)

    ChrTalk(    #51
        0xD,
        "啊，小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        (
            "嘿嘿，刚才您\x01",
            "真是太帅了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "小姐果然\x01",
            "是我们的女神啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1147")

    label("loc_10F8")

    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #54
        0xD,
        (
            "嘿嘿，刚才您\x01",
            "真是太帅了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "我们会努力修船，\x01",
            "请小姐耐心期待吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1147")

    Jump("loc_121B")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BD")
    OP_A2(0x4)

    ChrTalk(    #56
        0xD,
        (
            "哦，是你们啊。\x01",
            "刚才多谢了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "『结社』的那群家伙\x01",
            "还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "你们最好\x01",
            "也多加小心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_11BD")


    ChrTalk(    #59
        0xD,
        (
            "『结社』的那群家伙\x01",
            "还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "我们本来也有相当的实力，\x01",
            "但却完全不是他们的对手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121B")

    TalkEnd(0xFE)
    Return()

    # Function_5_F27 end

    def Function_6_121F(): pass

    label("Function_6_121F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x12A, -25710, -500, 6350, 158)
    SetChrPos(0x129, -26570, -500, 5830, 143)
    SetChrPos(0x146, -26910, -500, 4600, 90)
    SetChrPos(0x102, -25290, -500, 3650, 0)
    OP_6D(-25995, -500, 5000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #61
        0x12A,
        (
            "#203F#2P不行……\x01",
            "没有启动钥匙就动不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x129,
        "#197F可恶……都走到这一步了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1033F#6P看上去确实不像那种\x01",
            "能轻易破坏的锁。\x02\x03",

            "#1030F还是去找启动钥匙比较快吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x146,
        (
            "#214F#5P果、果然是在\x01",
            "这里的守备队长手中吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1031F#6P恐怕是的。\x02\x03",

            "应该有一间队长室的，\x01",
            "我们先去调查那里吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -23370, 0, 3020, 90)
    SetChrPos(0x1, -23370, 0, 3020, 90)
    SetChrPos(0x2, -23370, 0, 3020, 90)
    SetChrPos(0x3, -23370, 0, 3020, 90)
    OP_6D(-23370, 0, 3020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(500)
    OP_A2(0x1805)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_6_121F end

    def Function_7_147E(): pass

    label("Function_7_147E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A3")
    Call(0, 8)
    Call(0, 9)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_14A3")

    Fade(500)
    OP_6D(44790, 100, 7060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 45590, 0, 5520, 0)
    SetChrPos(0x102, 46620, 0, 5450, 0)
    SetChrPos(0xF8, 45580, 0, 4260, 0)
    SetChrPos(0xF9, 47010, 0, 4130, 0)
    OP_8C(0xA, 180, 0)
    OP_4A(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xA,
        (
            "#200F#2P对了……忘了一件事。\x02\x03",

            "你们听过\x01",
            "『Ｏ·Ｒ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ』\x01",
            "这个词吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1004F#6P那、那是什么？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #68
        0x10B,
        (
            "#213F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738")

    label("loc_15EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1632")

    ChrTalk(    #69
        0x105,
        (
            "#1164F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738")

    label("loc_1632")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #70
        0x104,
        (
            "#030F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738")

    label("loc_1674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B7")

    ChrTalk(    #71
        0x109,
        (
            "#1060F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738")

    label("loc_16B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F9")

    ChrTalk(    #72
        0x107,
        (
            "#064F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738")

    label("loc_16F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1738")

    ChrTalk(    #73
        0x106,
        (
            "#555F#6PＯＲＰＨＥＵＳ……\x01",
            "是读作奥菲斯吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1738")


    ChrTalk(    #74
        0x102,
        "#1044F#6P……这个词怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#206F#2P没什么，只是监视我们的\x01",
            "猎兵们曾经提到过它。\x02\x03",

            "我觉得它可能有什么含义，\x01",
            "所以就记下来了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(    #76
        0x10B,
        "#210F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "确实让人很在意呢。\x02\x03",

            "#1004F（啊……或许是！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186E")

    label("loc_182C")


    ChrTalk(    #78
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "确实让人很在意呢。\x02\x03",

            "#1004F（啊……或许是！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186E")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #79
        "\x18\x07\x05关于这个词你有什么线索吗？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【工业区域的通称】\x01",      # 0
            "【福音的正式名称】\x01",      # 1
            "【终端密码】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_192A"),
        (1, "loc_19D7"),
        (2, "loc_1A8D"),
        (SWITCH_DEFAULT, "loc_1AFE"),
    )


    label("loc_192A")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        (
            "#1035F#4P不，工业区域的名字\x01",
            "应该是『法克特里亚』哦。\x02\x03",

            "#1040F莫非是……\x01",
            "工业区域的终端所要求输入\x01",
            "的密码也说不定啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #81
        0x101,
        "#1018F#5P是……是那个啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_19D7")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #82
        0x102,
        (
            "#1035F#4P不，『福音』这名字\x01",
            "在这座都市里似乎也是\x01",
            "同样的叫法。\x02\x03",

            "#1040F或许是……\x01",
            "工业区域的终端所要求输入\x01",
            "的密码也说不定啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #83
        0x101,
        "#1018F#5P是……是那个啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1A8D")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #84
        0x102,
        (
            "#1040F#4P嗯。\x01",
            "大概就是工业区域车站的终端密码。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #85
        0x101,
        "#1018F#5P啊，约修亚你也这么认为？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1AFE")


    ChrTalk(    #86
        0xA,
        "#206F#2P？　怎么回事？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    OP_8C(0x101, 0, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #87
        (
            "\x07\x05将工业区域终端\x01",
            "需要密码口令才能打开地下道入口\x01",
            "的事情向吉尔说明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #88
        0xA,
        (
            "#200F#2P原来如此……\x01",
            "确实有这个可能。\x02\x03",

            "看来很有试一试的必要啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1006F#6P嘿嘿，果然没错吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C20")

    ChrTalk(    #90
        0x10B,
        "#211F#6P谢谢啦，吉尔哥！\x02",
    )

    CloseMessageWindow()

    label("loc_1C20")


    ChrTalk(    #91
        0x102,
        "#1040F#6P赶快去确认一下吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 0)
    OP_A2(0x222D)
    OP_28(0x9E, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_7_147E end

    def Function_8_1C58(): pass

    label("Function_8_1C58")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CD2"),
        (1, "loc_1CD8"),
        (SWITCH_DEFAULT, "loc_1CDE"),
    )


    label("loc_1CD2")

    OP_A2(0x1200)
    Jump("loc_1CDE")

    label("loc_1CD8")

    OP_A2(0x1201)
    Jump("loc_1CDE")

    label("loc_1CDE")

    Return()

    # Function_8_1C58 end

    def Function_9_1CDF(): pass

    label("Function_9_1CDF")

    FadeToDark(0, 0, -1)
    OP_6D(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_1CDF end

    def Function_10_1D72(): pass

    label("Function_10_1D72")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC5")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_1F83")

    label("loc_1DC5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #93
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F68")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x32)
    OP_73(0x0)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1F68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F82")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1F82")

    Return()

    label("loc_1F83")

    Return()

    # Function_10_1D72 end

    SaveToFile()

Try(main)
