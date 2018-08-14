from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '里农',                                 # 9
        '斯蒂娜',                               # 10
        '目标用照相机',                         # 11
        '',                                     # 12
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT26/CH20789 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT26/CH20789P._CP',             # 02
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
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


    DeclActor(
        TriggerX            = 980,
        TriggerZ            = 0,
        TriggerY            = 118670,
        TriggerRange        = 1000,
        ActorX              = 980,
        ActorZ              = 1100,
        ActorY              = 118670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_146",          # 00, 0
        "Function_1_165",          # 01, 1
        "Function_2_16F",          # 02, 2
        "Function_3_185",          # 03, 3
        "Function_4_B1B",          # 04, 4
        "Function_5_B7A",          # 05, 5
        "Function_6_BF6",          # 06, 6
        "Function_7_C6A",          # 07, 7
    )


    def Function_0_146(): pass

    label("Function_0_146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_164")

    Return()

    # Function_0_146 end

    def Function_1_165(): pass

    label("Function_1_165")

    OP_B1("T0121_n")
    Return()

    # Function_1_165 end

    def Function_2_16F(): pass

    label("Function_2_16F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_184")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_16F")

    label("loc_184")

    Return()

    # Function_2_16F end

    def Function_3_185(): pass

    label("Function_3_185")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(5930, 0, 2009, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 3480, 0, -260, 0)
    SetChrPos(0x155, 5120, 0, -7500, 0)
    OP_9F(0x155, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20B():
        OP_6D(5930, 0, -2009, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_20B)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x155, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    ChrTalk(    #0
        0x155,
        "#291F#1P里农先生！\x02",
    )

    CloseMessageWindow()

    def lambda_261():
        OP_6D(4800, 0, 2000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_261)

    def lambda_279():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_279)

    def lambda_289():
        OP_6B(2900, 2500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_289)
    OP_62(0x155, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_2B0():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2B0)

    def lambda_2CB():

        label("loc_2CB")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_2CB")

    QueueWorkItem2(0x10, 2, lambda_2CB)

    def lambda_2DC():

        label("loc_2DC")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_2DC")

    QueueWorkItem2(0x11, 2, lambda_2DC)
    WaitChrThread(0x155, 0x1)

    def lambda_2F2():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2F2)
    WaitChrThread(0x155, 0x1)

    def lambda_312():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_312)
    WaitChrThread(0x155, 0x1)

    def lambda_332():
        OP_8E(0xFE, 0x12C0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_332)
    WaitChrThread(0x155, 0x1)

    ChrTalk(    #1
        0x10,
        (
            "#6P呀，艾丝蒂尔。\x01",
            "又来看运动鞋吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x155,
        (
            "#290F#11P嗯嗯……！\x01",
            "有新品进货吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#6P真可惜，没有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#6P嗯，\x01",
            "下次进货大概是１６日吧……\x02",
        )
    )

    Jump("loc_3FC")

    label("loc_3FC")

    CloseMessageWindow()

    ChrTalk(    #5
        0x155,
        (
            "#296F#11P…………１６日！？\x01",
            "还要等一星期啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 90, 500)
    Sleep(300)

    ChrTalk(    #6
        0x155,
        (
            "#292F#5P还要一星期，还要一星期……\x01",
            "………………（唠唠叨叨）。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x11,
        "#6P艾丝蒂尔～？\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x155, 0x11, 500)

    ChrTalk(    #8
        0x155,
        "#293F#5P啊，斯蒂娜阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "#6P呼呼，\x01",
            "终于被我逮到了吧～！\x02",
        )
    )

    Jump("loc_558")

    label("loc_558")

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#6P我刚刚看到了一件\x01",
            "很适合艾丝蒂尔的衣服哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#6P今天一定要让你\x01",
            "穿上像个女孩样的洋装！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x155,
        (
            "#292F#5P咦，不、不行！\x02\x03",

            "#295F我正要去抓虫子呢。\x01",
            "会弄脏的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x155,
        (
            "#293F#5P啊…………！？\x01",
            "对了，我还要去抓虫呢！\x02\x03",

            "#296F好险好险，\x01",
            "差点给忘了……\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x155,
        (
            "#290F#5P嗯，\x01",
            "首先要去收集材料！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "先去找伊莉莎\x01",        # 0
            "立刻赶往缇欧家\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(    #15
        0x155,
        (
            "#291F#5P好，先去找伊莉莎！\x02\x03",

            "冲啊冲啊～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AC():
        OP_6D(5930, 0, -2009, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7AC)

    def lambda_7C4():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7C4)

    def lambda_7D4():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7D4)
    OP_62(0x155, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7F6():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_7F6)
    WaitChrThread(0x155, 0x1)

    def lambda_816():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_816)
    WaitChrThread(0x155, 0x1)

    def lambda_836():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_836)
    WaitChrThread(0x155, 0x1)

    def lambda_856():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFE2B4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_856)
    Sleep(500)

    def lambda_876():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_876)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #16
        0x10,
        (
            "最近她比以前\x01",
            "更有精神了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#6P是不是发生了\x01",
            "什么好事呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91A():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_91A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_B1A")

    label("loc_93E")


    ChrTalk(    #18
        0x155,
        (
            "#292F#5P好，这就冲去农场！\x02\x03",

            "#291F要赶快才行了～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_98B():
        OP_6D(5930, 0, -2009, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_98B)

    def lambda_9A3():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9A3)

    def lambda_9B3():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9B3)
    OP_62(0x155, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9D5():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_9D5)
    WaitChrThread(0x155, 0x1)

    def lambda_9F5():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_9F5)
    WaitChrThread(0x155, 0x1)

    def lambda_A15():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_A15)
    WaitChrThread(0x155, 0x1)

    def lambda_A35():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFE2B4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_A35)
    Sleep(500)

    def lambda_A55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_A55)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #19
        0x10,
        (
            "最近她比以前\x01",
            "更有精神了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#6P是不是发生了\x01",
            "什么好事呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF9():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_AF9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_B1A")

    Return()

    # Function_3_185 end

    def Function_4_B1B(): pass

    label("Function_4_B1B")

    OP_82(0x81, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\x62\x03\x07\x00。\x02",
    )

    Jump("loc_B54")

    label("loc_B54")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x10, 0x1)
    OP_3E(0x362, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_B1B end

    def Function_5_B7A(): pass

    label("Function_5_B7A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_BA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA1)

    def lambda_BB3():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB3)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x456, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3F2, 0x0, 0x1BD28, 0x7D0, 0x0)
    Return()

    # Function_5_B7A end

    def Function_6_BF6(): pass

    label("Function_6_BF6")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_C22():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C22)

    def lambda_C34():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C34)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x316, 0x0, 0x1B79C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_BF6 end

    def Function_7_C6A(): pass

    label("Function_7_C6A")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_C96():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C96)

    def lambda_CA8():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA8)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x8E8, 0x0, 0x1B652, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_C6A end

    SaveToFile()

Try(main)
