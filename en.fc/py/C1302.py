from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1302   ._SN',
        MapName             = 'Bose',
        Location            = 'C1302.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Royal Army Soldier',                   # 14
        'Royal Army Soldier',                   # 15
        'Royal Army Officer',                   # 16
        'Colonel Richard',                      # 17
        'Captain Amalthea',                     # 18
        'General Morgan',                       # 19
        'Nial',                                 # 20
        'Dorothy',                              # 21
        'Royal Army Soldier',                   # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Royal Army Soldier',                   # 25
        'Royal Army Soldier',                   # 26
        'Royal Army Soldier',                   # 27
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02130 ._CH',             # 00
        'ED6_DT07/CH02120 ._CH',             # 01
        'ED6_DT07/CH02110 ._CH',             # 02
        'ED6_DT07/CH01650 ._CH',             # 03
        'ED6_DT07/CH01310 ._CH',             # 04
        'ED6_DT07/CH02030 ._CH',             # 05
        'ED6_DT07/CH02100 ._CH',             # 06
        'ED6_DT07/CH02060 ._CH',             # 07
        'ED6_DT06/CH20063 ._CH',             # 08
        'ED6_DT07/CH02080 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02130P._CP',             # 00
        'ED6_DT07/CH02120P._CP',             # 01
        'ED6_DT07/CH02110P._CP',             # 02
        'ED6_DT07/CH01650P._CP',             # 03
        'ED6_DT07/CH01310P._CP',             # 04
        'ED6_DT07/CH02030P._CP',             # 05
        'ED6_DT07/CH02100P._CP',             # 06
        'ED6_DT07/CH02060P._CP',             # 07
        'ED6_DT06/CH20063P._CP',             # 08
        'ED6_DT07/CH02080P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
    )

    DeclNpc(
        X                   = -35700,
        Z                   = 0,
        Y                   = -85400,
        Direction           = 0,
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
        X                   = -36200,
        Z                   = 0,
        Y                   = -84300,
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
        X                   = -34100,
        Z                   = 0,
        Y                   = -82100,
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
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48683,
        Z                   = -3000,
        Y                   = 29357,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209710,
        Z                   = 0,
        Y                   = 11740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_362",          # 00, 0
        "Function_1_381",          # 01, 1
        "Function_2_382",          # 02, 2
        "Function_3_398",          # 03, 3
        "Function_4_1E4A",         # 04, 4
        "Function_5_1EA5",         # 05, 5
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_36E"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D")
    OP_A2(0x35C)
    Event(0, 3)

    label("loc_37D")

    Jump("loc_380")

    label("loc_380")

    Return()

    # Function_0_362 end

    def Function_1_381(): pass

    label("Function_1_381")

    Return()

    # Function_1_381 end

    def Function_2_382(): pass

    label("Function_2_382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_397")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_382")

    label("loc_397")

    Return()

    # Function_2_382 end

    def Function_3_398(): pass

    label("Function_3_398")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-17060, 3750, -15530, 0)
    OP_67(0, 5310, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, -16500, 2000, -14000, 180)
    SetChrPos(0x103, -17120, 2000, -13840, 180)
    SetChrPos(0x102, -16600, 2000, -12660, 180)
    SetChrPos(0x104, -17460, 2000, -12310, 180)
    SetChrPos(0xB, -13140, 4000, -23900, 180)
    SetChrPos(0xA, -13220, 4000, -22610, 180)
    SetChrPos(0xD, -11860, 4000, -22360, 180)
    SetChrPos(0x8, -13031, 4000, -21770, 233)
    SetChrPos(0xC, -13750, 4000, -21750, 180)
    SetChrPos(0x9, -12600, 4000, -21120, 64)
    SetChrPos(0xF, -12300, 4000, -20010, 180)
    TurnDirection(0xB, 0xA, 0)
    TurnDirection(0xC, 0xA, 0)
    TurnDirection(0xD, 0xA, 0)
    TurnDirection(0xF, 0xA, 0)
    SetChrPos(0x13, -17040, 4000, -24290, 0)
    SetChrPos(0x14, -16980, 4000, -25880, 0)

    def lambda_508():

        label("loc_508")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_508")

    QueueWorkItem2(0x14, 1, lambda_508)

    def lambda_519():

        label("loc_519")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_519")

    QueueWorkItem2(0x13, 1, lambda_519)
    FadeToBright(1000, 0)
    OP_20(0x5DC)

    def lambda_538():
        OP_6D(-15280, 4000, -18760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_538)

    def lambda_550():
        OP_8E(0xFE, 0xFFFFBBC2, 0xFA0, 0xFFFFC126, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_550)
    Sleep(100)

    def lambda_570():
        OP_8E(0xFE, 0xFFFFBC4E, 0xFA0, 0xFFFFB9B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_570)
    Sleep(100)

    def lambda_590():
        OP_8E(0xFE, 0xFFFFBED8, 0xFA0, 0xFFFFC180, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_590)

    def lambda_5AB():
        OP_8E(0xFE, 0xFFFFC0CC, 0xFA0, 0xFFFFBC08, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AB)
    Sleep(100)

    def lambda_5CB():
        OP_8E(0xFE, 0xFFFFBBA4, 0xFA0, 0xFFFFBF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CB)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_61E():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61E)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_648():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_648)
    WaitChrThread(0x104, 0x1)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_672():
        OP_8C(0xFE, 134, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_672)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #0
        0x101,
        "#004F#3PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #1
        0x102,
        "#014FWhat's this...?\x02",
    )

    CloseMessageWindow()
    OP_21()

    def lambda_721():

        label("loc_721")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_721")

    QueueWorkItem2(0x101, 0, lambda_721)

    def lambda_732():

        label("loc_732")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_732")

    QueueWorkItem2(0x102, 0, lambda_732)

    def lambda_743():

        label("loc_743")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_743")

    QueueWorkItem2(0x103, 0, lambda_743)

    def lambda_754():

        label("loc_754")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_754")

    QueueWorkItem2(0x104, 0, lambda_754)
    OP_1D(0x65)

    def lambda_767():
        OP_6D(-8410, 4000, -22720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_767)

    def lambda_77F():
        OP_6E(437, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77F)

    def lambda_78F():
        OP_6C(125000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_78F)
    Sleep(2000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #2
        0x9,
        (
            "#201F#2PHow'd the army find out about\x01",
            "this place?\x02\x03",

            "That liar! Things weren't supposed\x01",
            "to go down like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#214F#5PHey! Get your dirty mitts\x01",
            "off of me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "#192FH-Hey! What's going on here?!\x02",
    )

    CloseMessageWindow()

    def lambda_8AF():
        OP_6D(-14680, 4000, -20970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AF)

    def lambda_8C7():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C7)

    def lambda_8DF():
        OP_6C(137000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8DF)

    def lambda_8EF():
        OP_6E(244, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EF)
    OP_43(0xB, 0x1, 0x0, 0x4)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x4)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x4)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    Sleep(600)

    ChrTalk(    #5
        0x14,
        (
            "#153F#6PSo those are the ring leaders\x01",
            "of the sky bandits?\x02\x03",

            "I'm surprised there's such a\x01",
            "young woman, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x13,
        (
            "#144F#6PHow about you shut your yap and\x01",
            "start taking some good pictures?!\x02\x03",

            "What are the chances of getting\x01",
            "another scoop like this?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    SetChrPos(0x10, -11930, 4000, -33160, 0)
    SetChrPos(0x12, -11930, 4000, -33160, 0)
    SetChrPos(0x11, -11930, 4000, -33160, 0)
    SetChrPos(0x15, -11450, 4050, -36300, 0)
    SetChrPos(0x16, -11450, 4050, -36300, 0)
    SetChrPos(0x17, -11450, 4050, -36300, 0)
    SetChrPos(0x18, -11450, 4050, -36300, 0)
    SetChrPos(0x19, -11450, 4050, -36300, 0)
    SetChrPos(0x1A, -11450, 4050, -36300, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x11, 0x4)

    def lambda_B5B():

        label("loc_B5B")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_B5B")

    QueueWorkItem2(0x14, 1, lambda_B5B)

    def lambda_B6C():

        label("loc_B6C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_B6C")

    QueueWorkItem2(0x13, 1, lambda_B6C)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    def lambda_B8D():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B8D)

    def lambda_B9B():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9B)

    def lambda_BA9():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA9)

    def lambda_BB7():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB7)

    def lambda_BC5():
        OP_6D(-15270, 4000, -25300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BC5)

    def lambda_BDD():
        OP_8E(0xFE, 0xFFFFC7AC, 0xFA0, 0xFFFFA060, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BDD)
    Sleep(400)

    def lambda_BFD():
        OP_8E(0xFE, 0xFFFFCB76, 0xFA0, 0xFFFF9AFC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BFD)
    Sleep(400)

    def lambda_C1D():
        OP_8E(0xFE, 0xFFFFC8C4, 0xFA0, 0xFFFF9674, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C1D)

    def lambda_C38():

        label("loc_C38")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C38")

    QueueWorkItem2(0x15, 1, lambda_C38)

    def lambda_C49():

        label("loc_C49")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C49")

    QueueWorkItem2(0x16, 1, lambda_C49)

    def lambda_C5A():

        label("loc_C5A")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C5A")

    QueueWorkItem2(0x17, 1, lambda_C5A)

    def lambda_C6B():

        label("loc_C6B")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C6B")

    QueueWorkItem2(0x18, 1, lambda_C6B)

    def lambda_C7C():

        label("loc_C7C")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C7C")

    QueueWorkItem2(0x19, 1, lambda_C7C)

    def lambda_C8D():

        label("loc_C8D")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_C8D")

    QueueWorkItem2(0x1A, 1, lambda_C8D)

    def lambda_C9E():
        OP_8E(0xFE, 0xFFFFD058, 0xFA0, 0xFFFFA0A6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_C9E)
    Sleep(400)

    def lambda_CBE():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFFA0BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_CBE)
    Sleep(400)

    def lambda_CDE():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFF9C5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_CDE)
    Sleep(400)

    def lambda_CFE():
        OP_8E(0xFE, 0xFFFFD012, 0xFA0, 0xFFFF9C5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_CFE)
    Sleep(400)

    def lambda_D1E():
        OP_8E(0xFE, 0xFFFFD472, 0xFA0, 0xFFFF9782, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_D1E)
    Sleep(400)

    def lambda_D3E():
        OP_8E(0xFE, 0xFFFFCFEA, 0xFA0, 0xFFFF9782, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_D3E)
    WaitChrThread(0x10, 0x1)

    def lambda_D5E():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D5E)
    WaitChrThread(0x11, 0x1)

    def lambda_D71():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D71)
    WaitChrThread(0x10, 0x1)

    def lambda_D84():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D84)

    ChrTalk(    #7
        0x10,
        (
            "#110FSo how about it, Nial. Is this enough\x01",
            "to help you write a decent article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x13,
        (
            "#141F#4PY-You bet it is!\x02\x03",

            "I'm really grateful that you took\x01",
            "us along!\x02\x03",

            "#147FOh, and would you mind if we took\x01",
            "a picture of you while we're at it?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x14, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    TurnDirection(0x10, 0x12, 400)

    ChrTalk(    #9
        0x10,
        (
            "#113F#6PHmm...what do you think,\x01",
            "General Morgan?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(    #10
        0x12,
        (
            "#163F#4PDo as you like. This plan was\x01",
            "successful thanks to your genius.\x02\x03",

            "#160FIn all honesty, this is truly\x01",
            "something to boast about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#115F#6PNo, this was just the result of\x01",
            "the accuracy of the Intelligence\x01",
            "Division's analysis.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #12
        0x10,
        (
            "#4P#110FAnd thanks to the cooperation of\x01",
            "those of you standing over there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_101A():

        label("loc_101A")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_101A")

    QueueWorkItem2(0x10, 2, lambda_101A)

    def lambda_102B():

        label("loc_102B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_102B")

    QueueWorkItem2(0x14, 2, lambda_102B)

    def lambda_103C():

        label("loc_103C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_103C")

    QueueWorkItem2(0x13, 2, lambda_103C)

    def lambda_104D():

        label("loc_104D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_104D")

    QueueWorkItem2(0x11, 2, lambda_104D)

    def lambda_105E():

        label("loc_105E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_105E")

    QueueWorkItem2(0x12, 2, lambda_105E)
    Sleep(500)

    ChrTalk(    #13
        0x12,
        "#161F#4PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)

    def lambda_10AE():
        OP_6D(-14680, 4000, -23970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10AE)

    def lambda_10C6():

        label("loc_10C6")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10C6")

    QueueWorkItem2(0x101, 2, lambda_10C6)

    def lambda_10D7():

        label("loc_10D7")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10D7")

    QueueWorkItem2(0x102, 2, lambda_10D7)

    def lambda_10E8():

        label("loc_10E8")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10E8")

    QueueWorkItem2(0x103, 2, lambda_10E8)

    def lambda_10F9():

        label("loc_10F9")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_10F9")

    QueueWorkItem2(0x104, 2, lambda_10F9)

    def lambda_110A():
        OP_8E(0xFE, 0xFFFFCAA4, 0xFA0, 0xFFFFB0AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_110A)
    Sleep(100)

    def lambda_112A():
        OP_8E(0xFE, 0xFFFFC4AA, 0xFA0, 0xFFFFAEFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_112A)
    Sleep(100)
    SetChrFlags(0x102, 0x4)

    def lambda_114F():
        OP_8E(0xFE, 0xFFFFC7B6, 0xFA0, 0xFFFFB514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_114F)
    Sleep(100)

    def lambda_116F():
        OP_8E(0xFE, 0xFFFFC2FC, 0xFA0, 0xFFFFB3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_116F)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #14
        0x101,
        (
            "#505FUm... What are you guys...\x01",
            "I mean, how the heck...\x02\x03",

            "What's...going on, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x13,
        "#143FI-It's you kids again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14,
        "#151FHey, look! It's Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        "#162FB-Bracers?! Why are you here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#027FJust for the record, I'll tell you.\x01",
            "We infiltrated this place one step\x01",
            "ahead of you...again.\x02\x03",

            "And the entire hideout has been\x01",
            "subdued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FWe chased the fleeing sky bandit\x01",
            "leaders up this way...\x02\x03",

            "...but I never would have guessed\x01",
            "that the Royal Army's patrol ships\x01",
            "would be waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        (
            "#162FGrrr...\x01",
            "Once again you've overstepped\x01",
            "your bounds.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x12, 400)

    ChrTalk(    #21
        0x10,
        (
            "#115F#6PWith all due respect, General.\x02\x03",

            "It was because of them that our military\x01",
            "strike saw this level of success.\x02\x03",

            "#110FTherefore, shouldn't we in turn\x01",
            "recognize their achievements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "#163F...\x02\x03",

            "#160FDo as you wish. I'll leave the\x01",
            "rest up to your discretion.\x02\x03",

            "I'll return to the ship and see what\x01",
            "information I can get out of these\x01",
            "sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#110F#6PVery well, General.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x4)
    OP_8C(0x12, 180, 400)
    OP_43(0x12, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_8C(0x1A, 180, 400)
    OP_43(0x1A, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_8C(0x19, 180, 400)
    OP_43(0x19, 0x1, 0x0, 0x4)
    Sleep(300)

    ChrTalk(    #24
        0x101,
        "#007FThat old man's as stubborn as ever.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #25
        0x10,
        (
            "#4P#115FHe's not a bad person. He just\x01",
            "lacks a little flexibility.\x02\x03",

            "#112FThat aside, where are the other\x01",
            "sky bandits and the hostages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#020FThe other lackeys should be just lying\x01",
            "all over the place unconscious.\x02\x03",

            "And as for the hostages, we have\x01",
            "them waiting in the same room\x01",
            "they were imprisoned in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#4P#110FI see...\x02\x03",

            "You have done this nation a\x01",
            "great service.\x02\x03",

            "Please leave the transportation\x01",
            "of the hostages and cargo to us.\x02\x03",

            "Let's move, Captain Amalthea!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        "#182FYes, Colonel!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x11, 0x1, 0x0, 0x5)

    def lambda_17D5():

        label("loc_17D5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17D5")

    QueueWorkItem2(0x14, 1, lambda_17D5)

    def lambda_17E6():

        label("loc_17E6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17E6")

    QueueWorkItem2(0x13, 1, lambda_17E6)

    def lambda_17F7():

        label("loc_17F7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_17F7")

    QueueWorkItem2(0x101, 2, lambda_17F7)

    def lambda_1808():

        label("loc_1808")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1808")

    QueueWorkItem2(0x102, 2, lambda_1808)

    def lambda_1819():

        label("loc_1819")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1819")

    QueueWorkItem2(0x103, 2, lambda_1819)

    def lambda_182A():

        label("loc_182A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_182A")

    QueueWorkItem2(0x104, 2, lambda_182A)
    Sleep(500)
    OP_43(0x15, 0x1, 0x0, 0x5)
    Sleep(200)
    OP_43(0x16, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x18, 0x1, 0x0, 0x5)
    Sleep(200)
    OP_43(0x17, 0x1, 0x0, 0x5)
    Sleep(300)

    ChrTalk(    #29
        0x13,
        "#143FAh, wait for me, Colonel!\x02",
    )

    CloseMessageWindow()

    def lambda_1894():

        label("loc_1894")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_1894")

    QueueWorkItem2(0x101, 2, lambda_1894)

    def lambda_18A5():

        label("loc_18A5")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18A5")

    QueueWorkItem2(0x102, 2, lambda_18A5)

    def lambda_18B6():

        label("loc_18B6")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18B6")

    QueueWorkItem2(0x103, 2, lambda_18B6)

    def lambda_18C7():

        label("loc_18C7")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_18C7")

    QueueWorkItem2(0x104, 2, lambda_18C7)
    Sleep(1000)

    ChrTalk(    #30
        0x13,
        (
            "#141FI'd really like to interview you\x01",
            "kids, but this time the Colonel\x01",
            "is top-priority.\x02\x03",

            "But if we have another opportunity,\x01",
            "I'd appreciate doing one with you,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x14,
        "#151FSee you later, Estelle, Joshua!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    OP_43(0x13, 0x1, 0x0, 0x5)
    Sleep(700)
    OP_43(0x14, 0x1, 0x0, 0x5)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_1A15():
        OP_6D(-15060, 4000, -19760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A15)

    def lambda_1A2D():
        OP_6E(232, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A2D)
    Sleep(3000)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x103)
    OP_63(0x104)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    OP_20(0x5DC)
    Sleep(1000)
    Fade(1000)
    OP_6B(3010, 0)
    OP_0D()

    ChrTalk(    #32
        0x104,
        (
            "#035FMy, my, my. You had your whole shining\x01",
            "moment uprooted and stolen just like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#007F#6PYou got that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        (
            "#027F#4PDon't let it bother you, Estelle.\x02\x03",

            "The bracer's role has always been\x01",
            "that of the unsung hero.\x02\x03",

            "So there's no real reason for us\x01",
            "to stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#010FThat sounds about right, yeah.\x02\x03",

            "Dad always made a point of staying\x01",
            "in the background, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #36
        0x101,
        (
            "#505F#6PReally? I never noticed.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #37
        0x101,
        "#004F#3S#6PAh! Where IS Dad?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1C61():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C61)

    def lambda_1C6F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6F)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #38
        0x102,
        (
            "#015FHmm...I guess that's the one problem\x01",
            "we've still got to figure out.\x02\x03",

            "#013FWhere is Dad now?\x01",
            "What is he doing?\x02\x03",

            "And why hasn't he tried to contact\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#003F#6PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#026F#4PIt looks like there's nothing else\x01",
            "left for us to do here.\x02\x03",

            "In the meantime, let's get back to\x01",
            "Bose and report what happened\x01",
            "with the incident.\x02\x03",

            "#020FWe'll try and figure out what to\x01",
            "do about your dad after that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E21")
    OP_28(0x13, 0x4, 0x40)

    label("loc_1E21")

    OP_28(0x37, 0x4, 0x10)
    OP_28(0x39, 0x1, 0x100)
    OP_28(0x39, 0x1, 0x200)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_398 end

    def Function_4_1E4A(): pass

    label("Function_4_1E4A")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFD54E, 0xFD2, 0xFFFF71EE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE053, 0xFA0, 0xFFFF7162, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE003, 0x7D0, 0xFFFF809E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFAA, 0x0, 0xFFFF813E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_1E4A end

    def Function_5_1EA5(): pass

    label("Function_5_1EA5")

    OP_8E(0xFE, 0xFFFFBE38, 0xFA0, 0xFFFFAFB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBCC6, 0xFA0, 0xFFFFC22A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBD52, 0x2EE, 0xFFFFD634, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_1EA5 end

    SaveToFile()

Try(main)
