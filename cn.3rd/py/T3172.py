from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3172   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3172.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '拉赛尔博士',                           # 9
        '艾莉卡',                               # 10
        '丹',                                   # 11
        '提妲',                                 # 12
        '物体',                                 # 13
        '咖啡',                                 # 14
        '咖啡',                                 # 15
        '咖啡',                                 # 16
        '导力装甲',                             # 17
        '目标用摄像机',                         # 18
        '',                                     # 19
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT27/CH03970 ._CH',             # 01
        'ED6_DT27/CH03980 ._CH',             # 02
        'ED6_DT07/CH00065 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
        'ED6_DT07/CH00061 ._CH',             # 05
        'ED6_DT26/CH20230 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT07/CH02023 ._CH',             # 08
        'ED6_DT26/CH20696 ._CH',             # 09
        'ED6_DT26/CH20697 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT26/CH20205 ._CH',             # 0C
        'ED6_DT26/CH20757 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT27/CH03970P._CP',             # 01
        'ED6_DT27/CH03980P._CP',             # 02
        'ED6_DT07/CH00065P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
        'ED6_DT07/CH00061P._CP',             # 05
        'ED6_DT26/CH20230P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT07/CH02023P._CP',             # 08
        'ED6_DT26/CH20696P._CP',             # 09
        'ED6_DT26/CH20697P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT26/CH20205P._CP',             # 0C
        'ED6_DT26/CH20757P._CP',             # 0D
    )

    DeclNpc(
        X                   = 29950,
        Z                   = -1000,
        Y                   = 8580,
        Direction           = 270,
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
        X                   = 34440,
        Z                   = -1000,
        Y                   = 8630,
        Direction           = 0,
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
        X                   = 1740,
        Z                   = 0,
        Y                   = 4730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34310,
        Z                   = -270,
        Y                   = 10390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179652,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1E6,
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
        "Function_0_25A",          # 00, 0
        "Function_1_2AE",          # 01, 1
        "Function_2_2DB",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_C41",          # 04, 4
        "Function_5_25A6",         # 05, 5
        "Function_6_25E7",         # 06, 6
        "Function_7_26F7",         # 07, 7
        "Function_8_2758",         # 08, 8
        "Function_9_2796",         # 09, 9
        "Function_10_27FE",        # 0A, 10
        "Function_11_28B8",        # 0B, 11
        "Function_12_28E4",        # 0C, 12
        "Function_13_2915",        # 0D, 13
        "Function_14_2946",        # 0E, 14
        "Function_15_3496",        # 0F, 15
        "Function_16_34F8",        # 10, 16
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266")

    label("loc_266")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_28E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_28E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2AD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2AD")

    Return()

    # Function_0_25A end

    def Function_1_2AE(): pass

    label("Function_1_2AE")

    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x5, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D7")
    OP_22(0xC9, 0x0, 0x64)
    Jump("loc_2DA")

    label("loc_2D7")

    OP_23(0xC9)

    label("loc_2DA")

    Return()

    # Function_1_2AE end

    def Function_2_2DB(): pass

    label("Function_2_2DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2DB")

    label("loc_2F0")

    Return()

    # Function_2_2DB end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(32780, -1000, 9320, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 30000, -1000, 8300, 270)
    SetChrPos(0x11, 30000, -1000, 9340, 270)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 33900, -1000, 7900, 225)
    SetChrPos(0x10, 32200, -1000, 8140, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x800)
    SetChrPos(0x18, 32940, -1500, 6120, 0)
    SetChrPos(0x106, 30500, -1000, -1500, 0)
    SoundLoad(521)
    SoundLoad(384)
    SoundLoad(383)
    SoundLoad(501)
    SoundLoad(554)
    SoundLoad(130)

    def lambda_3DB():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3DB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x13,
        (
            "#063F#11P呜呜，是吗……\x02\x03",

            "在最终检查的时候\x01",
            "我本来应该\x01",
            "注意到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        (
            "#1457F#5P…………提妲，\x01",
            "还不确定\x01",
            "这就是原因呢。\x02\x03",

            "#1452F不要妄下判断。\x02\x03",

            "要反省和背负责任，\x01",
            "都要等确定了原因再说。\x02",
        )
    )

    Jump("loc_4DF")

    label("loc_4DF")

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "#063F#11P嗯、嗯……\x02\x03",

            "但我还是…………\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x22A, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #3
        0x106,
        "青年的声音",
        "#1S#1P呜哇……！？#2S\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x106,
        "青年的声音",
        (
            "#1S#1P这、这锤子是什么啊……？#2S\x02\x03",

            "#1S……真、真危险…………#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x13, 180, 500)
    Sleep(300)

    ChrTalk(    #5
        0x13,
        (
            "#064F#5P咦，\x01",
            "刚才是不是阿加特大哥哥的声音？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 500)
    Sleep(300)

    ChrTalk(    #6
        0x11,
        "#1451F#5P谁知道～是错觉吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#064F#5P嗯，但是……\x02\x03",

            "#067F差不多到约定的时间了。\x02\x03",

            "……我得去\x01",
            "热一下饭菜才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)
    OP_8E(0x13, 0x7620, 0xFFFFFC18, 0x15F4, 0x1194, 0x0)

    def lambda_6EC():
        OP_8E(0xFE, 0x7530, 0xFFFFFC18, 0xE74, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6EC)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x13, 0x1)

    def lambda_723():
        OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_723)
    WaitChrThread(0x13, 0x1)

    def lambda_743():
        OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0x26C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_743)
    WaitChrThread(0x13, 0x1)

    def lambda_763():
        OP_8E(0xFE, 0x5910, 0xFFFFFC18, 0x26C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_763)
    WaitChrThread(0x13, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #8
        0x106,
        "青年的声音",
        "#1S#1P呜哦……！？#2S\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x106,
        "青年的声音",
        "#1S#1P为、为什么街上会有枪射过来……！？#2S\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 270, 400)
    Sleep(100)
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #10
        0x10,
        (
            "#104F#11P哎呀，艾莉卡……\x02\x03",

            "#100F我觉得枪\x01",
            "是不是有些过头了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#1465F#11P是、是啊。\x01",
            "至少陷阱什么的还可以……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x17F, 0x0, 0x64)
    Sleep(3600)

    NpcTalk(    #12
        0x106,
        "青年的声音",
        "#1S#1P呜哇…………！？#2S\x02",
    )

    CloseMessageWindow()
    OP_22(0x209, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x180, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        (
            "#1461F#11P…………唔，\x01",
            "阿加特要多久之后\x01",
            "才能到达呢？\x02\x03",

            "我还想跟他\x01",
            "推心置腹地\x01",
            "好好聊聊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#1458F#5P呼呼呼……\x01",
            "那只有女神才知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)
    OP_8E(0x11, 0x780A, 0xFFFFFC18, 0x2828, 0x4B0, 0x0)
    Sleep(300)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #15
        0x11,
        (
            "#1456F#5P哼哼，\x01",
            "看来还挺有一手的。\x02\x03",

            "#1458F……但是。\x01",
            "但是啊，阿加特·科洛斯纳。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 500)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1835F#5P#3S『实验』才刚刚开始呢！#2S\x02",
    )

    Fade(500)
    OP_7C(0x0, 0x12C, 0xBB8, 0x190)
    OP_6D(32670, -1000, 10430, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2600, 0)
    CloseMessageWindow()
    OP_0D()
    Sleep(300)

    def lambda_B4C():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_B4C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00Episode『导力装甲开发计划/后篇』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C31")
    Sleep(1000)
    OP_28(0x2, 0x4, 0x10)
    OP_28(0x2, 0x4, 0x20)
    OP_35(0x6, 0xD4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05提妲学会了战技\x01",
            "\x07\x02『导力装甲』\x07\x05。\x02",
        )
    )

    Jump("loc_C25")

    label("loc_C25")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_C31")

    OP_C2(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2F1 end

    def Function_4_C41(): pass

    label("Function_4_C41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1840, 0, 5480, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -170, 0, 4680, 0)
    SetChrPos(0x107, 1750, 0, 4350, 90)
    SetChrPos(0x10, 4500, 0, 2800, 0)
    SetChrChipByIndex(0x107, 12)
    SetChrSubChip(0x107, 0)

    def lambda_CD7():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_CD7)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    TurnDirection(0x12, 0x107, 400)
    Sleep(300)

    ChrTalk(    #19
        0x12,
        (
            "#1460F#6P提妲，可以了。\x02\x03",

            "之后的我来做，\x01",
            "今天你就休息吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12, 500)
    Sleep(300)

    ChrTalk(    #20
        0x107,
        (
            "#1261F#11P不用，\x01",
            "这点小事我经常做啦。\x02\x03",

            "#1260F爸爸才该\x01",
            "早点去休息啊。\x02\x03",

            "其实你偷偷把工作\x01",
            "都急急忙忙解决了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#1463F#6P嗯、嗯……\x02\x03",

            "#1465F哈哈，\x01",
            "提妲说话也越来越尖锐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#1267F#11P我也快１３岁了哦。\x01",
            "不是小孩子了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #23
        0x10,
        "#1P这、这是……！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_EA7():
        OP_6D(5840, 0, 5480, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_EA7)

    def lambda_EBF():
        OP_8C(0x107, 90, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_EBF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x19, 0xFF)
    WaitChrThread(0x19, 0x0)
    Sleep(800)
    OP_6D(27640, -1000, 10200, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10, 30350, -1000, 9550, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 30290, -1000, 8380, 270)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_72(0x5, 0x0)
    ExitThread()

    def lambda_F56():
        OP_6D(31640, -1000, 10200, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_F56)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    Sleep(500)

    ChrTalk(    #24
        0x10,
        (
            "#104F#5P艾莉卡啊，\x01",
            "你当真要做这种东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1457F#11P……我就是为了这个才回来的。\x02\x03",

            "#1452F能够制造这种东西的，\x01",
            "非利贝尔中央工房莫属。\x02\x03",

            "至少我是这么认为的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#102F#5P唔、唔……\x01",
            "不过啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x107, 23120, 0, 1760, 0)

    ChrTalk(    #27
        0x107,
        (
            "#1264F#5P……妈妈？\x01",
            "爷爷？\x02",
        )
    )

    Jump("loc_10B5")

    label("loc_10B5")

    CloseMessageWindow()
    OP_59()
    OP_22(0x7, 0x0, 0x64)
    ClearChrFlags(0x107, 0x8)
    SetChrPos(0x107, 22340, 0, 860, 90)

    def lambda_10D8():
        OP_6D(29640, -1000, 8160, 2500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_10D8)

    def lambda_10F0():

        label("loc_10F0")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_10F0")

    QueueWorkItem2(0x11, 2, lambda_10F0)

    def lambda_1101():
        OP_8E(0xFE, 0x62FC, 0x0, 0xF14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1101)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #28
        0x11,
        (
            "#1454F#11P哎呀，提妲。\x01",
            "你还没睡吗？\x02\x03",

            "都过十二点了，\x01",
            "赶快去睡吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        (
            "#1264F#6P嗯，这个是设计图……？\x02\x03",

            "#1261F什么什么，也给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11CD():
        OP_6D(31640, -1000, 6400, 3800)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_11CD)

    def lambda_11E5():
        OP_6C(32000, 3800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_11E5)

    def lambda_11F5():
        OP_8E(0xFE, 0x62FC, 0x0, 0x49C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11F5)
    WaitChrThread(0x107, 0x1)

    def lambda_1215():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x49C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1215)
    Sleep(500)
    OP_44(0x11, 0x2)
    OP_43(0x11, 0x3, 0x0, 0x5)

    def lambda_1240():

        label("loc_1240")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_1240")

    QueueWorkItem2(0x10, 2, lambda_1240)
    WaitChrThread(0x107, 0x1)

    def lambda_1256():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1256)
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #30
        0x11,
        (
            "#1452F#5P你啊，\x01",
            "刚洗完澡，小心感冒哦。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #31
        0x107,
        (
            "#1263F#12P哎哎～\x01",
            "我也要看我也要看！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x107, 0x3, 0x0, 0x6)

    ChrTalk(    #32
        0x107,
        (
            "#1260F#12P好像很复杂的样子……\x02\x03",

            "右端的那个，\x01",
            "是导力引擎吧。\x02\x03",

            "#1261F这么小巧精致的设计……\x02\x03",

            "啊，是新的飞艇吗？\x01",
            "还是…………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x3)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #33
        0x107,
        (
            "#1265F#12P妈妈，\x01",
            "我也要看啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#1833F#5P啊啊真是的，这孩子。\x02\x03",

            "还是老样子，\x01",
            "一看到机械就眼睛发亮啊～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        (
            "#1262F#12P……妈妈！？\x01",
            "别想蒙混过关！！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1466():
        OP_6D(30640, -1000, 6400, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1466)
    SetChrPos(0x12, 22500, 0, 560, 90)

    def lambda_148F():
        OP_8E(0xFE, 0x6590, 0x0, 0x424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_148F)
    Sleep(500)

    def lambda_14AF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_14AF)
    Sleep(200)
    OP_22(0x7, 0x0, 0x64)

    def lambda_14C7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_14C7)
    Sleep(200)

    def lambda_14DA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_14DA)
    WaitChrThread(0x12, 0x1)
    Sleep(500)

    ChrTalk(    #36
        0x12,
        (
            "#1460F#6P这边已经收拾好了。\x02\x03",

            "差不多该开始了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#1451F#11P哎呀，丹，\x01",
            "你来得正好。\x02\x03",

            "这孩子就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        (
            "#1465F#6P嗯嗯，是啊。\x01",
            "都这么晚了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #39
        0x107,
        "#1265F#3S#11P咦咦～！？\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()

    def lambda_15E9():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x424, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_15E9)
    Sleep(500)

    def lambda_1609():

        label("loc_1609")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1609")

    QueueWorkItem2(0x107, 2, lambda_1609)

    def lambda_161A():

        label("loc_161A")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_161A")

    QueueWorkItem2(0x11, 2, lambda_161A)

    def lambda_162B():

        label("loc_162B")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_162B")

    QueueWorkItem2(0x10, 2, lambda_162B)
    WaitChrThread(0x12, 0x1)

    def lambda_1641():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0xA28, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1641)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #40
        0x12,
        "#1460F#12P来，提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x107,
        (
            "#1262F#5P就、就让我\x01",
            "看一下下啦！\x02\x03",

            "变频器的转矩那么小，\x01",
            "真是令人在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        (
            "#1465F#12P（嗯，\x01",
            "  一阵子不见就大有长进啊……）\x02\x03",

            "#1461F好啦好啦提妲，睡觉啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#1265F#5P但、但是……\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_44(0x11, 0x2)
    OP_44(0x10, 0x2)

    def lambda_176E():

        label("loc_176E")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_176E")

    QueueWorkItem2(0x11, 2, lambda_176E)

    def lambda_177F():

        label("loc_177F")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_177F")

    QueueWorkItem2(0x10, 2, lambda_177F)

    def lambda_1790():

        label("loc_1790")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_1790")

    QueueWorkItem2(0x12, 2, lambda_1790)

    def lambda_17A1():
        OP_8F(0xFE, 0x7C74, 0xFFFFFC18, 0xE74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17A1)
    WaitChrThread(0x12, 0x1)
    OP_43(0x12, 0x3, 0x0, 0x7)

    def lambda_17C8():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_17C8)
    WaitChrThread(0x107, 0x1)

    def lambda_17E8():
        OP_8E(0xFE, 0x5CBC, 0x0, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_17E8)
    Sleep(2000)
    OP_43(0x11, 0x3, 0x0, 0x8)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x12, 0x3)
    OP_44(0x12, 0x2)
    Sleep(500)
    OP_43(0x12, 0x3, 0x0, 0x9)
    Sleep(2000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x107)
    Sleep(500)
    OP_8C(0x107, 45, 500)

    def lambda_1854():
        OP_6D(31400, -1000, 9740, 2500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1854)

    def lambda_186C():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_186C)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #44
        0x11,
        (
            "#1452F#11P首先是\x01",
            "这个单元的制作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#104F#5P唔，好像很麻烦呢。\x02\x03",

            "#102F似乎有必要\x01",
            "先在卡佩尔上\x01",
            "做一下模拟实验……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#1462F#12P然后是框架，\x01",
            "以前的材料支持不住。\x02\x03",

            "是不是应该试试新素材……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(24920, 0, 2100, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_43(0x11, 0x3, 0x0, 0xB)
    OP_43(0x10, 0x3, 0x0, 0xC)
    OP_43(0x12, 0x3, 0x0, 0xD)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #47
        0x107,
        (
            "#1260F（在、在说什么呢。\x01",
            "  心砰砰跳…………）\x02\x03",

            "（再稍微\x01",
            "  靠近一点吧……）\x02",
        )
    )

    Jump("loc_1A4D")

    label("loc_1A4D")

    CloseMessageWindow()

    def lambda_1A54():
        OP_6D(26820, 0, 3800, 2400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1A54)

    def lambda_1A6C():
        OP_8E(0xFE, 0x6360, 0x0, 0xA3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1A6C)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    def lambda_1AB0():
        OP_6D(27220, 0, 5440, 1300)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1AB0)

    def lambda_1AC8():
        OP_8F(0xFE, 0x6360, 0x0, 0xF14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1AC8)
    WaitChrThread(0x107, 0x1)
    OP_44(0x12, 0x3)
    OP_63(0x12)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x12, 225, 500)
    Sleep(300)

    ChrTalk(    #48
        0x12,
        "#1463F#11P提妲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#1271F呜，被发现了……\x02",
    )

    CloseMessageWindow()

    def lambda_1B57():

        label("loc_1B57")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1B57")

    QueueWorkItem2(0x107, 2, lambda_1B57)

    def lambda_1B68():
        OP_8E(0xFE, 0x79E0, 0xFFFFFC18, 0x1874, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B68)
    WaitChrThread(0x12, 0x1)

    def lambda_1B88():
        OP_8E(0xFE, 0x79E0, 0xFFFFFC18, 0x4EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B88)
    WaitChrThread(0x12, 0x1)

    def lambda_1BA8():
        OP_8E(0xFE, 0x639C, 0x0, 0x4EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BA8)
    WaitChrThread(0x12, 0x1)

    def lambda_1BC8():
        OP_8E(0xFE, 0x639C, 0x0, 0xA3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BC8)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #50
        0x12,
        "#1465F#12P好啦，快去睡啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x107,
        "#1263F#5P哎～但是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "#1460F#12P详细的情况，\x01",
            "明天再告诉你吧。\x02\x03",

            "……好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        "#1272F#5P呜呜～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #54
        0x107,
        (
            "#1262F#5P……一定哦。\x02\x03",

            "爸爸，一定要告诉我哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12,
        "#1461F#12P好好，一定的。\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 225, 400)

    def lambda_1D31():
        OP_8E(0xFE, 0x5820, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D31)
    Sleep(500)
    OP_8C(0x12, 225, 400)

    def lambda_1D58():
        OP_8E(0xFE, 0x5820, 0x0, 0xFFFFFEE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D58)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-1900, 0, 33040, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6F(0x7, 20)
    OP_44(0x107, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrFlags(0x107, 0x2)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x107, 0x40)
    SetChrPos(0x107, -2180, 200, 31320, 0)
    SetChrChipByIndex(0x107, 6)
    SetChrSubChip(0x107, 10)
    SetChrPos(0x12, -4059, 0, 31660, 90)
    SetChrSubChip(0x12, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #56
        0x107,
        (
            "#1252F#11P说好了哦，爸爸。\x01",
            "…………一定哦！\x02\x03",

            "不能趁我不知道的时候\x01",
            "就偷偷做好了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "#1460F#6P嗯，知道啦。\x02\x03",

            "我向空之女神发誓\x01",
            "一定遵守诺言。\x02\x03",

            "#1461F晚安，提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#1250F#11P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0x13, 0x320)
    Sleep(1000)

    ChrTalk(    #59
        0x107,
        "#1253F#100W#11P晚……安……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #60
        0x107,
        "#1253F#100W#11P……呼～呼～…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x12, 0x4)

    def lambda_1F7A():
        OP_8E(0xFE, 0xFFFFF1F0, 0x0, 0x7BAC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F7A)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_22(0x186, 0x0, 0x64)
    OP_70(0x7, 0xC)
    OP_73(0x7)
    Sleep(300)

    def lambda_1FB3():
        OP_8F(0xFE, 0xFFFFF025, 0x0, 0x7BAC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FB3)
    WaitChrThread(0x12, 0x1)
    ClearChrFlags(0x12, 0x4)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #61
        0x12,
        (
            "#1465F#6P（……有时候\x01",
            "  提妲说话真像艾莉卡呢。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x107, 0x2)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x107, 0x40)
    SetChrPos(0x107, -6160, 0, 5160, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(420, 0, 2360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x15, -1660, 800, 1400, 0)
    SetChrPos(0x16, -900, 800, 1400, 0)
    SetChrPos(0x17, -900, 800, 150, 0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x10, -2300, 200, 1800, 90)
    SetChrPos(0x11, 340, 200, 1610, 270)
    OP_44(0x10, 0x3)
    OP_63(0x10)
    OP_44(0x11, 0x3)
    OP_63(0x11)
    SetChrPos(0x12, -2870, 4000, 4750, 270)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x12, 0x3, 0x0, 0xA)
    Sleep(1000)
    OP_63(0x10)
    Sleep(100)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #62
        0x10,
        "#104F#6P………………就是这样了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#1453F#11P『噬身之蛇』吗……\x02\x03",

            "看来他们果然拥有\x01",
            "超乎想象的技术实力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#100F#6P…………是啊。\x02\x03",

            "说实话，\x01",
            "他们的技术实力远远超越我们。\x02\x03",

            "#104F人形兵器、『福音』、\x01",
            "然后是『古罗力亚斯』…………\x02\x03",

            "不过我对他们的技术\x01",
            "也不是完全没头绪……\x02",
        )
    )

    Jump("loc_22F1")

    label("loc_22F1")

    CloseMessageWindow()
    WaitChrThread(0x12, 0x3)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 310, 200, 450, 270)
    Sleep(1000)

    ChrTalk(    #65
        0x10,
        (
            "#100F#6P对了，你怎么搞的。\x01",
            "突然提起这个……\x02\x03",

            "他们的资料\x01",
            "我不是都发给你了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12,
        (
            "#1464F#2P其实……\x02\x03",

            "#1462F我们也知道的，\x01",
            "『噬身之蛇』……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)

    ChrTalk(    #67
        0x10,
        "#103F#6P你、你说什么！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #68
        0x12,
        (
            "#1462F#2P虽然并没有\x01",
            "直接遭遇他们。\x02\x03",

            "不过，他们通过猎兵团\x01",
            "或特定资本家等渠道\x01",
            "正在稳步扩张势力……\x02\x03",

            "#1464F这几年巡回大陆诸国边境时，\x01",
            "对此深有感受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "#1453F#11P……所以我们才回来的。\x02\x03",

            "但是没有想到\x01",
            "他们竟会来到利贝尔，\x01",
            "让对方抢占了先机……\x02\x03",

            "#1452F所以我们更要分秒必争\x01",
            "完成这个才行。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2579():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2579)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C41 end

    def Function_5_25A6(): pass

    label("Function_5_25A6")


    def lambda_25AC():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x1E50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_25AC)
    WaitChrThread(0x11, 0x1)

    def lambda_25CC():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_25CC)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_5_25A6 end

    def Function_6_25E7(): pass

    label("Function_6_25E7")


    def lambda_25ED():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_25ED)
    Sleep(300)

    def lambda_260D():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_260D)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_2632():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2632)
    Sleep(300)

    def lambda_2652():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2652)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_2677():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2677)
    Sleep(300)

    def lambda_2697():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2697)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_26BC():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_26BC)
    Sleep(300)

    def lambda_26DC():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_26DC)
    WaitChrThread(0x107, 0x1)
    Return()

    # Function_6_25E7 end

    def Function_7_26F7(): pass

    label("Function_7_26F7")


    def lambda_26FD():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_26FD)
    WaitChrThread(0x12, 0x1)

    def lambda_271D():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_271D)
    WaitChrThread(0x12, 0x1)

    def lambda_273D():
        OP_8F(0xFE, 0x6040, 0x0, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_273D)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_7_26F7 end

    def Function_8_2758(): pass

    label("Function_8_2758")

    OP_44(0x11, 0x2)
    OP_44(0x10, 0x2)
    OP_8C(0x11, 0, 500)

    def lambda_276D():
        OP_8E(0xFE, 0x7652, 0xFFFFFC18, 0x20BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_276D)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 270, 500)
    OP_8C(0x10, 225, 500)
    Return()

    # Function_8_2758 end

    def Function_9_2796(): pass

    label("Function_9_2796")

    OP_8C(0x12, 90, 500)

    def lambda_27A3():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27A3)
    WaitChrThread(0x12, 0x1)

    def lambda_27C3():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x1A2C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27C3)
    WaitChrThread(0x12, 0x1)

    def lambda_27E3():
        OP_8E(0xFE, 0x75F8, 0xFFFFFC18, 0x1C98, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27E3)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_9_2796 end

    def Function_10_27FE(): pass

    label("Function_10_27FE")


    def lambda_2804():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2804)

    def lambda_2816():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x128E, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2816)
    WaitChrThread(0x12, 0x1)

    def lambda_2836():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x2D0, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2836)
    WaitChrThread(0x12, 0x1)

    def lambda_2856():
        OP_8E(0xFE, 0xFFFFED4A, 0x0, 0xFFFFFD44, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2856)
    WaitChrThread(0x12, 0x1)

    def lambda_2876():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFFD44, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2876)
    WaitChrThread(0x12, 0x1)

    def lambda_2896():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFFF38, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2896)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Return()

    # Function_10_27FE end

    def Function_11_28B8(): pass

    label("Function_11_28B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E3")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("Function_11_28B8")

    label("loc_28E3")

    Return()

    # Function_11_28B8 end

    def Function_12_28E4(): pass

    label("Function_12_28E4")

    Sleep(1000)

    label("loc_28E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2914")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("loc_28E9")

    label("loc_2914")

    Return()

    # Function_12_28E4 end

    def Function_13_2915(): pass

    label("Function_13_2915")

    Sleep(2000)

    label("loc_291A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2945")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("loc_291A")

    label("loc_2945")

    Return()

    # Function_13_2915 end

    def Function_14_2946(): pass

    label("Function_14_2946")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3170, 500, 36110, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(289, 0)
    SetChrPos(0x107, 1840, 500, 35070, 90)
    OP_0D()
    Sleep(300)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x107,
        (
            "#060F啊……有了有了。\x02\x03",

            "……这下就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x12, 255)
    SetChrPos(0x12, -3950, -1000, 39060, 90)
    OP_8E(0x12, 0xFFFFFA88, 0x0, 0x95B0, 0x7D0, 0x0)
    OP_8C(0x12, 135, 400)

    ChrTalk(    #71
        0x12,
        "#1460F#2P找到了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #72
        0x107,
        "#060F#2P咦，爸爸……\x02",
    )

    CloseMessageWindow()

    def lambda_2A79():
        OP_6D(3150, 0, 36870, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2A79)
    OP_8E(0x12, 0x262, 0x1F4, 0x8912, 0x7D0, 0x0)
    OP_8C(0x12, 90, 400)
    WaitChrThread(0x107, 0x0)

    ChrTalk(    #73
        0x107,
        "#060F#2P不用看着锅吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x12,
        (
            "#1460F#6P啊啊……\x01",
            "让它一直煮着就好了。\x02\x03",

            "比起那个，\x01",
            "我倒是更在意提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        "#060F#2P我、我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12,
        (
            "#1460F#6P刚才提妲也说了吧？\x02\x03",

            "想再多听一些话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x107,
        "#060F#2P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12,
        (
            "#1460F#6P我仔细考虑过你的话。\x02\x03",

            "把你抛下两年不管\x01",
            "却被那样说……\x02\x03",

            "我们真是\x01",
            "差劲的父母啊。\x02",
        )
    )

    Jump("loc_2C00")

    label("loc_2C00")

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        (
            "#060F#2P爸、爸爸……\x02\x03",

            "不是的……\x01",
            "没、没有那种事。\x02\x03",

            "这样我就已经很满足了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#1460F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        (
            "#060F#2P虽然不能和你们说话，\x01",
            "还是觉得有点寂寞……\x02\x03",

            "但是，\x01",
            "能和爷爷、妈妈一起做实验，\x01",
            "我也一样很开心。\x02\x03",

            "虽然有点奇怪，\x01",
            "不过这就是我们\x01",
            "一家团聚的方式吧……\x02\x03",

            "嘿嘿……\x01",
            "我现在就是这么想的。\x02",
        )
    )

    Jump("loc_2D6A")

    label("loc_2D6A")

    CloseMessageWindow()

    ChrTalk(    #82
        0x12,
        "#1460F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        "#060F#2P……怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x12,
        (
            "#1460F#6P不、不，真令人吃惊啊。\x02\x03",

            "我觉得这真是\x01",
            "成熟的想法啊。\x02\x03",

            "呼，一阵子没见，\x01",
            "你真的长大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x107,
        (
            "#060F#2P是、是吗？\x02\x03",

            "不过，\x01",
            "也是因为发生了很多事……\x02",
        )
    )

    Jump("loc_2E71")

    label("loc_2E71")

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "#1460F#6P唔，『很多事』吗……\x02\x03",

            "……比如说阿加特大哥哥？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x107,
        (
            "#060F#2P啊、啊！？\x02\x03",

            "为、为什么突然说起这个！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#1460F#6P哈哈，看来说中了。\x02\x03",

            "……他是很重要的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x107,
        (
            "#060F#2P唔……\x02\x03",

            "……嗯，很重要。\x02\x03",

            "不知为什么，\x01",
            "妈妈好像误会了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#1460F#6P妈妈会担心\x01",
            "也是理所当然的。\x02\x03",

            "爸爸还在当游击士的时候\x01",
            "也总让妈妈担心呢。\x02\x03",

            "她是不希望让提妲你\x01",
            "也经历相同的感受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x107,
        (
            "#060F#2P啊……\x02\x03",

            "所、所以才那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        (
            "#1460F#6P嗯，\x01",
            "希望你也能理解妈妈的心情……\x02\x03",

            "说到底，\x01",
            "要是有误会就应该先解除才是。\x02",
        )
    )

    Jump("loc_30AE")

    label("loc_30AE")

    CloseMessageWindow()

    ChrTalk(    #93
        0x107,
        (
            "#060F#2P是、是啊。\x02\x03",

            "但是，\x01",
            "突然叫他来我们家的话……\x02",
        )
    )

    Jump("loc_30FE")

    label("loc_30FE")

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        (
            "#1460F#6P……太危险了，还是算了吧。\x02\x03",

            "妈妈生起气来\x01",
            "就不知道会发生什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        "#060F#2P……也、也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x12,
        (
            "#1460F#6P唔，条件真严峻啊。\x02\x03",

            "要是能有什么借口\x01",
            "让他过来就好了……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x107,
        "#060F#2P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x12,
        (
            "#1460F#6P……不，我想到办法了。\x02\x03",

            "好，\x01",
            "我去搅一下锅里的东西。\x02",
        )
    )

    Jump("loc_324E")

    label("loc_324E")

    CloseMessageWindow()

    def lambda_3255():
        OP_6D(2500, 0, 37500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3255)

    def lambda_326D():
        OP_6E(300, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_326D)
    OP_8C(0x12, 315, 400)

    def lambda_3284():
        OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0x8F8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3284)
    Sleep(200)

    ChrTalk(    #99
        0x107,
        "#060F#2P爸、爸爸？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x12, 0x0)
    Sleep(300)
    OP_8C(0x12, 90, 400)
    Sleep(300)

    ChrTalk(    #100
        0x12,
        (
            "#1460F#6P解除误会的事\x01",
            "就交给爸爸吧。\x02\x03",

            "虽然会花点时间，\x01",
            "不过我不会给你捣乱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        "#060F#2P嗯、嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x12,
        "#1460F#6P那么，晚饭见。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_337E():
        OP_6D(930, 0, 38980, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_337E)
    OP_43(0x12, 0x0, 0x0, 0x10)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x107, 0x0)

    def lambda_33A7():
        OP_6D(2950, 500, 36100, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_33A7)

    def lambda_33BF():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_33BF)
    WaitChrThread(0x107, 0x0)

    ChrTalk(    #103
        0x107,
        (
            "#060F#5P呼……吓了我一跳。\x02\x03",

            "竟然突然说起\x01",
            "阿加特大哥哥的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x107,
        (
            "#060F#5P不、不好！\x01",
            "要把书送过去才是！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0xF)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x250A)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2946 end

    def Function_15_3496(): pass

    label("Function_15_3496")

    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xFFFFFB14, 0x0, 0x975E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFECAA, 0xFFFFF830, 0x97E0, 0x1388, 0x0)

    def lambda_34CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34CB)
    OP_8E(0xFE, 0xFFFFE6B0, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_3496 end

    def Function_16_34F8(): pass

    label("Function_16_34F8")

    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x96D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFECAA, 0xFFFFF830, 0x97E0, 0x7D0, 0x0)

    def lambda_352D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_352D)
    OP_8E(0xFE, 0xFFFFE6B0, 0xFFFFF830, 0x9772, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_34F8 end

    SaveToFile()

Try(main)
