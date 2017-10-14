from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1511   ._SN',
        MapName             = 'Bose',
        Location            = 'T1511.x',
        MapIndex            = 1,
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
        'Scherazard',                           # 9
        'Agate',                                # 10
        'Olivier',                              # 11
        'Kloe',                                 # 12
        'Tita',                                 # 13
        'Zin',                                  # 14
        'Father Kevin',                         # 15
        'Sophina',                              # 16
        '皿',                                   # 17
        '皿',                                   # 18
        '皿',                                   # 19
        '皿',                                   # 20
        '皿',                                   # 21
        '皿',                                   # 22
        '皿',                                   # 23
        '皿',                                   # 24
        'グラス',                               # 25
        'グラス',                               # 26
        'グラス',                               # 27
        'グラス',                               # 28
        'グラス',                               # 29
        'グラス',                               # 30
        'グラス',                               # 31
        'グラス',                               # 32
        'Kurt',                                 # 33
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
        'ED6_DT07/CH00023 ._CH',             # 00
        'ED6_DT07/CH00053 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT07/CH00043 ._CH',             # 03
        'ED6_DT07/CH00063 ._CH',             # 04
        'ED6_DT07/CH00073 ._CH',             # 05
        'ED6_DT27/CH03083 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH00020 ._CH',             # 08
        'ED6_DT07/CH00050 ._CH',             # 09
        'ED6_DT07/CH00030 ._CH',             # 0A
        'ED6_DT07/CH00040 ._CH',             # 0B
        'ED6_DT07/CH00060 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT27/CH03080 ._CH',             # 0E
        'ED6_DT27/CH03003 ._CH',             # 0F
        'ED6_DT06/CH20020 ._CH',             # 10
        'ED6_DT06/CH20021 ._CH',             # 11
        'ED6_DT26/CH20403 ._CH',             # 12
        'ED6_DT26/CH20373 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH00053P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT07/CH00043P._CP',             # 03
        'ED6_DT07/CH00063P._CP',             # 04
        'ED6_DT07/CH00073P._CP',             # 05
        'ED6_DT27/CH03083P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH00020P._CP',             # 08
        'ED6_DT07/CH00050P._CP',             # 09
        'ED6_DT07/CH00030P._CP',             # 0A
        'ED6_DT07/CH00040P._CP',             # 0B
        'ED6_DT07/CH00060P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT27/CH03080P._CP',             # 0E
        'ED6_DT27/CH03003P._CP',             # 0F
        'ED6_DT06/CH20020P._CP',             # 10
        'ED6_DT06/CH20021P._CP',             # 11
        'ED6_DT26/CH20403P._CP',             # 12
        'ED6_DT26/CH20373P._CP',             # 13
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 262161,
        ChipIndex           = 0x11,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
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
        Unknown3            = 262161,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_46A",          # 00, 0
        "Function_1_49C",          # 01, 1
        "Function_2_49D",          # 02, 2
        "Function_3_24B6",         # 03, 3
        "Function_4_4B82",         # 04, 4
        "Function_5_4C0B",         # 05, 5
    )


    def Function_0_46A(): pass

    label("Function_0_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_484")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_49B")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_49B")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_49B")

    Return()

    # Function_0_46A end

    def Function_1_49C(): pass

    label("Function_1_49C")

    Return()

    # Function_1_49C end

    def Function_2_49D(): pass

    label("Function_2_49D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B0")
    Call(0, 4)

    label("loc_4B0")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0xE, 15900, 250, 11150, 180)
    SetChrPos(0x101, 17150, 200, 9830, 270)
    SetChrPos(0xB, 14800, 200, 9950, 90)
    SetChrPos(0xC, 17300, 200, 8480, 270)
    SetChrPos(0x8, 14840, 200, 8410, 90)
    SetChrPos(0x9, 17340, 200, 6860, 270)
    SetChrPos(0xA, 14850, 200, 6940, 90)
    SetChrPos(0xD, 15940, 200, 5490, 0)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xE, 6)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x9, 2)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xA, 1)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x10, 15970, 800, 10210, 0)
    SetChrPos(0x11, 16440, 800, 9370, 0)
    SetChrPos(0x12, 15700, 800, 9540, 0)
    SetChrPos(0x13, 16440, 800, 8109, 0)
    SetChrPos(0x14, 15700, 800, 8390, 0)
    SetChrPos(0x15, 16440, 800, 6900, 0)
    SetChrPos(0x16, 15700, 800, 7140, 0)
    SetChrPos(0x17, 15900, 800, 6260, 0)
    SetChrPos(0x18, 15430, 800, 10100, 0)
    SetChrPos(0x19, 16190, 800, 9880, 0)
    SetChrPos(0x1A, 15550, 800, 7940, 0)
    SetChrPos(0x1B, 15690, 800, 9110, 0)
    SetChrPos(0x1C, 16260, 800, 8610, 0)
    SetChrPos(0x1D, 16400, 800, 7350, 0)
    SetChrPos(0x1E, 15580, 800, 6670, 0)
    SetChrPos(0x1F, 16300, 800, 6360, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(16750, 200, 8800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(17040, 0, 9760, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x1D, 0x4)
    OP_72(0x1E, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xE,
        (
            "#1065F#3PYowwww. Sounds like things got, uh,\x01",
            "kinda crazy.\x02\x03",

            "So there really was an ancient dragon nestin'\x01",
            "in Liberl?\x02\x03",

            "#1067FAnd it warned about the Aureole before\x01",
            "flying off, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1007F#4PYeah. Makes my head spin just thinking\x01",
            "about everything that happened.\x02\x03",

            "#1015FWhat I really don't get is why Ragnard\x01",
            "couldn't tell us anything about the Aureole,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xE,
        (
            "#1060F#3PActually, there is a line in the Testaments\x01",
            "this reminds me of.\x02\x03",

            "#1065F'And the Goddess, having bequeathed Her\x01",
            "Treasures, sent forth the Holy Beasts to\x01",
            "observe the path the children of Men would take.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "#043F#3PA 'Holy Beast'...\x02\x03",

            "That certainly does seem like Ragnard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#035F#2PThe more pertinent point, I feel,\x01",
            "is the command to 'observe.'\x02\x03",

            "#030FThey may simply watch over us,\x01",
            "and were commanded to not interfere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "#053F#2PHmph. Load of help that is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xE,
        (
            "#1060F#3PWell, one way or another, I sure think this\x01",
            "makes it look like the Aureole exists!\x02\x03",

            "Think we can even start to piece things\x01",
            "together, thanks to what I've found in my\x01",
            "pokin' around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1002F#4PRight, you were investigating the towers.\x02\x03",

            "Did you find anything out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xE,
        (
            "#1065F#3PA little bit, yeah.\x02\x03",

            "#1063FI think you guys are familiar with those weird\x01",
            "machines at the top of each tower, right?\x02\x03",

            "Didja know they're currently glowing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D85")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as confirmed that the devices are operating\x01",          # 0
            "Set as not confirmed that the devices are operating\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D67"),
        (1, "loc_D76"),
        (SWITCH_DEFAULT, "loc_D85"),
    )


    label("loc_D67")

    OP_29(0x66, 0x1, 0x1000)
    OP_29(0x66, 0x1, 0x2000)
    Jump("loc_D85")

    label("loc_D76")

    OP_28(0x66, 0x2, 0x1000)
    OP_28(0x66, 0x2, 0x2000)
    Jump("loc_D85")

    label("loc_D85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E20")

    ChrTalk(    #9
        0x101,
        (
            "#1015F#4PYeah, I remember seeing that one was all lit up.\x02\x03",

            "I don't, uh, quite get what that has to\x01",
            "do with the Aureole, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC0")

    label("loc_E20")


    ChrTalk(    #10
        0x101,
        (
            "#1004F#4POh, yeah! The Amberl Tower was shining when\x01",
            "we hunted monsters there.\x02\x03",

            "#1015FI don't, uh, quite get what that has to do\x01",
            "with the Aureole, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC0")


    ChrTalk(    #11
        0xE,
        (
            "#1063F#3PWell, Captain Schwarz mentioned something to me.\x02\x03",

            "Something weird happened in that room where\x01",
            "you fought Alan Richard just before that\x01",
            "mechanical monster showed up, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1004F#4POh, yeah...\x02\x03",

            "#1015FIf I remember right, after the Gospel was used,\x01",
            "all the lights in the ruins went out...\x02\x03",

            "And then there was this voice out of nowhere\x01",
            "giving a warning, and the pillars all sunk\x01",
            "into the floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#022F#2PRight... The warning was about the 'first\x01",
            "barrier' being 'no longer operative' and the\x01",
            "'device towers' being enabled, as I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "#1060F#3PYeah, that's what I've heard.\x02\x03",

            "#1065FSo on a hunch, I double-checked the timing\x01",
            "with some witnesses...\x02\x03",

            "#1063FThose four towers started lighting up and\x01",
            "stuff at the same time the Gospel was used.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1005F#4PYou're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "#065F#4PS-So the device towers the warning\x01",
            "mentioned are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        (
            "#072F#2PThe four towers of Liberl and the\x01",
            "machines at their peaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        (
            "#1065F#3PI don't got any other explanation,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#035F#2PSo to sum up, then...\x02\x03",

            "#030F...the ruins beneath Grancel Castle are what\x01",
            "produces this 'first barrier.'\x02\x03",

            "However, when Colonel Richard used the Gospel,\x01",
            "this 'barrier' was eliminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#047F#3PAnd, in its place, the device\x01",
            "towers were activated.\x02\x03",

            "#042FPresumably to produce a second barrier\x01",
            "of some sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1002F#4PA 'second' barrier?\x01",
            "But why would you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#053F#2PIf you're gonna protect somethin', you always\x01",
            "want to make sure you have a backup.\x02\x03",

            "#552FDoesn't answer the questions of what kinda\x01",
            "barrier is it, or what the hell is it a\x01",
            "barrier for, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xE,
        (
            "#1065F#3PAbout that.\x02\x03",

            "#1063FI'm startin' to think it's something to\x01",
            "hide the location of the Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x101, 2)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    Sleep(60)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xC, 2)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xB, 1)
    Sleep(60)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x9, 2)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x101,
        (
            "#1020F#4PThat's right! The Aureole wasn't in the\x01",
            "castle's ruins.\x02\x03",

            "But it's still supposed to be somewhere\x01",
            "in Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xE,
        (
            "#1060F#3PExactly.\x02\x03",

            "#1065FAnd if we assume the society's goal is to\x01",
            "obtain the Aureole...\x02\x03",

            "#1063FThen I think we can say their 'experiments'\x01",
            "are part of a plan to further that goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1007F#4PThey need to do all that just to...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#035F#2PThe experiments, the Gospels, and the Aureole...\x02\x03",

            "Heh, it seems they are more tightly interwoven\x01",
            "than we first believed.\x02\x03",

            "#030FAnd the one sitting at the loom would be this\x01",
            "man called the 'professor.'\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)

    ChrTalk(    #28
        0x101,
        (
            "#1007F#4PYeah, it's all him.\x02\x03",

            "#1002FThe same guy who put the Gospel on Ragnard's\x01",
            "head and made him attack Bose.\x02\x03",

            "And the one...who...\x02\x03",

            "#1003F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        "#064F#4PEstelle?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 1)
    Sleep(100)

    ChrTalk(    #30
        0xE,
        (
            "#1064F#3PUh, what's up, Estelle?\x01",
            "You got awfully quiet all of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(100)

    ChrTalk(    #31
        0x101,
        (
            "#1002F#4PYeah... About this 'professor.'\x02\x03",

            "I think he's the one who made Joshua leave\x01",
            "in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "#043F#3PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#022F#2PWait a moment...\x02\x03",

            "You mean he's the one who orchestrated the\x01",
            "events that brought Joshua into your home?\x01",
            "And then made him leave the way he did?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(100)

    ChrTalk(    #34
        0x101,
        (
            "#1003F#6PI think so...\x02\x03",

            "#1010FAnd I bet he's the one who manipulated\x01",
            "Colonel Richard and Kurt's memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        "#052F#2PYou're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "#072F#2PHmm. We do not have an explanation for\x01",
            "Kurt's memories, it is true.\x02\x03",

            "Why do you think this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1026F#6PWell...you see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05Estelle explained that she can't remember the identity of\x01",
            "one man she met the day Joshua disappeared.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #39
        0x8,
        "#022F#2PThat really happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#555F#2PIs this another thing you've been trying to\x01",
            "shoulder all by yourself or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1025F#6PUm, not exactly, but...\x02\x03",

            "#1007FSorry, I guess it's kind of late to\x01",
            "bring it up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "#042F#3PI don't think there can be any doubt\x01",
            "at this point, though.\x02\x03",

            "It's safe to say that this person must be\x01",
            "the one responsible for all our trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "#032F#2PHm. He is clearly a man of twisted morals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        "#074F#2PYes... We'll need to be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        "#063F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1025F#6PAwww. Sorry, Tita.\x02\x03",

            "I didn't mean to bring up all this serious\x01",
            "junk when we came out here to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "#560F#4POh, no, no, it's okay, Estelle!\x02\x03",

            "#561FIt's just, I was wondering why someone\x01",
            "would do things like this...\x02\x03",

            "Make everyone so unhappy,\x01",
            "make Joshua suffer...\x02\x03",

            "I just...don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#6PAww, Tita, don't worry about trying to\x01",
            "understand a weirdo like that, okay?\x02\x03",

            "#1006FYou just need to worry about being Tita!\x02\x03",

            "Right, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#055F#2PWhy the hell do you keep dragging me into\x01",
            "these conversations?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 2)
    Sleep(100)

    ChrTalk(    #50
        0xB,
        "#041F#3PHahaha!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(100)

    ChrTalk(    #51
        0x8,
        "#027F#5PAhhh... We needed that, I think.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    Sleep(100)

    ChrTalk(    #52
        0xE,
        "#1067F#3P...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #53
        0x101,
        "#1015F#4PMm? Kevin?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(75)
    SetChrSubChip(0xB, 1)
    Sleep(100)

    ChrTalk(    #54
        0xE,
        (
            "#1060F#3POh, nothin'.\x02\x03",

            "#1061FSo howsabout we call that enough\x01",
            "information swappin' for one day?\x02\x03",

            "It'd be a crime to let all this wonderful\x01",
            "food go to waste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1006F#4PCan't say no to that!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(50)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    SetChrSubChip(0xC, 0)
    Sleep(50)
    SetChrSubChip(0x9, 0)
    Sleep(100)

    ChrTalk(    #56
        0xA,
        (
            "#037F#2PYes, let us leave debate aside for now.\x02\x03",

            "Instead let us navigate the forests of meat\x01",
            "through the rivers of liquor! Merriment awaits!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x8,
        "#021F#5PRIVERS of liquor, Lenheim?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0xA,
        (
            "#034F#2PThat was...an unfortunate metaphor.\x01",
            "Oh, please, Schera, do not make me swim!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05And so Estelle and her friends set about\x01",
            "enjoying their holiday.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_2_49D end

    def Function_3_24B6(): pass

    label("Function_3_24B6")

    EventBegin(0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x20, 0x2)
    SetChrPos(0x20, 49000, -100, 22700, 180)
    SetChrChipByIndex(0x20, 18)
    SetChrSubChip(0x20, 0)
    OP_6F(0x1B, 11)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x101, 50500, 0, 21820, 270)
    SetChrPos(0xE, 50500, 0, 22640, 270)
    SetChrPos(0x8, 50560, 0, 23630, 225)
    SetChrPos(0xA, 50120, 0, 25120, 180)
    SetChrPos(0x9, 48850, 0, 24330, 180)
    SetChrPos(0xB, 51170, 0, 24660, 225)
    SetChrPos(0xC, 49770, -100, 24140, 180)
    SetChrPos(0xD, 48990, 0, 25290, 180)
    SetChrChipByIndex(0x8, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0xB, 11)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6D(51790, 0, 24790, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)
    OP_6D(56510, 0, 29350, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)

    def lambda_2641():
        OP_6D(51790, 0, 24790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2641)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #60
        0xE,
        (
            "#1065F#2PI patched him up as best I can,\x01",
            "but his wounds're pretty serious.\x02\x03",

            "#1063FHe'll have to stay bed-bound for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1026F#2PPoor Kurt...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#552F#5PNever thought I'd see the day where KURT\x01",
            "gets thrashed like this.\x02\x03",

            "The hell happened...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1002F#2PKurt and his team were really close to finding\x01",
            "the society's base, from what Lugran told us.\x02\x03",

            "Which means Anelace and Carna and Grant\x01",
            "should have been wi--\x02\x03",

            "#1020FOh, no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "#572F#3PThis is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#022F#6PI called Lugran on the inn's phone.\x02\x03",

            "He's contacting the other branches and\x01",
            "the Royal Army now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1020F#2PBut, but...!\x02\x03",

            "If things've gone wrong,\x01",
            "Anelace and the others'll...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#020F#6PWe know, we know. Don't panic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#053F#5PWe need to get out there and do what we can.\x02\x03",

            "#555FProblem is, where the hell did Kurt's boat\x01",
            "float in from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#032F#6PHmm. It is curious.\x01",
            "Valleria Lake has no islands or reefs, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#043F#6PThat's right. It's tremendously deep, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#035F#6PSo it must have floated in from another shore.\x02\x03",

            "It could be very hard to divine precisely which\x01",
            "shore, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1007F#2PYeah... The lake is huge.\x02\x03",

            "#1015FI guess we could ask the army patrol\x01",
            "ships to help too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x20,
        "#847FNnngh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x101,
        "#1004F#2PKurt?!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x20, 1)
    Sleep(300)
    SetChrSubChip(0x20, 2)
    Sleep(1500)
    SetChrSubChip(0x20, 3)
    Sleep(1000)

    ChrTalk(    #75
        0x20,
        (
            "#844FAh... This is...\x02\x03",

            "Estelle... Ah, and Agate...everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "#556F#5PThis is the Kingfisher Inn,\x01",
            "on the lakeshore in Bose.\x02\x03",

            "You drifted here on the waves,\x01",
            "you tough old goat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x20,
        (
            "#844FThe Kingfisher... Yes, I see...\x02\x03",

            "#843FI remember my teammates and I infiltrating\x01",
            "the society's base...\x02\x03",

            "And then...then I... I...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0xFFFFFE70, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #78
        0x101,
        "#1020F#2PKurt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#023F#6PDon't tell me...\x02",
    )

    CloseMessageWindow()
    OP_63(0x20)
    Sleep(500)

    ChrTalk(    #80
        0x20,
        (
            "#844FKh... DAMN it all!\x02\x03",

            "To have my memory stolen not once,\x01",
            "but TWICE! Agh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1002F#2PI knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "#032F#6PThe society has intruded upon\x01",
            "your mind once again...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 2)
    Sleep(500)

    ChrTalk(    #83
        0x20,
        (
            "#842FZin, please!\x02\x03",

            "Use your chi on me as you did last time!\x02\x03",

            "Otherwise, everyone else will...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xD,
        (
            "#572F#3PLast time was...a desperate improvisation.\x02\x03",

            "It won't be able to restore memories locked\x01",
            "away by hypnosis.\x02\x03",

            "#074FBesides, with your injuries... No.\x01",
            "We cannot risk it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x20,
        "#844FBut...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        "#1060F#2PIn that case, let ME try somethin'.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_30A3():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30A3)

    def lambda_30B1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_30B1)
    Sleep(100)

    def lambda_30C4():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30C4)

    def lambda_30D2():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_30D2)
    Sleep(400)

    ChrTalk(    #87
        0x101,
        "#1004F#2PBwuh?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 3)
    Sleep(500)

    ChrTalk(    #88
        0x20,
        "#842F...And you are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "#1060F#2PKevin Graham, Gralsritter of the church.\x02\x03",

            "Think Anelace might have told you 'bout me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x20,
        "#841FAh... Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1015F#2PH-Hang on a sec, Kevin.\x01",
            "You can undo hypnosis?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#1071F#2PWell...dunno what I could do about any nasty\x01",
            "stuff that's wormed its way into the subconscious.\x01",
            "Buuuuuut...\x02\x03",

            "I think I can manage a little somethin' if\x01",
            "it's just some kind of block on his short-term\x01",
            "memory.\x02\x03",

            "#1062FDoesn't seem like it's been that long since\x01",
            "he was hit, so!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1025F#2POh, neat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "#032F#6PHm. Is this an example of Thaumaturgy,\x01",
            "the secret arts of the church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        (
            "#1061F#2PYou might call it that.\x02\x03",

            "#1060FThis, uh, might feel like your head's\x01",
            "gettin' kicked by a mule. Repeatedly.\x02\x03",

            "I'm guessing you don't care much, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x20,
        "#842FNot at all. Please, do what you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        "#1065F#2PAll right.\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    Fade(500)
    SetChrChipByIndex(0xE, 19)
    SetChrSubChip(0xE, 0)
    OP_21()
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xE, 1)
    Sleep(1000)

    ChrTalk(    #98
        0xE,
        (
            "#1063F#2PIn the name of She Who Dwells Above do I hold\x01",
            "this consecrated septium.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x21)
    Sleep(500)

    def lambda_34D8():
        OP_6B(2600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34D8)

    def lambda_34E8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34E8)

    def lambda_34F6():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34F6)
    Sleep(50)

    def lambda_3509():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3509)

    def lambda_3517():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3517)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp082_00.eff")
    PlayEffect(0x1, 0x0, 0xE, -450, 800, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #99
        0x101,
        "#1004F#2P(Wow...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        "#560F#5P(So pretty!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        (
            "#1065F#2PSilver reflection of the conscious will,\x01",
            "black luminance of time's flow...\x02\x03",

            "By your opposing natures, I divest this\x01",
            "mortal man of the ties which bind\x01",
            "his mind!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 50020, 900, 22900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    SetChrSubChip(0x20, 3)
    Sleep(100)
    SetChrSubChip(0x20, 4)
    Sleep(100)
    SetChrSubChip(0x20, 5)

    ChrTalk(    #102
        0x20,
        "#847FNNNGH!\x02",
    )

    OP_9E(0x20, 0x14, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1020F#2PKURT! You okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x20,
        (
            "#847FYes, I...think. I think so.\x02\x03",

            "...So much is returning.\x01",
            "As though a mist is clearing from my mind...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xE, 14)
    SetChrSubChip(0xE, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #105
        0xE,
        (
            "#1063F#2PJust let the fog clear, and remain calm\x01",
            "and relaxed.\x02\x03",

            "Whatever you do, don't try to look into the\x01",
            "darkness that lies beyond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x20,
        (
            "#843FYes, I understand.\x02\x03",

            "Hah... I see what you meant when you warned\x01",
            "me this would be unpleasant.\x02\x03",

            "That is...my ego, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        "#1064F#2PYou can tell? I'm surprised!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x20,
        (
            "#843FI am proficient in meditation, remember...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 5)
    Sleep(300)
    SetChrSubChip(0x20, 4)
    Sleep(300)
    SetChrSubChip(0x20, 3)
    Sleep(1000)

    ChrTalk(    #109
        0x20,
        "#845F...I'm fine. I think I remember enough now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1025F#2PReally? Great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        "#070F#3PHmmm. An impressive technique.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "#051F#5PHeh, you really are more than just a\x01",
            "skirt-chasin' priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        "#021F#6PWell done, Kevin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#1061F#2PHahaha! C'mon, don't inflate my ego TOO much,\x01",
            "here! I mean, a little, sure, but not too much.\x02\x03",

            "#1063FAnyhow... Kurt!\x01",
            "What do you remember, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x20,
        (
            "#843FYes. Well...\x02\x03",

            "#842FThe society has a base on the northwestern\x01",
            "shore of the lake.\x02\x03",

            "They've built some kind of research facility\x01",
            "in secret...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1020F#2PA RESEARCH FACILITY?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#022F#6PWhen did they...?\x01",
            "How did they...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#043F#6PThe northwestern parts of the lakeshore\x01",
            "are sparsely populated at best...\x02\x03",

            "Even so, guard airships do patrol over\x01",
            "the area. I don't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x20,
        (
            "#843FThe facility is cleverly hidden.\x02\x03",

            "They project a dummy image into the sky\x01",
            "to prevent aerial scouting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1005F#2PWHAAAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        "#034F#6PWell, that is...an impressive feat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "#065F#5PI-It's theoretically POSSIBLE, but\x01",
            "how would you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x20,
        (
            "#844FAnd if you approach by land...\x02\x03",

            "A deep fog springs up around you\x01",
            "as you draw near.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#042F#6PA fog!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#552F#5PSounds just like Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x20,
        (
            "#843FWe broke through the fog and entered the facility.\x02\x03",

            "But then...we were ambushed by a team\x01",
            "of people calling themselves 'Enforcers.'\x02\x03",

            "#844FThey caught us completely off guard\x01",
            "and crushed us almost immediately.\x02\x03",

            "I lost consciousness not long after\x01",
            "reaching the boat...\x02\x03",

            "#847F...DAMN my cowardice! Abandoning\x01",
            "Grant and Carna and Anelace like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1006F#2PKurt, don't worry about it, okay?\x02\x03",

            "We're going to save Anelace and all the rest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x20,
        "#842FEstelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "#051F#5PHeh, don't worry, Kurt. You told us everything\x01",
            "we need to know to go kick some fools around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#020F#6PYes. On top of that, I suspect we'll\x01",
            "have some help from the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        "#070F#3PLeave the rest to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x20,
        (
            "#845FThank you.\x02\x03",

            "#847FForgive me... I leave it in your...hands...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 4)
    Sleep(300)
    SetChrSubChip(0x20, 5)
    Sleep(200)
    SetChrSubChip(0x20, 6)
    Sleep(200)
    SetChrSubChip(0x20, 7)
    Sleep(1000)

    ChrTalk(    #133
        0x101,
        "#1020F#2PK-KURT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        (
            "#1065F#2PDon't worry, he's just unconscious.\x02\x03",

            "#1063FAnyway. Sounds like we don't have\x01",
            "time to stand around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1005F#2PRight!\x02\x03",

            "We need to get going before the army does!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0xB, 0x101, 400)
    Sleep(200)

    ChrTalk(    #136
        0x8,
        (
            "#022F#6PEstelle, I'm sure I don't need\x01",
            "to tell you this, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #137
        0x101,
        (
            "#1003F#2PYeah... I know.\x02\x03",

            "This is going to be the most dangerous thing\x01",
            "we've ever done. By a lot.\x02\x03",

            "#1002FBut you know what? I was prepared to\x01",
            "settle things with the society one way or\x01",
            "another.\x02\x03",

            "It'll just happen sooner than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#023F#6PEstelle...\x02\x03",

            "#524FWell...I think that was the shortest\x01",
            "vacation in history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#051F#5PNah, we got plenty of rest.\x02\x03",

            "Now it's time to gear up for the real fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        (
            "#074F#3PThere is a problem...\x01",
            "A small army of us going together would\x01",
            "stand out too much.\x02\x03",

            "#070FIt would be best to send a smaller group,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1006F#2PYeah, good idea.\x02\x03",

            "#1015FHey, everyone?\x02\x03",

            "Do you mind if I pick a team like I did\x01",
            "back in the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#020F#6PAs you did beneath Grancel?\x01",
            "I think that's for the best.\x01",
            "I'll be happy to come along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xD,
        "#070F#3PSure, I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        (
            "#051F#5PI won't hold any grudges if you don't pick me...\x01",
            "though I do wanna bust some heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xA,
        (
            "#031F#6POf course! Though you will,\x01",
            "naturally, ask me to come along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "#048F#6PIf you need someone who can heal injuries,\x01",
            "I will be happy to come along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        (
            "#062F#5PI, um, I can help with machines and stuff,\x01",
            "I think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1025F#2PThanks, guys...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #149
        0xE,
        (
            "#1068F#1PEr, sorry to spoil the fun, buuuuut...\x02\x03",

            "#1060FD'you mind picking me first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "#1063F#1PFrom the sounds of it, Anelace and your\x01",
            "friends are in the society's claws.\x02\x03",

            "If they've been given the same treatment Kurt\x01",
            "was, or worse, what'll you guys do, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1020F#2POh...uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        "#070F#3PI see. A good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "#051F#5PYeah, good point.\x01",
            "Looks like you're in no matter\x01",
            "what, Mister Priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        "#1061F#1PHeheh, thank ya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1016F#2PWe should be thanking you, Kevin.\x02\x03",

            "#1006FOkay. Let me pick the rest of the team.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)

    label("loc_48D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B59")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #157
        (
            "\x06\x18\x07\x05You may now reconfigure your party.\x01",
            "Swap party members and their gear in and out\x01",
            "as needed, and select 'move out' when ready.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Form Party\x01",            # 0
            "Change Equipment\x01",      # 1
            "Move Out\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A56")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #158
        (
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from\x01",
            "the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_4B56")

    label("loc_4A56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4A8F")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_4ABB")

    label("loc_4A8F")


    AnonymousTalk(    #159
        "\x07\x05Please form your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_4ABB")

    Jump("loc_4B56")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B2A")
    SetChrName("")

    AnonymousTalk(    #160
        "\x06\x18\x07\x05Are you ready to continue?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B27")
    Jump("loc_4B59")

    label("loc_4B27")

    Jump("loc_4B56")

    label("loc_4B2A")


    AnonymousTalk(    #161
        "\x07\x05Please form your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_4B59")

    OP_69(0x0, 0x0)
    SetMapFlags(0x1)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_31(0xFF, 0xFE, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0901   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_4B56")

    Jump("loc_48D4")

    # Function_3_24B6 end

    def Function_4_4B82(): pass

    label("Function_4_4B82")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BFE"),
        (1, "loc_4C04"),
        (SWITCH_DEFAULT, "loc_4C0A"),
    )


    label("loc_4BFE")

    OP_A2(0x1200)
    Jump("loc_4C0A")

    label("loc_4C04")

    OP_A2(0x1201)
    Jump("loc_4C0A")

    label("loc_4C0A")

    Return()

    # Function_4_4B82 end

    def Function_5_4C0B(): pass

    label("Function_5_4C0B")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_5_4C0B end

    SaveToFile()

Try(main)
