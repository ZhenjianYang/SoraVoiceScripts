from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1410   ._SN',
        MapName             = 'Bose',
        Location            = 'C1410.x',
        MapIndex            = 62,
        MapDefaultBGM       = "ed60015",
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
        '维姆拉',                               # 9
        '阿加特',                               # 10
        '目标用照相机',                         # 11
        '',                                     # 12
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = 33900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_150",          # 02, 2
        "Function_3_166",          # 03, 3
        "Function_4_B78",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126")

    label("loc_126")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_14E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_14E")

    Return()

    # Function_0_11A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Return()

    # Function_1_14F end

    def Function_2_150(): pass

    label("Function_2_150")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_165")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_150")

    label("loc_165")

    Return()

    # Function_2_150 end

    def Function_3_166(): pass

    label("Function_3_166")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(3000, 1500, 39360, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 2800, 0, 38100, 270)
    SetChrPos(0x10, 3140, 0, 36980, 270)
    SetChrPos(0x112, 540, 0, 37040, 90)
    SetChrPos(0x111, 440, 0, 37840, 90)
    SetChrPos(0x113, 340, 0, 38640, 90)

    def lambda_219():
        OP_6D(3000, 0, 39360, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_219)

    def lambda_231():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_231)
    FadeToBright(2000, 0)
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x111,
        (
            "#1749F#6P说是要离开卢安，\x01",
            "本来我还有点期待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x113,
        (
            "#1765F#6P哼，\x01",
            "没想到竟然被带到这种\x01",
            "满是雾气的山谷里的小屋来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x112,
        (
            "#1755F#6P仔细想想，\x01",
            "我们好像还是第一次离开卢安吧？\x02\x03",

            "#1754F结果竟然一上来\x01",
            "就来到这么隐秘的地方呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x111,
        (
            "#1744F#6P唉，不管怎么说\x01",
            "这只是为了考试。\x02\x03",

            "#1740F心存期待\x01",
            "反而不合情理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x112,
        "#1751F#6P哦，迪恩还挺老练的嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_3DF():
        OP_6D(3500, 0, 39360, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3DF)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    WaitChrThread(0x12, 0x0)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #5
        0x11,
        (
            "#051F#11P哼，\x01",
            "这不是明白得很吗。\x02\x03",

            "#053F看你们这么多嘴，\x01",
            "本来还打算呵斥一下来着……\x02\x03",

            "#050F总之，\x01",
            "聊天就到此为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x111,
        "#1742F#6P是、是……大哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x113,
        "#1763F#6P啧，自以为是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#053F#11P好了，\x01",
            "接下来终于要进行\x01",
            "事关游击士资格的最终考试了。\x02\x03",

            "通过这个考试\x01",
            "你们就能成为准游击士……\x02\x03",

            "#051F在这之前……\x02\x03",

            "你们直到今天都没掉队，\x01",
            "就暂且先表扬一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x111,
        "#1743F#6P表、表扬……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x112,
        (
            "#1753F#6P这、这是\x01",
            "吹的什么风啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1764F#6P哼，真恶心啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x11,
        (
            "#555F#11P……我说你们，\x01",
            "到底当我是什么人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x113,
        (
            "#1761F总之，\x01",
            "赶快说明考试内容吧。\x02\x03",

            "我们想早点活动一下身体，\x01",
            "都等得不耐烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#051F#11P哼，说话还是\x01",
            "那么没大没小。\x02\x03",

            "#053F算了，\x01",
            "那我这就开始说明吧。\x02\x03",

            "#050F考试内容简单明了——\x01",
            "就是通过有魔兽徘徊的洞窟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1743F#6P洞、洞窟？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        "#1753F#6P还要赶路吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#051F#11P别担心。\x01",
            "地方离这里不远。\x02\x03",

            "#053F总之，\x01",
            "你们要进入那个洞窟，\x01",
            "并且走到最深处。\x02\x03",

            "虽然没有什么时间限制，\x01",
            "不过我会在最里面等着，\x01",
            "你们还是尽快赶来吧。\x02\x03",

            "#050F——说明完毕。\x01",
            "有什么问题尽管提吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x111,
        (
            "#1744F#6P穿过洞窟啊……\x02\x03",

            "#1741F关键在于一边打退魔兽\x01",
            "一边前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x112,
        (
            "#1756F#6P这么简单，\x01",
            "而且感觉正适合我们，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x113,
        "#1761F#6P嘿嘿，应该不会无聊了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        "#551F#11P……看来没问题了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        (
            "#051F#5P那么，维姆拉大叔。\x02\x03",

            "后方支援就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)
    Sleep(300)

    ChrTalk(    #23
        0x10,
        "#12P这倒好说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#12P让他们去真的没问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#053F#5P交给我吧，大叔。\x02\x03",

            "#051F那么，\x01",
            "就赶快去考试现场吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC7():
        OP_8E(0xFE, 0x8C, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AC7)
    Sleep(300)

    def lambda_AE7():

        label("loc_AE7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_AE7")

    QueueWorkItem2(0x111, 2, lambda_AE7)

    def lambda_AF8():

        label("loc_AF8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_AF8")

    QueueWorkItem2(0x112, 2, lambda_AF8)

    def lambda_B09():

        label("loc_B09")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B09")

    QueueWorkItem2(0x113, 2, lambda_B09)

    def lambda_B1A():
        OP_8F(0xFE, 0x0, 0x0, 0x9092, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_B1A)
    Sleep(600)
    FadeToDark(2000, 0, -1)
    OP_43(0x10, 0x3, 0x0, 0x4)
    WaitChrThread(0x11, 0x1)

    def lambda_B50():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B50)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_166 end

    def Function_4_B78(): pass

    label("Function_4_B78")


    def lambda_B7E():
        OP_8E(0xFE, 0x53C, 0x0, 0x9074, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B7E)
    WaitChrThread(0x10, 0x1)

    def lambda_B9E():
        OP_8E(0xFE, 0x8C, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B9E)
    WaitChrThread(0x10, 0x1)

    def lambda_BBE():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BBE)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_4_B78 end

    SaveToFile()

Try(main)
