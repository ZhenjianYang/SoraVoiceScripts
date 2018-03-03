from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Monster',                              # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Joshua',                               # 13
        'Target Camera',                        # 14
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
        "Function_3_188A",         # 03, 3
        "Function_4_18BF",         # 04, 4
        "Function_5_18F4",         # 05, 5
        "Function_6_1929",         # 06, 6
        "Function_7_195E",         # 07, 7
        "Function_8_1993",         # 08, 8
        "Function_9_19C8",         # 09, 9
        "Function_10_19FD",        # 0A, 10
        "Function_11_1A45",        # 0B, 11
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
        "#292F#11PThis is mine! You can't have it!\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x101, 0x0, 0x12C, 0x0, 0x12C, 0x1388)

    ChrTalk(    #1
        0x101,
        (
            "#294F#11PGo away!\x02\x03",

            "Shoo! Shoo!\x02",
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

    def lambda_4B6():
        OP_6D(57060, -170, 9970, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4B6)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4E0():
        OP_8F(0xFE, 0xDF3E, 0xFFFFFFF6, 0x2B7A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E0)

    ChrTalk(    #2
        0x101,
        (
            "#297F#11PD-Don't come any closer!\x02\x03",

            "A-Are you listening to me?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)

    def lambda_55C():

        label("loc_55C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_55C")

    QueueWorkItem2(0x10, 3, lambda_55C)

    def lambda_56F():

        label("loc_56F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_56F")

    QueueWorkItem2(0x11, 3, lambda_56F)

    def lambda_582():

        label("loc_582")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_582")

    QueueWorkItem2(0x12, 3, lambda_582)

    def lambda_595():

        label("loc_595")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_595")

    QueueWorkItem2(0x13, 3, lambda_595)
    Sleep(500)

    def lambda_5AD():
        OP_6D(57520, 0, 10690, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_5AD)

    def lambda_5C5():
        OP_6C(320000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5C5)

    def lambda_5D5():
        OP_67(0, 4500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5D5)

    def lambda_5ED():
        OP_6B(2960, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_5ED)
    OP_43(0x101, 0x3, 0x0, 0xB)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 3)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 51030, 130, 4130, 80)
    OP_7D(0x0, 0x14, 0x28, 0x190)

    def lambda_631():
        OP_96(0xFE, 0xC760, 0xFFFFFFEC, 0x2DAA, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_631)
    OP_22(0x195, 0x0, 0x64)
    OP_44(0x12, 0x3)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)

    def lambda_662():
        OP_8F(0xFE, 0xDF3E, 0xFFFFFFF6, 0x2B7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_662)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 90, 0)

    def lambda_698():
        OP_96(0xFE, 0xE0B0, 0x0, 0x29C2, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_698)
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

    def lambda_726():
        OP_96(0xFE, 0xE90C, 0xFFFFFEC0, 0x1342, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_726)
    Sleep(500)

    def lambda_749():
        OP_9E(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_749)
    Sleep(1000)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_772():

        label("loc_772")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_772")

    QueueWorkItem2(0x12, 3, lambda_772)
    Fade(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 3)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 180, 0)
    ClearChrFlags(0x14, 0x20)
    OP_0D()

    ChrTalk(    #3
        0x101,
        "#293F#5P...Wha...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    NpcTalk(    #4
        0x14,
        "Joshua",
        "#1670F#11PGet behind me.\x02",
    )

    CloseMessageWindow()

    def lambda_7EA():
        OP_6D(57540, 0, 10660, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7EA)

    def lambda_802():
        OP_6C(344000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_802)

    def lambda_812():
        OP_67(0, 4720, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_812)

    def lambda_82A():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_82A)
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

    def lambda_8B6():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_8B6)
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

    def lambda_9D7():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9D7)

    def lambda_9F1():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_9F1)

    def lambda_A0B():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A0B)

    def lambda_A25():
        OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A25)
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

    def lambda_A76():

        label("loc_A76")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A76")

    QueueWorkItem2(0x10, 3, lambda_A76)

    def lambda_A89():

        label("loc_A89")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A89")

    QueueWorkItem2(0x11, 3, lambda_A89)

    def lambda_A9C():

        label("loc_A9C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A9C")

    QueueWorkItem2(0x12, 3, lambda_A9C)

    def lambda_AAF():

        label("loc_AAF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AAF")

    QueueWorkItem2(0x13, 3, lambda_AAF)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_AD9():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_AD9)
    Sleep(50)
    OP_22(0x81, 0x0, 0x64)
    OP_20(0xBB8)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)

    def lambda_B00():
        OP_8F(0xFE, 0x11490, 0xFFFFFEDE, 0x6C2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B00)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B2D():
        OP_8C(0xFE, 210, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B2D)
    Sleep(50)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)

    def lambda_B4A():
        OP_8F(0xFE, 0xC4A4, 0x104, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B4A)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B77():
        OP_8C(0xFE, 164, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_B77)
    Sleep(50)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)

    def lambda_B94():
        OP_8F(0xFE, 0xF4EC, 0x6E, 0xFFFFEC82, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B94)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_BC1():
        OP_8C(0xFE, 255, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BC1)
    Sleep(50)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)

    def lambda_BDE():
        OP_8F(0xFE, 0xA5D2, 0xFA, 0x1478, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BDE)
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

    def lambda_C23():
        OP_6D(56940, 40, 12740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C23)

    def lambda_C3B():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3B)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    NpcTalk(    #5
        0x14,
        "Joshua",
        (
            "#1677F#6P(Whew...)\x02\x03",

            "#1675F(This is about as much as I can do\x01",
            "with my current stamina...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#293F#5PThey ran away...\x02\x03",

            "U-Umm... Joshua...?\x02",
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
        "#1672F#11P#3SWhat is WRONG with you?!#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#293F#6P...Huh?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB3)
    Sleep(500)

    ChrTalk(    #9
        0x14,
        (
            "#1670F#11PWhat are you even doing this far in a place this\x01",
            "dangerous? Did you even stop to think what might\x01",
            "happen?!\x02\x03",

            "#1672FYou're a child! Don't put yourself in unnecessary\x01",
            "danger!\x02\x03",

            "#1672FWhy do you never stop to think before diving\x01",
            "headfirst into anything?! For once in your life,\x01",
            "try and look before you leap!\x02\x03",

            "#1675FOtherwise...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#293F#6PJoshua...\x02\x03",

            "#291FHeehee. You came at just the right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x14,
        (
            "#1672F#11PThat's not funny!\x02\x03",

            "If I hadn't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#290F#6PLook at this!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_AD(0x2400D9, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetMessageWindowPos(80, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #13
        (
            "\x07\x00Look! Look! I finally caught one!\x02\x03",

            "#100WThis is it!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(30, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #14
        "\x07\x00#5S#20WThis is the Bug of Legends!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 330, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #15
        (
            "\x07\x00#1678FWha...?!\x02\x03",

            "...\x02\x03",

            "#1677F(It's huge...)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #16
        0x101,
        "#291F#6PHeehee. Isn't it cool?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)

    ChrTalk(    #17
        0x101,
        "#296F#6PUmm... Joshua...\x02",
    )

    CloseMessageWindow()

    def lambda_115E():
        OP_8E(0xFE, 0xD548, 0xA, 0x2D50, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_115E)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #18
        0x101,
        (
            "#295F#6PIf something bad happened to you in the past...\x02\x03",

            "but you don't want to talk about it,\x01",
            "then I'm not going to force you to.\x02\x03",

            "#299FI'll just wait until you feel ready to talk about it\x01",
            "with me.\x02\x03",

            "Till then, I'll be right here by your side, waiting.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #19
        0x14,
        "#1678F#11P#3S...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#290F#6PThe other thing I'll do...\x02\x03",

            "#291F...is give you this bug! So cheer up, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14,
        "#1675F#11P...\x02",
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
            "#1679F#11PHeh...\x02\x03",

            "#1679FYou're telling me that bug's somehow legendary?\x01",
            "'Cause I don't see what's so impressive about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        (
            "#294F#6P#3SWhaaat?!#2S\x02\x03",

            "B-But it's huge! This is the most awesome bug\x01",
            "in the entire world!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        (
            "#1679F#11PNope.\x02\x03",

            "#1689FNot in the slightest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#292F#6PGrrr...\x02\x03",

            "You just wait!\x02",
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
            "#294FI'll find a bug that'll amaze you, even if I have\x01",
            "to search forever and ever!\x02\x03",

            "So you just wait right here!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1541():

        label("loc_1541")

        TurnDirection(0xFE, 0x101, 500)
        OP_48()
        Jump("loc_1541")

    QueueWorkItem2(0x14, 2, lambda_1541)
    SetChrFlags(0x101, 0x1000)

    def lambda_1557():

        label("loc_1557")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1557")

    QueueWorkItem2(0x101, 3, lambda_1557)

    def lambda_156A():
        OP_8E(0xFE, 0x104C8, 0xFFFFFFD8, 0x161C, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_156A)
    Sleep(2000)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    Sleep(500)
    OP_44(0x14, 0x2)

    ChrTalk(    #27
        0x14,
        "#1679F#1S#6P...You amaze me more than any bug ever will.#2S\x02",
    )

    CloseMessageWindow()

    def lambda_15EE():
        OP_6B(3030, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_15EE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x18\x07\x0C#40WBecause I can't believe how much I've changed\x01",
            "because of you...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #29
        "\x18\x07\x0C#40WYou're such a strange girl...\x02",
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
        "\x18\x07\x0C#40WIt was then that I made a promise to myself.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x18\x07\x0C#40WIt was for my own good, and no one else's.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x18\x07\x0C#40WThe only condition by which I could permit\x01",
            "something as unnatural as me to be allowed\x01",
            "to live in this peaceful world...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x18\x07\x0C#40WDoing so was the most cowardly thing I could\x01",
            "have possibly done...but I hope you can forgive\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x18\x07\x0C#40WI was more concerned about that than about\x01",
            "continuing to deceive myself.\x02",
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

    def Function_3_188A(): pass

    label("Function_3_188A")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_189A():
        OP_8F(0xFE, 0xE826, 0xFFFFFECA, 0x13C4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_189A)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_3_188A end

    def Function_4_18BF(): pass

    label("Function_4_18BF")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_18CF():
        OP_8F(0xFE, 0xCD82, 0xFFFFFF38, 0x22CE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18CF)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_4_18BF end

    def Function_5_18F4(): pass

    label("Function_5_18F4")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1904():
        OP_8F(0xFE, 0xD73C, 0xFFFFFF92, 0x1194, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1904)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_18F4 end

    def Function_6_1929(): pass

    label("Function_6_1929")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1939():
        OP_8F(0xFE, 0xE920, 0xFFFFFEFC, 0xEEC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1939)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_1929 end

    def Function_7_195E(): pass

    label("Function_7_195E")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_196E():
        OP_8F(0xFE, 0xF46A, 0xFFFFFEC0, 0x1784, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_196E)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_195E end

    def Function_8_1993(): pass

    label("Function_8_1993")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_19A3():
        OP_8F(0xFE, 0xD232, 0xFFFFFF74, 0x2468, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19A3)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_1993 end

    def Function_9_19C8(): pass

    label("Function_9_19C8")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_19D8():
        OP_8F(0xFE, 0xD84A, 0xFFFFFEDE, 0x181A, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19D8)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_19C8 end

    def Function_10_19FD(): pass

    label("Function_10_19FD")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)

    def lambda_1A0D():
        OP_8F(0xFE, 0xF258, 0xFFFFFF7E, 0x1DEC, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A0D)
    Sleep(1000)
    OP_8C(0xFE, 314, 0)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 284, 0)
    Return()

    # Function_10_19FD end

    def Function_11_1A45(): pass

    label("Function_11_1A45")

    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    OP_8C(0x101, 0, 400)

    def lambda_1A69():
        OP_8F(0xFE, 0xDEE4, 0x14, 0x3002, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A69)
    Sleep(100)
    OP_8C(0x10, 36, 400)
    Sleep(100)
    OP_8C(0x13, 314, 400)
    Return()

    # Function_11_1A45 end

    SaveToFile()

Try(main)
