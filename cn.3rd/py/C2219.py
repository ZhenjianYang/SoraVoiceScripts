from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2219   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2219.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2219   ._SN',
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
        '弗科特老人',                           # 9
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
        'ED6_DT07/CH01000 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
    )

    DeclNpc(
        X                   = -2870,
        Z                   = 0,
        Y                   = 202000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_D3",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_25A",          # 03, 3
        "Function_4_9A2",          # 04, 4
        "Function_5_A03",          # 05, 5
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Return()

    # Function_0_D2 end

    def Function_1_D3(): pass

    label("Function_1_D3")

    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x5)
    Return()

    # Function_1_D3 end

    def Function_2_DD(): pass

    label("Function_2_DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_244")

    label("loc_102")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_244")

    label("loc_11B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_244")

    label("loc_134")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_244")

    label("loc_14D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_244")

    label("loc_166")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_244")

    label("loc_17F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_244")

    label("loc_198")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_244")

    label("loc_1B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_244")

    label("loc_1CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_244")

    label("loc_1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_244")

    label("loc_1FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_244")

    label("loc_215")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_244")

    label("loc_22E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_259")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_244")

    label("loc_259")

    Return()

    # Function_2_DD end

    def Function_3_25A(): pass

    label("Function_3_25A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_5F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2A8")

    ChrTalk(    #0
        0xFE,
        (
            "在这里，\x01",
            "或许有我的幸福所在……\x02",
        )
    )

    Jump("loc_2A4")

    label("loc_2A4")

    CloseMessageWindow()
    Jump("loc_300")

    label("loc_2A8")


    ChrTalk(    #1
        0xFE,
        (
            "在这灯塔也有颗\x01",
            "闪烁发光的石头……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "或许它\x01",
            "正是我的幸福所在……\x02",
        )
    )

    Jump("loc_2FC")

    label("loc_2FC")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_300")

    Jump("loc_5F0")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 4)), scpexpr(EXPR_END)), "loc_3C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_33F")

    ChrTalk(    #3
        0xFE,
        (
            "不要哭丧着脸，\x01",
            "有什么困难就和我说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5")

    label("loc_33F")


    ChrTalk(    #4
        0xFE,
        (
            "什么呀，\x01",
            "不就是找个人嘛。\x02",
        )
    )

    Jump("loc_36B")

    label("loc_36B")

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "是谁？我也帮你去找。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x14E,
        (
            "#1714F不用了，没关系……\x02\x03",

            "#1713F谢谢，老爷爷……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3C5")

    Jump("loc_5F0")

    label("loc_3C8")

    EventBegin(0x1)
    OP_8C(0xFE, 270, 0)
    Fade(1000)
    OP_6D(-1600, 0, 202380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x14E, -1280, 0, 202300, 270)
    Sleep(1000)

    ChrTalk(    #7
        0xFE,
        (
            "真是的，\x01",
            "最近的年轻人啊……\x02",
        )
    )

    Jump("loc_457")

    label("loc_457")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 90, 500)
    Sleep(500)

    ChrTalk(    #8
        0xFE,
        "啊，原、原来是小孩子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14E,
        (
            "#1712F请、请问，老爷爷……\x02\x03",

            "有没有一个小女孩\x01",
            "来过这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "小女孩？\x01",
            "没有，我不记得看到过……\x02",
        )
    )

    Jump("loc_515")

    label("loc_515")

    CloseMessageWindow()

    ChrTalk(    #11
        0x14E,
        (
            "#1713F是、是吗……\x02\x03",

            "对不起，\x01",
            "打扰了……\x02",
        )
    )

    Jump("loc_552")

    label("loc_552")

    CloseMessageWindow()

    def lambda_559():

        label("loc_559")

        TurnDirection(0xFE, 0x14E, 0)
        OP_48()
        Jump("loc_559")

    QueueWorkItem2(0x10, 3, lambda_559)
    OP_43(0x14E, 0x3, 0x0, 0x4)
    Sleep(3000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #12
        0xFE,
        (
            "真是的，\x01",
            "最近的年轻人啊……\x02",
        )
    )

    Jump("loc_5B8")

    label("loc_5B8")

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "……总是匆匆忙忙的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F44)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x3)
    NewScene("ED6_DT21/C2219   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_5F0")

    Jump("loc_99E")

    label("loc_5F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_63B")

    ChrTalk(    #14
        0xFE,
        "幸福之石……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "会有那种东西\x01",
            "存在吗…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_994")

    label("loc_63B")

    EventBegin(0x1)
    OP_8C(0xFE, 270, 0)
    Fade(1000)
    OP_6D(-1600, 0, 202380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x14E, -1250, 0, 202480, 270)
    SetChrPos(0x14F, -1060, 0, 201620, 270)
    Sleep(1000)

    ChrTalk(    #16
        0xFE,
        (
            "真是的，\x01",
            "最近的年轻人啊……\x02",
        )
    )

    Jump("loc_6DB")

    label("loc_6DB")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 90, 500)
    Sleep(500)

    ChrTalk(    #17
        0xFE,
        "啊，原、原来是小孩子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14E,
        "#1718F老爷爷，您好。\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_63(0x14E)

    ChrTalk(    #19
        0x14E,
        (
            "#1714F啊，对了。\x01",
            "灯塔这么高……\x02\x03",

            "#1718F老爷爷，\x01",
            "您见过幸福之石吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "幸、幸福之石！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14F,
        "#1730F闪闪发光，十分漂亮的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "……………没、没有。\x01",
            "我活了这么多年，\x01",
            "都没有看到过那种东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1716F是吗……\x02\x03",

            "#1710F那真是谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    Sleep(400)

    ChrTalk(    #24
        0x14E,
        (
            "#1718F走吧，波利。\x01",
            "必须赶紧了！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x14E, 0x3, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #25
        0x14F,
        (
            "#1731F老爷爷，\x01",
            "请保重您的腰。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8DE():

        label("loc_8DE")

        TurnDirection(0xFE, 0x14F, 0)
        OP_48()
        Jump("loc_8DE")

    QueueWorkItem2(0x10, 3, lambda_8DE)
    OP_43(0x14F, 0x3, 0x0, 0x4)
    Sleep(3000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #26
        0xFE,
        (
            "真是的，\x01",
            "最近的年轻人啊……\x02",
        )
    )

    Jump("loc_93D")

    label("loc_93D")

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "……真是出奇地敏锐。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0xFE,
        "……幸福之石吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F43)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x3)
    NewScene("ED6_DT21/C2219   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_994")

    Jump("loc_99E")

    label("loc_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_99E")

    label("loc_99E")

    TalkEnd(0xFE)
    Return()

    # Function_3_25A end

    def Function_4_9A2(): pass

    label("Function_4_9A2")


    def lambda_9A8():
        OP_8E(0xFE, 0xB04, 0x0, 0x32104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A8)
    WaitChrThread(0xFE, 0x1)

    def lambda_9C8():
        OP_8E(0xFE, 0xB04, 0x0, 0x3283E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C8)
    WaitChrThread(0xFE, 0x1)

    def lambda_9E8():
        OP_8E(0xFE, 0xFFFFF254, 0xFFFFF830, 0x328F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E8)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_9A2 end

    def Function_5_A03(): pass

    label("Function_5_A03")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_5_A03 end

    SaveToFile()

Try(main)
