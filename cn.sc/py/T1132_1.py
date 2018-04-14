from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1132_1 ._SN',
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
        "Function_1_1B2",          # 01, 1
        "Function_2_91D",          # 02, 2
        "Function_3_BD3",          # 03, 3
        "Function_4_238B",         # 04, 4
        "Function_5_23BB",         # 05, 5
        "Function_6_23F0",         # 06, 6
        "Function_7_2425",         # 07, 7
        "Function_8_246E",         # 08, 8
        "Function_9_24A3",         # 09, 9
        "Function_10_251A",        # 0A, 10
        "Function_11_34A9",        # 0B, 11
        "Function_12_34F9",        # 0C, 12
        "Function_13_35FF",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3")
    Return()

    label("loc_C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_DF")
    Call(1, 2)
    Jump("loc_E3")

    label("loc_DF")

    Call(1, 1)

    label("loc_E3")

    Jump("loc_1B1")

    label("loc_E6")

    OP_4A(0xB, 255)
    TalkBegin(0xB)

    ChrTalk(    #0
        0xB,
        (
            "此房间现在\x01",
            "归帝国大使馆使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        (
            "闲杂人等\x01",
            "请勿出入。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A0")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_1A0")

    OP_69(0xF6, 0x0)
    OP_30(0x0)
    OP_0D()
    TalkEnd(0xB)
    OP_4B(0xB, 255)

    label("loc_1B1")

    Return()

    # Function_0_AA end

    def Function_1_1B2(): pass

    label("Function_1_1B2")

    EventBegin(0x0)
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE")
    TurnDirection(0x4, 0xB, 0)

    label("loc_1EE")


    ChrTalk(    #2
        0xB,
        (
            "此房间现在\x01",
            "归帝国大使馆使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "闲杂人等\x01",
            "请勿出入。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_892")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8")

    ChrTalk(    #4
        0x106,
        "#052F这里是帝国大使馆的接待处吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        "是，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#050F有事的不是你们吗。\x02\x03",

            "我们是游击士协会的游击士。\x01",
            "看了公告板上的委托来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD")

    label("loc_2E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A")

    ChrTalk(    #8
        0x103,
        "#020F这里是帝国大使馆的接待处吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "是，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#020F有事的是你们吧。\x02\x03",

            "我们是游击士协会的游击士。\x01",
            "看了公告板上的委托来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD")

    label("loc_39A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")

    ChrTalk(    #12
        0x108,
        "#070F这里是帝国大使馆的接待处吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "是，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x108,
        (
            "#070F有事的不是你们吗。\x02\x03",

            "我们是游击士协会的游击士。\x01",
            "看了公告板上的委托来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD")

    label("loc_44E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")

    ChrTalk(    #16
        0x104,
        "#030F这里是帝国大使馆的接待处吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "是，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "……还以为是谁呢，\x01",
            "这不是奥利维尔吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        "今天来大使馆有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1000F有事的\x01",
            "不是你们吗？\x02\x03",

            "我们是游击士协会的游击士。\x01",
            "看了公告板上的委托来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD")

    label("loc_537")


    ChrTalk(    #21
        0x101,
        "#1011F这里是帝国大使馆的接待处？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "是，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1000F有事的\x01",
            "不是你们吗？\x02\x03",

            "我们是游击士协会的游击士。\x01",
            "看了公告板上的委托来到这里的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD")


    ChrTalk(    #25
        0xB,
        (
            "啊，是游击士吗？\x01",
            "真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "可以的话，我想\x01",
            "立即说明一下情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "你们方便吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78D")

    ChrTalk(    #28
        0x101,
        (
            "#1007F抱、抱歉……\x02\x03",

            "考虑了一下，\x01",
            "现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "噢，这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "那么，事情处理完后\x01",
            "麻烦再来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1000F那就先这样。\x02\x03",

            "#1015F总之我们现在\x01",
            "得先去一趟拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_773")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    OP_28(0x78, 0x1, 0x8000)
    Return()

    label("loc_78D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_800")

    ChrTalk(    #32
        0x101,
        "#1006F嗯，没问题哦。\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Return()

    label("loc_800")


    ChrTalk(    #33
        0x101,
        (
            "#1015F抱歉哦，\x01",
            "现在可不行。\x02\x03",

            "我们还有其他要事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        "噢，这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        (
            "那么，事情处理完后\x01",
            "麻烦再来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1000F嗯，就先这样。\x02",
    )

    CloseMessageWindow()
    OP_28(0x78, 0x1, 0x8000)

    label("loc_892")

    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_909")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_909")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_1_1B2 end

    def Function_2_91D(): pass

    label("Function_2_91D")

    EventBegin(0x0)
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_959")
    TurnDirection(0x4, 0xB, 0)

    label("loc_959")


    ChrTalk(    #37
        0xB,
        "各位，等候多时了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "要事已经处理完了吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(    #39
        0x101,
        (
            "#1007F抱、抱歉……\x01",
            "还不行呢。\x02\x03",

            "#1015F总之我们现在\x01",
            "得先去一趟拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5A")
    SetChrPos(0xFA, -128130, 0, 138000, 270)

    label("loc_A5A")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    OP_28(0x78, 0x1, 0x8000)
    Return()

    label("loc_A74")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")

    ChrTalk(    #40
        0x101,
        "#1006F嗯，没问题了。\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Return()

    label("loc_AE7")


    ChrTalk(    #41
        0x101,
        (
            "#1015F啊，抱歉哦。\x02\x03",

            "还得花点时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        "唔，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "没办法呢。\x01",
            "那么，请稍后再来。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBF")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_BBF")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_91D end

    def Function_3_BD3(): pass

    label("Function_3_BD3")


    ChrTalk(    #44
        0xB,
        "那么这边请。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "详细情况\x01",
            "由书记官来说明。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xB, 0x1)
    OP_44(0xB, 0x2)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6D(-123540, 0, 180180, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -130449, 0, 179930, 90)
    SetChrPos(0x101, -131450, 0, 179930, 90)
    SetChrPos(0xF7, -132450, 0, 179930, 90)
    SetChrPos(0xF8, -133450, 0, 179930, 90)
    SetChrPos(0xF9, -134450, 0, 179930, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD1")
    SetChrPos(0x4, -135450, 0, 179930, 90)

    label("loc_CD1")

    OP_4A(0xD, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_70(0x2, 0xE)

    def lambda_D08():
        OP_6D(-126280, 0, 181030, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D08)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFE0A5D, 0x0, 0x2C268, 0x7D0, 0x0)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #46
        0xB,
        (
            "阁下，游击士们\x01",
            "已经到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xA, 255)
    TurnDirection(0xA, 0xB, 400)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #47
        0xA,
        "#1101F喔喔，来了吗！\x02",
    )

    CloseMessageWindow()

    def lambda_D9F():

        label("loc_D9F")

        TurnDirection(0xD, 0x101, 400)
        OP_48()
        Jump("loc_D9F")

    QueueWorkItem2(0xD, 1, lambda_D9F)
    OP_43(0x101, 0x0, 0x1, 0x4)
    OP_43(0xF7, 0x0, 0x1, 0x5)
    OP_43(0xF8, 0x0, 0x1, 0x6)
    OP_43(0xF9, 0x0, 0x1, 0x7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD9")
    OP_43(0x4, 0x0, 0x1, 0x8)

    label("loc_DD9")


    def lambda_DDF():
        OP_6D(-125210, 0, 179480, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DDF)
    OP_8E(0xA, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    OP_8C(0xA, 270, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E20")
    WaitChrThread(0x4, 0x0)
    Jump("loc_E25")

    label("loc_E20")

    WaitChrThread(0xF9, 0x0)

    label("loc_E25")

    OP_44(0xB, 0x1)
    OP_43(0xB, 0x0, 0x1, 0x9)
    OP_44(0xD, 0x1)

    ChrTalk(    #48
        0xA,
        "#1100F啊，你们是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #49
        0x105,
        "#040F好久不见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E94")

    label("loc_E78")


    ChrTalk(    #50
        0x101,
        "#1011F啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    label("loc_E94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBD")

    ChrTalk(    #51
        0x108,
        "#070F唔，又见面了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_EBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(    #52
        0x104,
        (
            "#030F呼，真高兴看到\x01",
            "您一如既往地健康啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "#1100F呼……你也是。\x02",
    )

    CloseMessageWindow()

    label("loc_F13")


    ChrTalk(    #54
        0x101,
        (
            "#1000F那个，在王都时\x01",
            "十分感谢您的协助。\x02\x03",

            "#1015F话说回来，您怎么会在柏斯？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_FFF")

    ChrTalk(    #55
        0xA,
        (
            "#1102F嗯，因为签署仪式圆满结束，\x01",
            "日程总算空闲下来了。\x02\x03",

            "于是就来落实\x01",
            "早就预定好的视察了。\x02\x03",

            "#1100F遗憾的是由于超市事件的影响\x01",
            "成果并不怎么显著。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105D")

    label("loc_FFF")


    ChrTalk(    #56
        0xA,
        (
            "#1102F嗯，因为签署仪式圆满结束，\x01",
            "日程总算空闲下来了。\x02\x03",

            "于是就来落实\x01",
            "早就预定好的视察了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108F")

    ChrTalk(    #57
        0x103,
        "#020F原来如此，您在视察啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_111C")

    label("loc_108F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C1")

    ChrTalk(    #58
        0x106,
        "#050F原来如此，是在视察啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_111C")

    label("loc_10C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(    #59
        0x108,
        "#070F原来如此，您在视察啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_111C")

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_111C")

    ChrTalk(    #60
        0x104,
        "#030F呼，就是视察吧。\x02",
    )

    CloseMessageWindow()

    label("loc_111C")


    ChrTalk(    #61
        0xA,
        (
            "#1100F哼，不过这些事\x01",
            "就先管不了那么多了。\x02\x03",

            "#1101F总、总而言之现在\x01",
            "必须想方设法把勋章给找回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1004F那，那\x01",
            "什么勋章很重要吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#1103F喂，书记官！\x01",
            "还在磨蹭什么。\x02\x03",

            "还不赶快拿那个东西\x01",
            "给各位游击士看！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #64
        0xD,
        "是，这就拿来。\x02",
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xFFFE1DC6, 0x0, 0x2B9BC, 0x3E8, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8E(0xA, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1002F感、感觉大使\x01",
            "好像相当焦躁……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        "唔，这也难怪……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        (
            "这次的事件\x01",
            "对阁下来说确实是一件大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "不管怎么说那个勋章\x01",
            "可是皇帝陛下所赐的荣誉之物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        (
            "这个要是丢了，\x01",
            "阁下可就颜面扫地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "如果事情传到本国，\x01",
            "阁下就会成为帝都的笑柄吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016F帝都的笑柄……\x02\x03",

            "会不会说得\x01",
            "太夸张了点？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "不，身为帝国之人\x01",
            "虽不便大肆宣扬——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xD,
        (
            "但这种窘态\x01",
            "简直就是社交界的好靶子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "一旦流言传开，\x01",
            "绝非儿戏，到时必被\x01",
            "城中千夫所指。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1019F切，人们就爱议论些这个啊。\x02\x03",

            "#1007F呼……社交界\x01",
            "其实是很恐怖的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(    #76
        0x107,
        "#561F真、真的啊……\x02",
    )

    CloseMessageWindow()

    label("loc_149F")


    ChrTalk(    #77
        0xD,
        (
            "这就是活在政界\x01",
            "之人的宿命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "请各位过来的原因\x01",
            "能理解了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(    #79
        0x106,
        (
            "#053F原来如此。\x01",
            "基本上了解情况了。\x02\x03",

            "#050F那，大使所说的\x01",
            "『那个东西』是什么？\x02\x03",

            "看起来像是有什么\x01",
            "东西要给我们看似的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E1")

    label("loc_156F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E8")

    ChrTalk(    #80
        0x103,
        (
            "#025F嗯，情况明白了。\x02\x03",

            "#027F那，大使所说的\x01",
            "『那个东西』是什么？\x02\x03",

            "好像有什么\x01",
            "东西要给我们看似的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E1")

    label("loc_15E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1664")

    ChrTalk(    #81
        0x108,
        (
            "#070F噢，情况了解了。\x02\x03",

            "对了，大使所说的\x01",
            "『那个东西』是什么？\x02\x03",

            "看起来好像有什么\x01",
            "东西要给我们看似的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E1")

    label("loc_1664")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E1")

    ChrTalk(    #82
        0x104,
        (
            "#030F呼，情况了解啦。\x02\x03",

            "对了，大使所说的\x01",
            "『那个东西』到底是什么？\x02\x03",

            "看起来好像有什么\x01",
            "东西要给我们看似的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E1")


    ChrTalk(    #83
        0xD,
        "啊，其实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xD,
        (
            "现场留下了疑似\x01",
            "犯罪声明的卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x101,
        "#1004F卡、卡片吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        "是，就是这样的东西──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x05　　美丽的公主及其随从啊。　　\x01",
            "　  制裁的钟声终于近了……\x01",
            "    铁马的勋章也将落入吾手。\x02\x03",

            "　　   若想将之夺还\x01",
            "　　 就破解吾之谜题吧。　\x02\x03",

            "　　第一把钥匙为以下咒文──\x01",
            "　　 　ＲＩＣＵＬ\x01",
            "　　 　面背的花查调\x02\x03",

            "　   一切之终即为始。 　\x01",
            "　    汝，不可忘却。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AB8")

    ChrTalk(    #88
        0x101,
        (
            "#1007F真是，每次都这么麻烦。\x02\x03",

            "一直被他这样骚扰，\x01",
            "连发牢骚的心情都没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1980")

    ChrTalk(    #89
        0x108,
        (
            "#070F哈哈，这也算是一种觉悟吧。\x02\x03",

            "总之，再确认一次\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB5")

    label("loc_1980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DA")

    ChrTalk(    #90
        0x106,
        (
            "#552F这就是所谓举手投降了吧。\x02\x03",

            "#053F总之，再确认一下\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB5")

    label("loc_19DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(    #91
        0x103,
        (
            "#025F是说该举手投降了吗。\x02\x03",

            "#020F总之，再确认一下\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB5")

    label("loc_1A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB5")

    ChrTalk(    #92
        0x104,
        (
            "#030F持续的郁闷，\x01",
            "打算对方已经坚持不住……\x02\x03",

            "呼，简直就是游说的极致。\x02\x03",

            "那，这些暂且不论，\x01",
            "再确认一下卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB5")

    Jump("loc_1CB5")

    label("loc_1AB8")


    ChrTalk(    #93
        0x101,
        (
            "#1019F嗯、嗯…………\x02\x03",

            "这个怎么看\x01",
            "都是张暗号卡片吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1A")

    ChrTalk(    #94
        0x105,
        "#043F啊，看来是呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B54")

    ChrTalk(    #95
        0x104,
        (
            "#035F呼，劲敌的挑战……\x01",
            "就好好接招吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(    #96
        0x108,
        (
            "#073F怪盗绅士……\x01",
            "『噬身之蛇』的执行者吗。\x02\x03",

            "#072F传闻倒是听过，\x01",
            "好像是个相当特立独行的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C01")

    ChrTalk(    #97
        0x106,
        (
            "#050F唔，总之先确认一下\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB5")

    label("loc_1C01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3E")

    ChrTalk(    #98
        0x103,
        (
            "#022F唔，总之先确认一下\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB5")

    label("loc_1C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C7B")

    ChrTalk(    #99
        0x107,
        (
            "#560F总、总之再确认一次\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB5")

    label("loc_1C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB5")

    ChrTalk(    #100
        0x104,
        (
            "#030F总之应该先确认一下\x01",
            "卡片的要点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB5")

    OP_51(0x1E, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1CFA():
        OP_69(0x1E, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CFA)
    OP_8C(0x101, 270, 400)

    def lambda_1D0F():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1D0F)
    Sleep(100)

    def lambda_1D22():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1D22)
    Sleep(150)
    TurnDirection(0xF9, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D49")
    TurnDirection(0x4, 0x101, 400)

    label("loc_1D49")

    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #101
        0x101,
        (
            "#1002F嗯，关键在于\x01",
            "这个『ＲＩＣＵＬ』吧。\x02\x03",

            "出发点应该是\x01",
            "找出这个的意义吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1E")

    ChrTalk(    #102
        0x106,
        (
            "#050F这么说来，这字母后面的文章\x01",
            "应该才是最重要的部分啊。\x02\x03",

            "那些部分很可能\x01",
            "就是对这些字母的暗示。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7D")

    label("loc_1E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(    #103
        0x103,
        (
            "#022F这么说来，这字母后面的文章\x01",
            "应该才是最重要的部分啊。\x02\x03",

            "那些部分很可能\x01",
            "就是对这些字母的暗示。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7D")

    label("loc_1E94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0A")

    ChrTalk(    #104
        0x108,
        (
            "#070F这么说来，这字母后面的文章\x01",
            "应该才是最重要的部分啊。\x02\x03",

            "那些部分很可能\x01",
            "就是对这些字母的暗示。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7D")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F7D")

    ChrTalk(    #105
        0x104,
        (
            "#030F这么说来，这字母后面的文章\x01",
            "应该才是最重要的部分啊。\x02\x03",

            "那些部分很可能\x01",
            "就是对这些字母的暗示。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC3")

    ChrTalk(    #106
        0x105,
        (
            "#042F『一切之终即为始』对吧。\x02\x03",

            "记得是这样的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A3")

    label("loc_1FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201A")

    ChrTalk(    #107
        0x107,
        (
            "#062F『一切之终即为始』\x01",
            "……是说这个部分吧。\x02\x03",

            "嗯，确实像是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A3")

    label("loc_201A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2060")

    ChrTalk(    #108
        0x104,
        (
            "#030F『一切之终即为始』吗。\x02\x03",

            "记得是这样的话吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A3")

    label("loc_2060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A3")

    ChrTalk(    #109
        0x103,
        (
            "#027F『一切之终即为始』吧。\x02\x03",

            "记得是这样的话呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A3")


    ChrTalk(    #110
        0x101,
        (
            "#1002F作为开始调查的\x01",
            "线索已经足够充分了。\x02\x03",

            "首先以这个为线索，\x01",
            "在市内调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        "找到调查的起点了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_2119():
        OP_6D(-125210, 0, 179480, 1000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2119)

    def lambda_2131():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2131)
    Sleep(100)

    def lambda_2144():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2144)
    Sleep(150)
    OP_8C(0x101, 90, 400)

    def lambda_215E():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_215E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2179")
    OP_8C(0x4, 90, 400)

    label("loc_2179")

    WaitChrThread(0xB, 0x1)

    ChrTalk(    #112
        0x101,
        (
            "#1006F嗯，算是吧。\x02\x03",

            "那么，要是发现了什么\x01",
            "就会再过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        "喔，期待你们的表现。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #114
        0xA,
        (
            "#1100F已经开始调查了吗？\x02\x03",

            "那么，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #115
        0x101,
        "#1006F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x78, 0x4, 0x4)
    OP_28(0x78, 0x4, 0x8)
    OP_28(0x78, 0x1, 0x1)
    OP_28(0x78, 0x1, 0x2)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0x0, -125660, 0, 179040, 90)
    SetChrPos(0x1, -125660, 0, 179040, 90)
    SetChrPos(0x2, -125660, 0, 179040, 90)
    SetChrPos(0x3, -125660, 0, 179040, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B6")
    SetChrPos(0x4, -125660, 0, 179040, 90)

    label("loc_22B6")

    OP_69(0x0, 0x0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_30(0x0)
    OP_8C(0x101, 90, 0)
    OP_8C(0xF7, 90, 0)
    OP_8C(0xF8, 90, 0)
    OP_8C(0xF9, 90, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231A")
    OP_8C(0xFA, 90, 0)

    label("loc_231A")

    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233A")
    OP_4A(0x4, 255)

    label("loc_233A")

    SetChrPos(0xB, -127460, 0, 181340, 180)
    SetChrPos(0xD, -123490, 0, 178400, 45)
    SetChrPos(0xA, -122680, 0, 179240, 270)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    FadeToBright(1500, 0)
    EventEnd(0x0)
    Return()

    # Function_3_BD3 end

    def Function_4_238B(): pass

    label("Function_4_238B")

    OP_8E(0x101, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFE18C6, 0x0, 0x2BA48, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_4_238B end

    def Function_5_23BB(): pass

    label("Function_5_23BB")

    Sleep(400)
    OP_8E(0xF7, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFE140C, 0x0, 0x2BDB8, 0x7D0, 0x0)
    OP_8C(0xF7, 90, 400)
    Return()

    # Function_5_23BB end

    def Function_6_23F0(): pass

    label("Function_6_23F0")

    Sleep(800)
    OP_8E(0xF8, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF8, 0xFFFE166E, 0x0, 0x2B6BA, 0x7D0, 0x0)
    OP_8C(0xF8, 90, 400)
    Return()

    # Function_6_23F0 end

    def Function_7_2425(): pass

    label("Function_7_2425")

    Sleep(1200)
    OP_8E(0xF9, 0xFFFE0AF2, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF9, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF9, 0xFFFE11A0, 0x0, 0x2BADE, 0x7D0, 0x0)
    OP_8C(0xF9, 90, 400)
    Return()

    # Function_7_2425 end

    def Function_8_246E(): pass

    label("Function_8_246E")

    Sleep(1600)
    OP_8E(0x4, 0xFFFE0AF2, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0x4, 0xFFFE0E30, 0x0, 0x2B82C, 0x7D0, 0x0)
    OP_8C(0x4, 90, 400)
    Return()

    # Function_8_246E end

    def Function_9_24A3(): pass

    label("Function_9_24A3")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_72(0x2, 0x800)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x2)
    OP_71(0x2, 0x800)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFE0A5D, 0x0, 0x2C268, 0x7D0, 0x0)
    OP_8C(0xB, 90, 400)
    Return()

    # Function_9_24A3 end

    def Function_10_251A(): pass

    label("Function_10_251A")

    EventBegin(0x0)
    SetChrPos(0x101, -124730, 0, 178760, 90)
    SetChrPos(0xF7, -125890, 0, 178760, 90)
    SetChrPos(0xF8, -125330, 0, 177850, 90)
    SetChrPos(0xF9, -126540, 0, 178170, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257D")
    SetChrPos(0x4, -127440, 0, 178220, 90)

    label("loc_257D")

    SetChrPos(0xA, -123450, 0, 178760, 270)
    SetChrPos(0xD, -122420, 0, 179380, 270)
    SetChrPos(0xC, -128419, 0, 180840, 90)
    OP_6D(-125530, 0, 179560, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_0D()

    ChrTalk(    #116
        0xA,
        (
            "#1101F这、这是真的吗！\x02\x03",

            "呵，真的\x01",
            "找到勋章了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1006F#1P嗯，真的真的。\x02\x03",

            "唔，事实胜于雄辩哦。\x01",
            "勋章还给您了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #118
        "\x07\x02#16I宝剑天马大勋章\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #119
        0xA,
        (
            "#1101F喔、喔喔！\x01",
            "这确实是我的……！\x02\x03",

            "……幸、幸好没事……\x02\x03",

            "#1102F（沉～～默………………）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2749")
    OP_62(0xF6, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2787")

    label("loc_2749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2770")
    OP_62(0xF6, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2787")

    label("loc_2770")

    OP_62(0xF6, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2787")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B3")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_27F1")

    label("loc_27B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DA")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_27F1")

    label("loc_27DA")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_27F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2818")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2856")

    label("loc_2818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283F")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2856")

    label("loc_283F")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2856")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2882")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_28C0")

    label("loc_2882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A9")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_28C0")

    label("loc_28A9")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_28C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2909")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F2")
    OP_62(0x4, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2909")

    label("loc_28F2")

    OP_62(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2909")

    Sleep(1000)

    ChrTalk(    #120
        0x101,
        (
            "#1016F#1P打、打断您沉浸在欢乐中\x01",
            "非常抱歉……\x02\x03",

            "不过您要找的东西，\x01",
            "确实就是这个什么什么勋章吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0xA,
        (
            "#1101F怒……！？\x02\x03",

            "不是什么什么勋章，\x01",
            "是宝剑天马大勋章!!!\x02\x03",

            "居然那样称呼\x01",
            "荣誉的赏赐，真是没礼貌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1019F#1P#1S那、那么长\x01",
            "谁记得住啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        "#1100F你刚才说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#1P没、没有，没什么。\x02\x03",

            "不管怎样，是那个勋章\x01",
            "没错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "#1100F嗯，没有错。\x02\x03",

            "#1102F呼，总算\x01",
            "逃过一劫了。\x02\x03",

            "之后只要抓住\x01",
            "犯事的狂徒，\x01",
            "这事就算解决了……\x02\x03",

            "#1100F那么，有\x01",
            "犯人的眉目了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1015F#1P其实犯人我们早就知道是谁……\x02\x03",

            "#1007F遗、遗憾的是\x01",
            "其行踪却完全不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#1101F你说什么？\x01",
            "抓不到他吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BEB")

    ChrTalk(    #128
        0x106,
        (
            "#050F#1P马上抓到是不可能的。\x02\x03",

            "疑似犯人\x01",
            "是国际犯罪组织的一员。\x02\x03",

            "『怪盗Ｂ』这名字\x01",
            "您有在哪里听说过吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4F")

    label("loc_2BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C63")

    ChrTalk(    #129
        0x103,
        (
            "#026F#1P马上抓到是不可能的呢。\x02\x03",

            "疑似犯人\x01",
            "是国际犯罪组织的一员。\x02\x03",

            "#027F『怪盗Ｂ』这名字\x01",
            "您知道吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4F")

    label("loc_2C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(    #130
        0x108,
        (
            "#074F#1P马上抓到不可能吧。\x02\x03",

            "疑似犯人\x01",
            "是国际犯罪组织的一员。\x02\x03",

            "#072F『怪盗Ｂ』这名字\x01",
            "您不知道吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4F")

    label("loc_2CD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4F")

    ChrTalk(    #131
        0x104,
        (
            "#030F#1P马上抓到是不可能的呢。\x02\x03",

            "疑似犯人\x01",
            "是国际犯罪组织的一员。\x02\x03",

            "『怪盗Ｂ』这名字\x01",
            "您没有听说过吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4F")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0xA,
        (
            "#1101F你说『怪盗Ｂ』！？\x02\x03",

            "那家伙在利贝尔\x01",
            "出现了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1011F#1P啊，您果然知道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#1100F呼，嗯……\x02\x03",

            "他曾经一时间闹得帝国诸城\x01",
            "鸡犬不宁。\x02\x03",

            "#1102F他是连我们帝国军\x01",
            "都抓不住的男人……\x02\x03",

            "看来这次只是寻回勋章\x01",
            "就该谢天谢地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1003F#1P啊啊，真遗憾……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xA,
        (
            "#1102F………………………………\x02\x03",

            "#1100F……巴克雷书记官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xA,
        "#1100F那个准备好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xD,
        "是，在这边。\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0xB)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #140
        0xA,
        "#1100F呼……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_A2(0x16)
    OP_43(0xD, 0x1, 0x1, 0xB)
    Sleep(400)

    def lambda_2F24():
        OP_8C(0xA, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F24)
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #141
        0xA,
        (
            "#1100F无法抓到他\x01",
            "实在遗憾……\x02\x03",

            "但对方既是那个『怪盗Ｂ』\x01",
            "就不能再有抱怨了。\x02\x03",

            "诸位出色地找到了勋章，\x01",
            "确保了我帝国的威信。\x02\x03",

            "#1102F鉴于如此劳苦功高，\x01",
            "本埃雷波尼亚帝国大使馆──\x02\x03",

            "——特此授予铁骑功勋章。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #142
        "\x1F\x3C\x01\x07\x00被授予。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x13C, 1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_22(0xBF, 0x0, 0x64)

    ChrTalk(    #143
        0xD,
        "诸位，恭喜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        "恭喜！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_63(0xC)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D1")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_310F")

    label("loc_30D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30F8")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_310F")

    label("loc_30F8")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_310F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3136")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3174")

    label("loc_3136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315D")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3174")

    label("loc_315D")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3174")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A0")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_31DE")

    label("loc_31A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C7")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_31DE")

    label("loc_31C7")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_31DE")

    Sleep(1000)

    ChrTalk(    #145
        0x101,
        "#1015F#1P啊、啊啊…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3236")

    ChrTalk(    #146
        0x105,
        (
            "#045F突、突然就被\x01",
            "授予了勋章呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3265")

    ChrTalk(    #147
        0x107,
        "#562F好、好像有点难为情……\x02",
    )

    CloseMessageWindow()

    label("loc_3265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(    #148
        0x106,
        "#552F什么啊，这么突然……\x02",
    )

    CloseMessageWindow()

    label("loc_3292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D4")

    ChrTalk(    #149
        0x103,
        (
            "#025F还真是夸张呢……\x01",
            "这就是所谓的帝国国风吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3305")

    ChrTalk(    #150
        0x108,
        "#071F哈哈，这就是帝国特色啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3347")

    ChrTalk(    #151
        0x104,
        (
            "#031F呼，虽然习惯了，\x01",
            "但这次也感到有些意外啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3347")


    ChrTalk(    #152
        0xA,
        (
            "#1102F突然被授予此等荣誉，\x01",
            "你们迷惑的心情我可以理解。\x02\x03",

            "年轻时的我，\x01",
            "首次被授予勋章时也是这样……\x02\x03",

            "#1100F然而，没什么好退缩的。\x01",
            "这次的工作完全值得称赞。\x02\x03",

            "#1100F不要被受勋者之名而拖累，\x01",
            "期待你们今后的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1016F#1P啊，嗯……谢谢。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #154
        "\x07\x02任务【帝国大使的委托】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2)
    OP_28(0x78, 0x1, 0x100)
    OP_28(0x78, 0x4, 0x10)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_10_251A end

    def Function_11_34A9(): pass

    label("Function_11_34A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D6")
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFE212C, 0x0, 0x2BA20, 0x3E8, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("loc_34F8")

    label("loc_34D6")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFE21CC, 0x0, 0x2BCB4, 0x3E8, 0x0)
    OP_8C(0xFE, 270, 400)

    label("loc_34F8")

    Return()

    # Function_11_34A9 end

    def Function_12_34F9(): pass

    label("Function_12_34F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3506")
    Return()

    label("loc_3506")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3518")
    Return()

    label("loc_3518")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_3553")
    Call(1, 13)
    Jump("loc_35F8")

    label("loc_3553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_3562")
    Call(1, 13)
    Jump("loc_35F8")

    label("loc_3562")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_35BA")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #155
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_35F8")

    label("loc_35BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #156
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_35F8")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_34F9 end

    def Function_13_35FF(): pass

    label("Function_13_35FF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3652")

    ChrTalk(    #157
        0x8,
        (
            "照片上的脸…\x01",
            "很遗憾，我没有印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "帮不上忙，\x01",
            "实在不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_3652")


    ChrTalk(    #159
        0x8,
        (
            "是在找\x01",
            "照片上的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        "这可伤脑筋了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "别说是客人的脸了，\x01",
            "还是１０年前的身影……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "实在抱歉，\x01",
            "还是别强人所难了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_36DA")

    TalkEnd(0x8)
    Return()

    # Function_13_35FF end

    SaveToFile()

Try(main)
