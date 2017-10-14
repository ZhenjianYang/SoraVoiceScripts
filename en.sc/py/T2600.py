from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2600   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'Academy - Back Road',                  # 9
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
        'ED6_DT27/CH03001 ._CH',             # 00
        'ED6_DT27/CH03011 ._CH',             # 01
        'ED6_DT27/CH03091 ._CH',             # 02
        'ED6_DT27/CH03131 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03001P._CP',             # 00
        'ED6_DT27/CH03011P._CP',             # 01
        'ED6_DT27/CH03091P._CP',             # 02
        'ED6_DT27/CH03131P._CP',             # 03
    )

    DeclNpc(
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1600,
        Y                   = 1000,
        Z                   = 9950,
        Range               = 1600,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x20E4,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 33200,
        TriggerZ            = 0,
        TriggerY            = 14520,
        TriggerRange        = 1000,
        ActorX              = 32570,
        ActorZ              = 0,
        ActorY              = 14530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_12E",          # 00, 0
        "Function_1_142",          # 01, 1
        "Function_2_18D",          # 02, 2
        "Function_3_2C7",          # 03, 3
        "Function_4_5EB",          # 04, 4
        "Function_5_640",          # 05, 5
        "Function_6_698",          # 06, 6
        "Function_7_6DC",          # 07, 7
        "Function_8_720",          # 08, 8
        "Function_9_764",          # 09, 9
    )


    def Function_0_12E(): pass

    label("Function_0_12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_141")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_141")

    Return()

    # Function_0_12E end

    def Function_1_142(): pass

    label("Function_1_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154")
    OP_6F(0x2, 0)
    Jump("loc_15B")

    label("loc_154")

    OP_6F(0x2, 60)

    label("loc_15B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_177")
    Jump("loc_18C")

    label("loc_177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_18C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_18C")

    Return()

    # Function_1_142 end

    def Function_2_18D(): pass

    label("Function_2_18D")

    OP_EA(0x2, 0xFD, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1340)
    Jump("loc_2B5")

    label("loc_283")


    AnonymousTalk(    #1
        "\x07\x05The chest stares back at you, judging you.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2B5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_18D end

    def Function_3_2C7(): pass

    label("Function_3_2C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x10A, 0x40)
    SetChrFlags(0x10E, 0x40)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x10A, 0x4)
    SetChrFlags(0x10E, 0x4)
    SetChrPos(0x102, 29770, 0, 14350, 0)
    SetChrPos(0x101, 29770, 0, 14350, 0)
    SetChrPos(0x10A, 29770, 0, 14350, 0)
    SetChrPos(0x10E, 29770, 0, 14350, 0)
    OP_6D(-210, 0, 1470, 0)
    OP_67(0, 12190, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    OP_11(0x44, 0x42, 0x79, 0x9B14, 0x15F2C, 0x0)
    OP_43(0x102, 0x2, 0x0, 0x4)
    FadeToBright(1000, 0)

    def lambda_3B7():
        OP_6D(24700, 0, 13240, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B7)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_11(0x44, 0x42, 0x79, 0x9B14, 0x124F8, 0x0)
    OP_6D(25650, 0, 15090, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_43(0x10A, 0x1, 0x0, 0x7)
    Sleep(1000)
    OP_43(0x10E, 0x1, 0x0, 0x8)
    WaitChrThread(0x10E, 0x1)
    OP_44(0x102, 0x2)
    OP_DC()

    ChrTalk(    #2
        0x101,
        "#1002F#5PIt's begun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        "#812F#6PYeah, we gotta hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1035F#5PI unlocked the back gate\x01",
            "when I was here earlier.\x02\x03",

            "#1040FIt should open easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10E,
        (
            "#843F#6PVery good.\x02\x03",

            "#842FWe should infiltrate each building swiftly\x01",
            "and rescue the hostages in each.\x02\x03",

            "Remember to check off those rescued\x01",
            "from our list in the notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1005F#5PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        "#816F#6PLet's go!\x02",
    )

    CloseMessageWindow()
    OP_28(0xC0, 0x1, 0x4)
    OP_28(0xC0, 0x1, 0x8)
    OP_28(0xC0, 0x1, 0x10)
    OP_28(0xC0, 0x1, 0x20)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_3_2C7 end

    def Function_4_5EB(): pass

    label("Function_4_5EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F")
    OP_22(0x235, 0x0, 0x3C)
    Sleep(1500)
    OP_23(0x235)
    Sleep(500)
    OP_22(0x235, 0x0, 0x3C)
    Sleep(1900)
    OP_23(0x235)
    Sleep(700)
    OP_22(0x235, 0x0, 0x3C)
    Sleep(1700)
    OP_23(0x235)
    Sleep(600)
    OP_22(0x235, 0x0, 0x3C)
    Sleep(2000)
    OP_23(0x235)
    Sleep(800)
    Jump("Function_4_5EB")

    label("loc_63F")

    Return()

    # Function_4_5EB end

    def Function_5_640(): pass

    label("Function_5_640")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 1)
    SetChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0x6888, 0x0, 0x380E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5CE4, 0x0, 0x380E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_640 end

    def Function_6_698(): pass

    label("Function_6_698")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 0)
    SetChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0x609A, 0x0, 0x3430, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_698 end

    def Function_7_6DC(): pass

    label("Function_7_6DC")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 2)
    SetChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0x61B2, 0x0, 0x3BC4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_6DC end

    def Function_8_720(): pass

    label("Function_8_720")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 3)
    SetChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0x6590, 0x0, 0x38A4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_720 end

    def Function_9_764(): pass

    label("Function_9_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3")

    ChrTalk(    #8
        0x101,
        (
            "#1002F(We can't waste any time.\x01",
            "Let's hurry to the academy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C3")

    label("loc_7C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810")

    ChrTalk(    #9
        0x102,
        (
            "#1042F(We're short on time.\x01",
            "Let's hurry to the academy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C3")

    label("loc_810")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")

    ChrTalk(    #10
        0x10A,
        (
            "#816F(We don't have any reason to stop\x01",
            "here. Let's hurry to the academy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C3")

    label("loc_86E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C3")

    ChrTalk(    #11
        0x10E,
        (
            "#842F(We don't have any business here.\x01",
            "Let's hurry to the academy.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C3")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_8E3")

    Return()

    # Function_9_764 end

    SaveToFile()

Try(main)
