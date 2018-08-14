from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4138   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4138.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '暗黑死刃',                             # 9
        '暗黑死刃',                             # 10
        '暗黑死刃',                             # 11
        '暗黑死刃',                             # 12
        '封印石③',                             # 13
        '',                                     # 14
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
        'ED6_DT29/CH14520 ._CH',             # 00
        'ED6_DT29/CH14521 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04150 ._CH',             # 03
        'ED6_DT07/CH00160 ._CH',             # 04
        'ED6_DT27/CH04580 ._CH',             # 05
        'ED6_DT26/CH20621 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH14520P._CP',             # 00
        'ED6_DT29/CH14521P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04150P._CP',             # 03
        'ED6_DT07/CH00160P._CP',             # 04
        'ED6_DT27/CH04580P._CP',             # 05
        'ED6_DT26/CH20621P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -49190,
        TriggerZ            = 1000,
        TriggerY            = 63810,
        TriggerRange        = 1000,
        ActorX              = -49190,
        ActorZ              = 2000,
        ActorY              = 63810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = 76130,
        TriggerRange        = 1000,
        ActorX              = 4970,
        ActorZ              = 1000,
        ActorY              = 76130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54740,
        TriggerZ            = 0,
        TriggerY            = 65190,
        TriggerRange        = 1000,
        ActorX              = 54740,
        ActorZ              = 1000,
        ActorY              = 65190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_32B",          # 02, 2
        "Function_3_867",          # 03, 3
        "Function_4_88B",          # 04, 4
        "Function_5_8B4",          # 05, 5
        "Function_6_8EF",          # 06, 6
        "Function_7_918",          # 07, 7
        "Function_8_9BB",          # 08, 8
        "Function_9_A5E",          # 09, 9
        "Function_10_B01",         # 0A, 10
        "Function_11_BA4",         # 0B, 11
        "Function_12_102A",        # 0C, 12
        "Function_13_133E",        # 0D, 13
        "Function_14_145E",        # 0E, 14
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_21B")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_1EE end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_22F")
    OP_B1("U4138_y")
    Jump("loc_238")

    label("loc_22F")

    OP_B1("U4138_n")

    label("loc_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, -49000, 2100, 63810, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2F8")

    label("loc_2F4")

    OP_64(0x0, 0x1)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A")
    OP_6F(0x5, 0)
    Jump("loc_311")

    label("loc_30A")

    OP_6F(0x5, 60)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323")
    OP_6F(0x6, 0)
    Jump("loc_32A")

    label("loc_323")

    OP_6F(0x6, 60)

    label("loc_32A")

    Return()

    # Function_1_21C end

    def Function_2_32B(): pass

    label("Function_2_32B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A2(0x2705)
    LoadEffect(0x1, "map\\mp250_01.eff")
    SetChrPos(0x109, 140, 0, 630, 0)
    SetChrPos(0x10F, 1260, 0, 70, 0)
    SetChrPos(0x107, -170, 0, -930, 0)
    SetChrPos(0x10E, 1320, 0, -1310, 0)
    OP_6D(1510, 5500, 7940, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)

    def lambda_3D4():
        OP_6D(1510, 0, 7940, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D4)

    def lambda_3EC():
        OP_67(0, 6130, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3EC)

    def lambda_404():
        OP_6B(2480, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_404)

    def lambda_414():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_414)

    def lambda_424():
        OP_8E(0xFE, 0xA0, 0x0, 0x1CA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_424)
    Sleep(100)

    def lambda_444():
        OP_8E(0xFE, 0x56E, 0x0, 0x1B62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_444)
    Sleep(100)

    def lambda_464():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x1720, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_464)
    Sleep(100)

    def lambda_484():
        OP_8E(0xFE, 0x46A, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_484)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    def lambda_4CC():
        OP_6B(2600, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4CC)
    OP_43(0x10, 0x0, 0x0, 0x7)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0x107, 0x0, 0x0, 0x5)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    WaitChrThread(0x13, 0x0)
    OP_1D(0x97)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1441F#6P……呜……………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #1
        0x109,
        "#1069F#6P突然袭击吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x107,
        "#065F#5P哇、哇啊啊……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x10E,
        "#177F#6P……来了！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_641():
        OP_6D(1730, 0, 7710, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_641)

    def lambda_659():
        OP_6B(1900, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_659)

    def lambda_669():

        label("loc_669")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_669")

    QueueWorkItem2(0x10, 3, lambda_669)
    SetChrChipByIndex(0x10, 1)

    def lambda_681():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0x15B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_681)
    Sleep(20)

    def lambda_6A1():

        label("loc_6A1")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_6A1")

    QueueWorkItem2(0x12, 3, lambda_6A1)
    SetChrChipByIndex(0x12, 1)

    def lambda_6B9():
        OP_8F(0xFE, 0x848, 0x0, 0x2076, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6B9)
    Sleep(20)

    def lambda_6D9():

        label("loc_6D9")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_6D9")

    QueueWorkItem2(0x13, 3, lambda_6D9)
    SetChrChipByIndex(0x13, 1)

    def lambda_6F1():
        OP_8F(0xFE, 0xA78, 0x0, 0x1608, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6F1)
    Sleep(30)

    def lambda_711():

        label("loc_711")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_711")

    QueueWorkItem2(0x11, 3, lambda_711)
    SetChrChipByIndex(0x11, 1)

    def lambda_729():
        OP_8F(0xFE, 0xFFFFFE8E, 0x0, 0x2242, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_729)
    WaitChrThread(0x109, 0x0)
    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_76E"),
        (2, "loc_853"),
        (1, "loc_85F"),
        (SWITCH_DEFAULT, "loc_864"),
    )


    label("loc_76E")

    EventBegin(0x0)
    OP_6D(810, 0, 5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x0, 810, 0, 5780, 0)
    SetChrPos(0x1, 810, 0, 5780, 0)
    SetChrPos(0x2, 810, 0, 5780, 0)
    SetChrPos(0x3, 810, 0, 5780, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2706)
    FadeToBright(1000, 0)
    Jump("loc_864")

    label("loc_853")

    NewScene("ED6_DT21/U4101   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_864")

    label("loc_85F")

    OP_B4(0x0)
    Jump("loc_864")

    label("loc_864")

    EventEnd(0x0)
    Return()

    # Function_2_32B end

    def Function_3_867(): pass

    label("Function_3_867")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1300)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_867 end

    def Function_4_88B(): pass

    label("Function_4_88B")

    Sleep(50)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_88B end

    def Function_5_8B4(): pass

    label("Function_5_8B4")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_8B4 end

    def Function_6_8EF(): pass

    label("Function_6_8EF")

    Sleep(150)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_8EF end

    def Function_7_918(): pass

    label("Function_7_918")

    SetChrPos(0xFE, -4780, 0, 5780, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_93F():

        label("loc_93F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_93F")

    QueueWorkItem2(0xFE, 3, lambda_93F)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x0, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_9A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A1)
    OP_82(0x0, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_7_918 end

    def Function_8_9BB(): pass

    label("Function_8_9BB")

    SetChrPos(0xFE, -1530, 0, 11320, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9E2():

        label("loc_9E2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_9E2")

    QueueWorkItem2(0xFE, 3, lambda_9E2)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x1, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_A44():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A44)
    OP_82(0x1, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_8_9BB end

    def Function_9_A5E(): pass

    label("Function_9_A5E")

    SetChrPos(0xFE, 3480, 0, 10830, 225)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A85():

        label("loc_A85")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A85")

    QueueWorkItem2(0xFE, 3, lambda_A85)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_AE7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE7)
    OP_82(0x2, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_9_A5E end

    def Function_10_B01(): pass

    label("Function_10_B01")

    SetChrPos(0xFE, 6000, 0, 5870, 270)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_B28():

        label("loc_B28")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B28")

    QueueWorkItem2(0xFE, 3, lambda_B28)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_B8A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8A)
    OP_82(0x3, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_10_B01 end

    def Function_11_BA4(): pass

    label("Function_11_BA4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "map\\mp250_01.eff")
    SetChrPos(0x109, 140, 0, 630, 0)
    SetChrPos(0x10F, 1260, 0, 70, 0)
    SetChrPos(0x107, -170, 0, -930, 0)
    SetChrPos(0x10E, 1320, 0, -1310, 0)
    OP_6D(1510, 5500, 7940, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)

    def lambda_C4A():
        OP_6D(1510, 0, 7940, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C4A)

    def lambda_C62():
        OP_67(0, 6130, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C62)

    def lambda_C7A():
        OP_6B(2480, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C7A)

    def lambda_C8A():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C8A)

    def lambda_C9A():
        OP_8E(0xFE, 0xA0, 0x0, 0x1CA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C9A)
    Sleep(100)

    def lambda_CBA():
        OP_8E(0xFE, 0x56E, 0x0, 0x1B62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CBA)
    Sleep(100)

    def lambda_CDA():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x1720, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_CDA)
    Sleep(100)

    def lambda_CFA():
        OP_8E(0xFE, 0x46A, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_CFA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    def lambda_D42():
        OP_6B(2600, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_D42)
    OP_43(0x10, 0x0, 0x0, 0x7)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0xA)
    WaitChrThread(0x13, 0x0)

    def lambda_D82():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_D82)
    Sleep(100)
    OP_8C(0x10E, 90, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_DFB():
        OP_6D(1730, 0, 7710, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DFB)

    def lambda_E13():
        OP_6B(1900, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E13)

    def lambda_E23():

        label("loc_E23")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E23")

    QueueWorkItem2(0x10, 3, lambda_E23)
    SetChrChipByIndex(0x10, 1)

    def lambda_E3B():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0x15B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E3B)
    Sleep(20)

    def lambda_E5B():

        label("loc_E5B")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E5B")

    QueueWorkItem2(0x12, 3, lambda_E5B)
    SetChrChipByIndex(0x12, 1)

    def lambda_E73():
        OP_8F(0xFE, 0x848, 0x0, 0x2076, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E73)
    Sleep(20)

    def lambda_E93():

        label("loc_E93")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E93")

    QueueWorkItem2(0x13, 3, lambda_E93)
    SetChrChipByIndex(0x13, 1)

    def lambda_EAB():
        OP_8F(0xFE, 0xA78, 0x0, 0x1608, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_EAB)
    Sleep(30)

    def lambda_ECB():

        label("loc_ECB")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_ECB")

    QueueWorkItem2(0x11, 3, lambda_ECB)
    SetChrChipByIndex(0x11, 1)

    def lambda_EE3():
        OP_8F(0xFE, 0xFFFFFE8E, 0x0, 0x2242, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_EE3)
    WaitChrThread(0x109, 0x0)
    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F28"),
        (2, "loc_1016"),
        (1, "loc_1022"),
        (SWITCH_DEFAULT, "loc_1027"),
    )


    label("loc_F28")

    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(810, 0, 5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x0, 810, 0, 5780, 0)
    SetChrPos(0x1, 810, 0, 5780, 0)
    SetChrPos(0x2, 810, 0, 5780, 0)
    SetChrPos(0x3, 810, 0, 5780, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2706)
    FadeToBright(1000, 0)
    Jump("loc_1027")

    label("loc_1016")

    NewScene("ED6_DT21/U4101   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_1027")

    label("loc_1022")

    OP_B4(0x0)
    Jump("loc_1027")

    label("loc_1027")

    EventEnd(0x0)
    Return()

    # Function_11_BA4 end

    def Function_12_102A(): pass

    label("Function_12_102A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -49390, 1000, 62530, 0)
    SetChrPos(0x10F, -47550, 1000, 63700, 270)
    SetChrPos(0x107, -50770, 1000, 62130, 45)
    SetChrPos(0x10E, -51210, 1000, 63420, 90)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_6D(-48350, 1000, 64590, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 6)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x14, 0xFFFF4034, 0x898, 0xF64A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x14, 0x80)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x54\x03\x07\x00。\x02",
    )

    Jump("loc_1168")

    label("loc_1168")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x354, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x10E,
        "#173F#6P那个……难道是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1448F#2P……没错。\x01",
            "之前封印上尉的就是\x01",
            "和这个一样的宝石。\x02\x03",

            "这里面应该也\x01",
            "封印着某个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#062F#6P嗯，\x01",
            "说到帝国大使馆的话……\x02\x03",

            "#064F啊，对了，\x01",
            "约修亚哥哥也是出身于埃雷波尼亚……\x02\x03",

            "#067F唔……\x01",
            "到底会是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1075F#2P反正我们解开之后\x01",
            "就知道了嘛。\x02\x03",

            "#1060F总之趁这个机会\x01",
            "先回据点一趟吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2707)
    OP_28(0x2B, 0x1, 0x40)
    OP_28(0x2B, 0x1, 0x80)
    OP_64(0x0, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_102A end

    def Function_13_133E(): pass

    label("Function_13_133E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x611, 1)"), scpexpr(EXPR_END)), "loc_13B0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x11\x06\x07\x00。\x02",
    )

    Jump("loc_1395")

    label("loc_1395")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BE)
    Jump("loc_141C")

    label("loc_13B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x11\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x11\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_13FD")

    label("loc_13FD")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_141C")

    Jump("loc_1450")

    label("loc_141F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1450")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_133E end

    def Function_14_145E(): pass

    label("Function_14_145E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_14D0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_14B5")

    label("loc_14B5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BF)
    Jump("loc_153C")

    label("loc_14D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_151D")

    label("loc_151D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_153C")

    Jump("loc_1570")

    label("loc_153F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1570")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_145E end

    SaveToFile()

Try(main)
