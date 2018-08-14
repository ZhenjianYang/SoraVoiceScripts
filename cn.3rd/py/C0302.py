from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C0302   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0302.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '魔兽',                                 # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '约修亚',                               # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT09/CH10240 ._CH',             # 00
        'ED6_DT07/CH02750 ._CH',             # 01
        'ED6_DT26/CH20789 ._CH',             # 02
        'ED6_DT26/CH20794 ._CH',             # 03
        'ED6_DT26/CH20795 ._CH',             # 04
        'ED6_DT09/CH10241 ._CH',             # 05
        'ED6_DT09/CH10243 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT09/CH10240P._CP',             # 00
        'ED6_DT07/CH02750P._CP',             # 01
        'ED6_DT26/CH20789P._CP',             # 02
        'ED6_DT26/CH20794P._CP',             # 03
        'ED6_DT26/CH20795P._CP',             # 04
        'ED6_DT09/CH10241P._CP',             # 05
        'ED6_DT09/CH10243P._CP',             # 06
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
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
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
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
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
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
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
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
        "Function_0_1A2",          # 00, 0
        "Function_1_1C1",          # 01, 1
        "Function_2_1C2",          # 02, 2
        "Function_3_189A",         # 03, 3
        "Function_4_18CF",         # 04, 4
        "Function_5_1904",         # 05, 5
        "Function_6_1939",         # 06, 6
        "Function_7_196E",         # 07, 7
        "Function_8_19A3",         # 08, 8
        "Function_9_19D8",         # 09, 9
        "Function_10_1A0D",        # 0A, 10
        "Function_11_1A55",        # 0B, 11
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1C0")

    Return()

    # Function_0_1A2 end

    def Function_1_1C1(): pass

    label("Function_1_1C1")

    Return()

    # Function_1_1C1 end

    def Function_2_1C2(): pass

    label("Function_2_1C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(57060, -170, 17970, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_11(0x46, 0x6E, 0x78, 0x4E20, 0x13880, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x101, 57150, -30, 7470, 180)
    SetChrPos(0x10, 51380, -30, 9160, 74)
    SetChrPos(0x11, 54370, 140, 3290, 36)
    SetChrPos(0x12, 60220, -120, 2290, 352)
    SetChrPos(0x13, 64040, -90, 5550, 284)
    OP_71(0x4, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x5, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x6, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    LoadEffect(0x0, "Craft\\cr161_00.eff")
    LoadEffect(0x1, "Craft\\cr163_00.eff")
    LoadEffect(0x2, "Craft\\cr163_01.eff")
    SoundLoad(389)
    SoundLoad(569)
    SoundLoad(129)

    def lambda_2F6():
        OP_6D(57060, -170, 7970, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2F6)

    def lambda_30E():
        OP_8F(0xFE, 0xDF3E, 0xFFFFFFE2, 0x24FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30E)

    def lambda_329():

        label("loc_329")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_329")

    QueueWorkItem2(0x10, 3, lambda_329)

    def lambda_33C():

        label("loc_33C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_33C")

    QueueWorkItem2(0x11, 3, lambda_33C)

    def lambda_34F():

        label("loc_34F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_34F")

    QueueWorkItem2(0x12, 3, lambda_34F)

    def lambda_362():

        label("loc_362")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_362")

    QueueWorkItem2(0x13, 3, lambda_362)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)
    Sleep(1500)
    OP_22(0x193, 0x0, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x13, 0x0, 0x0, 0x7)
    OP_8C(0x101, 225, 500)
    Sleep(800)
    OP_8C(0x101, 135, 500)
    Sleep(800)
    OP_8C(0x101, 180, 500)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#292F#11P这是我的！\x01",
            "才不会给你们！\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x101, 0x0, 0x12C, 0x0, 0x12C, 0x1388)

    ChrTalk(    #1
        0x101,
        (
            "#294F#11P你、你们这些家伙！！\x02\x03",

            "嘘、嘘，到那边去！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x3)
    OP_43(0x10, 0x0, 0x0, 0x8)
    Sleep(800)

    def lambda_4D7():
        OP_6D(57060, -170, 9970, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4D7)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_501():
        OP_8F(0xFE, 0xDF3E, 0xFFFFFFF6, 0x2B7A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_501)

    ChrTalk(    #2
        0x101,
        (
            "#297F#11P……不是说了嘛！\x02\x03",

            "不要到这边来！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)

    def lambda_579():

        label("loc_579")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_579")

    QueueWorkItem2(0x10, 3, lambda_579)

    def lambda_58C():

        label("loc_58C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_58C")

    QueueWorkItem2(0x11, 3, lambda_58C)

    def lambda_59F():

        label("loc_59F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_59F")

    QueueWorkItem2(0x12, 3, lambda_59F)

    def lambda_5B2():

        label("loc_5B2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5B2")

    QueueWorkItem2(0x13, 3, lambda_5B2)
    Sleep(500)

    def lambda_5CA():
        OP_6D(57520, 0, 10690, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_5CA)

    def lambda_5E2():
        OP_6C(320000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5E2)

    def lambda_5F2():
        OP_67(0, 4500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5F2)

    def lambda_60A():
        OP_6B(2960, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_60A)
    OP_43(0x101, 0x3, 0x0, 0xB)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 3)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 51030, 130, 4130, 80)
    OP_7D(0x0, 0x14, 0x28, 0x190)

    def lambda_64E():
        OP_96(0xFE, 0xC760, 0xFFFFFFEC, 0x2DAA, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_64E)
    OP_22(0x195, 0x0, 0x64)
    OP_44(0x12, 0x3)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)

    def lambda_67F():
        OP_8F(0xFE, 0xDF3E, 0xFFFFFFF6, 0x2B7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_67F)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 90, 0)

    def lambda_6B5():
        OP_96(0xFE, 0xE0B0, 0x0, 0x29C2, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6B5)
    Sleep(300)
    PlayEffect(0x0, 0x0, 0x12, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F5, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x96, 0x96, 0xBB8, 0x12C)
    OP_7D(0x1, 0x14, 0x0, 0x0)
    OP_44(0x12, 0x1)
    OP_22(0x21A, 0x0, 0x64)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)

    def lambda_743():
        OP_96(0xFE, 0xE90C, 0xFFFFFEC0, 0x1342, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_743)
    Sleep(500)

    def lambda_766():
        OP_9E(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_766)
    Sleep(1000)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_78F():

        label("loc_78F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_78F")

    QueueWorkItem2(0x12, 3, lambda_78F)
    Fade(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 3)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 180, 0)
    ClearChrFlags(0x14, 0x20)
    OP_0D()

    ChrTalk(    #3
        0x101,
        "#293F#5P咦………………？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    NpcTalk(    #4
        0x14,
        "少年",
        "#1670F#11P躲在我的背后。\x02",
    )

    Jump("loc_818")

    label("loc_818")

    CloseMessageWindow()

    def lambda_81F():
        OP_6D(57540, 0, 10660, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_81F)

    def lambda_837():
        OP_6C(344000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_837)

    def lambda_847():
        OP_67(0, 4720, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_847)

    def lambda_85F():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_85F)
    OP_8C(0x10, 74, 0)
    WaitChrThread(0x15, 0x0)
    OP_22(0x21F, 0x0, 0x64)
    OP_D9(0x0, "CTI02750")
    OP_22(0x185, 0x0, 0x64)
    OP_6B(3060, 0)
    OP_7C(0x64, 0x64, 0xBB8, 0x7D0)
    Sleep(2000)
    OP_D9(0x1)
    PlayEffect(0x1, 0x0, 0x14, 0, -1300, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1200)

    def lambda_8EB():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_8EB)
    OP_22(0x239, 0x0, 0x64)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 6)
    SetChrSubChip(0x13, 0)
    PlayEffect(0x2, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x11, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x12, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x13, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A0C():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A0C)

    def lambda_A26():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A26)

    def lambda_A40():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A40)

    def lambda_A5A():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A5A)
    Sleep(500)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(1500)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 0)
    SetChrSubChip(0x13, 0)

    def lambda_AAB():

        label("loc_AAB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AAB")

    QueueWorkItem2(0x10, 3, lambda_AAB)

    def lambda_ABE():

        label("loc_ABE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_ABE")

    QueueWorkItem2(0x11, 3, lambda_ABE)

    def lambda_AD1():

        label("loc_AD1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AD1")

    QueueWorkItem2(0x12, 3, lambda_AD1)

    def lambda_AE4():

        label("loc_AE4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AE4")

    QueueWorkItem2(0x13, 3, lambda_AE4)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B0E():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B0E)
    Sleep(50)
    OP_22(0x81, 0x0, 0x64)
    OP_20(0xBB8)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)

    def lambda_B35():
        OP_8F(0xFE, 0x11490, 0xFFFFFEDE, 0x6C2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B35)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B62():
        OP_8C(0xFE, 210, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B62)
    Sleep(50)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)

    def lambda_B7F():
        OP_8F(0xFE, 0xC4A4, 0x104, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B7F)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_BAC():
        OP_8C(0xFE, 164, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_BAC)
    Sleep(50)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)

    def lambda_BC9():
        OP_8F(0xFE, 0xF4EC, 0x6E, 0xFFFFEC82, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BC9)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_BF6():
        OP_8C(0xFE, 255, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BF6)
    Sleep(50)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)

    def lambda_C13():
        OP_8F(0xFE, 0xA5D2, 0xFA, 0x1478, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C13)
    Sleep(3000)
    OP_21()
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    def lambda_C58():
        OP_6D(56940, 40, 12740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C58)

    def lambda_C70():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C70)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    NpcTalk(    #5
        0x14,
        "少年",
        (
            "#1677F#6P（呼………………）\x02\x03",

            "#1675F（以现在的体力，\x01",
            "  这已经是极限了吧……）\x02",
        )
    )

    Jump("loc_CEE")

    label("loc_CEE")

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#293F#5P啊，跑掉了……\x02\x03",

            "我、我说……\x01",
            "…………约修亚……？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(55780, 30, 10650, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(121000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 54450, 10, 12120, 180)
    SetChrPos(0x14, 54930, 20, 10520, 180)
    Sleep(2000)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)
    Fade(300)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 1)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x14, 0x101, 500)
    Sleep(200)

    ChrTalk(    #7
        0x14,
        "#1672F#11P#3S你到底在干什么！！#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#293F#6P咦……！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB3)
    Sleep(500)

    ChrTalk(    #9
        0x14,
        (
            "#1670F#11P竟然跑到这种森林的深处来，\x01",
            "还被魔兽袭击……\x02\x03",

            "#1672F明明是个小孩子，居然做如此危险的事情！\x02\x03",

            "#1672F……你总是这么鲁莽。\x01",
            "怎么也要看清楚周围的状况再行动吧！\x02\x03",

            "#1675F这样的话……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#293F#6P约修亚…………\x02\x03",

            "#291F嘿嘿，这下正好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x14,
        (
            "#1672F#11P……哪里好了！\x02\x03",

            "如果我不来的话，\x01",
            "现在你…………！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#290F#6P好啦，你看这个！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_AD(0x2400D9, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetMessageWindowPos(80, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #13
        (
            "\x07\x00……怎么样，约修亚！\x01",
            "最终还是让我抓住了吧！\x02\x03",

            "#100W这家伙就是…………\x02",
        )
    )

    Jump("loc_1087")

    label("loc_1087")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(30, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #14
        "\x07\x00#5S#20W『传说中的虫』！！#2S\x02",
    )

    Jump("loc_10D6")

    label("loc_10D6")

    OP_7C(0x0, 0x12C, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 330, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #15
        (
            "\x07\x00#1678F……这………………！？\x02\x03",

            "…………………………\x02\x03",

            "#1677F（……太大了…………）\x02",
        )
    )

    Jump("loc_116E")

    label("loc_116E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #16
        0x101,
        "#291F#6P哈哈……不得了吧！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)

    ChrTalk(    #17
        0x101,
        "#296F#6P对了，约修亚……\x02",
    )

    CloseMessageWindow()

    def lambda_11F2():
        OP_8E(0xFE, 0xD548, 0xA, 0x2D50, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11F2)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #18
        0x101,
        (
            "#295F#6P如果你有什么心里不好受的……\x02\x03",

            "又不愿意说出来的话，\x01",
            "……那我就不问了。\x02\x03",

            "#299F我就等到你愿意跟我说为止。\x02\x03",

            "……在那之前，我都会待在你身边哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #19
        0x14,
        "#1678F#11P#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#290F#6P…………嗯。\x02\x03",

            "#291F这只虫给你！\x01",
            "好了，这下该打起精神来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14,
        "#1675F#11P…………………………\x02",
    )

    CloseMessageWindow()
    StopSound(0x61A8, 0x13880, 0xBB8)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #22
        0x14,
        (
            "#1679F#11P哼………………\x02\x03",

            "#1679F……这就是传说中的虫吗？\x01",
            "没有什么了不起的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        (
            "#294F#6P#3S什么…………！！#2S\x02\x03",

            "没，没什么了不起！？\x01",
            "这么大居然还说没什么了不起！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        (
            "#1679F#11P嗯，这根本不算什么。\x02\x03",

            "#1689F…………只有这种程度吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#292F#6P唔～～～…………\x02\x03",

            "哼，你等着……\x01",
            "绝对要让你心服口服！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(300)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x101, 120, 400)
    Sleep(300)

    ChrTalk(    #26
        0x101,
        (
            "#294F我一定会抓到更加厉害的虫子，\x01",
            "让约修亚你吓一大跳！！\x02\x03",

            "…………约修亚！！\x01",
            "你就在那里呆着！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15D5():

        label("loc_15D5")

        TurnDirection(0xFE, 0x101, 500)
        OP_48()
        Jump("loc_15D5")

    QueueWorkItem2(0x14, 2, lambda_15D5)
    SetChrFlags(0x101, 0x1000)

    def lambda_15EB():

        label("loc_15EB")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_15EB")

    QueueWorkItem2(0x101, 3, lambda_15EB)

    def lambda_15FE():
        OP_8E(0xFE, 0x104C8, 0xFFFFFFD8, 0x161C, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15FE)
    Sleep(2000)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    Sleep(500)
    OP_44(0x14, 0x2)

    ChrTalk(    #27
        0x14,
        "#1679F#1S#6P…………已经被吓得不轻啦。#2S\x02",
    )

    CloseMessageWindow()

    def lambda_1677():
        OP_6B(3030, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1677)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x18\x07\x0C#40W我竟然发生了这么大的变化。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x18\x07\x0C#40W你真是个不可思议的孩子。\x01",
            "#40W………艾丝蒂尔…………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x18\x07\x0C#40W――于是，我许下了一个约定。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x18\x07\x0C#40W不是和其他任何人，而是和我自己做的约定。 \x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x18\x07\x0C#40W是让这个和平的世界\x01",
            "能够容纳下我这样一个特殊人物的咒文。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x18\x07\x0C#40W这是世上最为卑鄙怯懦的做法，\x01",
            "而你，到底会不会原谅我呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x18\x07\x0C#40W这是比起不断伪装自己\x01",
            "更令我担心的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x1388)
    OP_21()
    OP_C4(0x1, 0x800)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C2 end

    def Function_3_189A(): pass

    label("Function_3_189A")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_18AA():
        OP_8F(0xFE, 0xE826, 0xFFFFFECA, 0x13C4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18AA)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_3_189A end

    def Function_4_18CF(): pass

    label("Function_4_18CF")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_18DF():
        OP_8F(0xFE, 0xCD82, 0xFFFFFF38, 0x22CE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18DF)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_4_18CF end

    def Function_5_1904(): pass

    label("Function_5_1904")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1914():
        OP_8F(0xFE, 0xD73C, 0xFFFFFF92, 0x1194, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1914)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_1904 end

    def Function_6_1939(): pass

    label("Function_6_1939")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1949():
        OP_8F(0xFE, 0xE920, 0xFFFFFEFC, 0xEEC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1949)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_1939 end

    def Function_7_196E(): pass

    label("Function_7_196E")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_197E():
        OP_8F(0xFE, 0xF46A, 0xFFFFFEC0, 0x1784, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_197E)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_196E end

    def Function_8_19A3(): pass

    label("Function_8_19A3")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_19B3():
        OP_8F(0xFE, 0xD232, 0xFFFFFF74, 0x2468, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19B3)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_19A3 end

    def Function_9_19D8(): pass

    label("Function_9_19D8")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_19E8():
        OP_8F(0xFE, 0xD84A, 0xFFFFFEDE, 0x181A, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19E8)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_19D8 end

    def Function_10_1A0D(): pass

    label("Function_10_1A0D")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1A1D():
        OP_8F(0xFE, 0xF258, 0xFFFFFF7E, 0x1DEC, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A1D)
    Sleep(1000)
    OP_8C(0xFE, 314, 0)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 284, 0)
    Return()

    # Function_10_1A0D end

    def Function_11_1A55(): pass

    label("Function_11_1A55")

    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    OP_8C(0x101, 0, 400)

    def lambda_1A79():
        OP_8F(0xFE, 0xDEE4, 0x14, 0x3002, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A79)
    Sleep(100)
    OP_8C(0x10, 36, 400)
    Sleep(100)
    OP_8C(0x13, 314, 400)
    Return()

    # Function_11_1A55 end

    SaveToFile()

Try(main)
