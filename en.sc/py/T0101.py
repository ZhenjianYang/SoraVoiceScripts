from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0101   ._SN',
        MapName             = 'rolent',
        Location            = 'T0101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0101_1 ._SN',
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
        'Tita',                                 # 10
        'Kloe',                                 # 11
        'Olivier',                              # 12
        'Agate',                                # 13
        "Rolent - Mayor's Residence",           # 14
        'Rolent Landing Port',                  # 15
        'Elize Highway',                        # 16
        'Milch Main Road',                      # 17
        'Malga Trail',                          # 18
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT06/CH20038 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT06/CH20038P._CP',             # 05
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
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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

    DeclNpc(
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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

    DeclNpc(
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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

    DeclNpc(
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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

    DeclNpc(
        X                   = 28060,
        Z                   = 0,
        Y                   = 80870,
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
        X                   = 43240,
        Y                   = -50,
        Z                   = 11610,
        Range               = 54840,
        Unknown_10          = 0x79E,
        Unknown_14          = 0x317E,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 18140,
        Y                   = -50,
        Z                   = 36360,
        Range               = 19090,
        Unknown_10          = 0x79E,
        Unknown_14          = 0xAF14,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 25210,
        Y                   = -50,
        Z                   = 70360,
        Range               = 30660,
        Unknown_10          = 0x79E,
        Unknown_14          = 0x11828,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_42A",          # 00, 0
        "Function_1_47D",          # 01, 1
        "Function_2_4C9",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_D4F",          # 04, 4
        "Function_5_D7F",          # 05, 5
        "Function_6_DAF",          # 06, 6
        "Function_7_DDF",          # 07, 7
        "Function_8_E3E",          # 08, 8
        "Function_9_111A",         # 09, 9
        "Function_10_13F6",        # 0A, 10
        "Function_11_16D2",        # 0B, 11
        "Function_12_21FF",        # 0C, 12
        "Function_13_222F",        # 0D, 13
        "Function_14_225F",        # 0E, 14
        "Function_15_228F",        # 0F, 15
        "Function_16_22B8",        # 10, 16
        "Function_17_2317",        # 11, 17
        "Function_18_23B2",        # 12, 18
        "Function_19_2404",        # 13, 19
        "Function_20_2579",        # 14, 20
        "Function_21_25C2",        # 15, 21
        "Function_22_260F",        # 16, 22
        "Function_23_2613",        # 17, 23
        "Function_24_2617",        # 18, 24
        "Function_25_261B",        # 19, 25
        "Function_26_261F",        # 1A, 26
        "Function_27_2623",        # 1B, 27
        "Function_28_2627",        # 1C, 28
        "Function_29_262B",        # 1D, 29
    )


    def Function_0_42A(): pass

    label("Function_0_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_444")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_47C")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_455")
    OP_A3(0x10F1)
    Event(0, 3)
    Jump("loc_47C")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_466")
    OP_A3(0x10F2)
    Event(0, 11)
    Jump("loc_47C")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_47C")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 2)
    Jump("loc_47C")

    label("loc_47C")

    Return()

    # Function_0_42A end

    def Function_1_47D(): pass

    label("Function_1_47D")

    OP_B1("T0100_n")
    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x230001)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xEA60, 0x0)

    label("loc_4B9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4C5"),
        (SWITCH_DEFAULT, "loc_4C8"),
    )


    label("loc_4C5")

    Jump("loc_4C8")

    label("loc_4C8")

    Return()

    # Function_1_47D end

    def Function_2_4C9(): pass

    label("Function_2_4C9")

    EventBegin(0x0)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0x15F90, 0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(50400, 0, 23350, 0)
    OP_67(0, 7720, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)

    def lambda_533():
        OP_6D(63060, 0, 57110, 9500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_533)

    def lambda_54B():
        OP_6C(38000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_54B)

    def lambda_55B():
        OP_67(0, 5420, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_55B)
    FadeToBright(1000, 0)
    Sleep(4500)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0211   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_4C9 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DE")
    Call(0, 17)
    FadeToBright(0, 0)
    Call(0, 18)

    label("loc_5DE")

    SetChrPos(0x101, 73060, 500, 32259, 0)
    SetChrPos(0x103, 73060, 500, 31260, 0)
    SetChrPos(0xF8, 73060, 500, 30260, 0)
    SetChrPos(0xF9, 73060, 500, 29260, 0)
    OP_6D(73090, 0, 34420, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x3B)
    OP_73(0xE)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x103, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_6A1():
        OP_6D(73020, 0, 37990, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A1)
    Sleep(2000)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    ChrTalk(    #0
        0x101,
        (
            "#1010F#6PHey, guys?\x02\x03",

            "#1002FAm I the only one who's suspecting\x01",
            "the society behind all this?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_766")

    ChrTalk(    #1
        0x108,
        "#074FNo... I'd say it's likely at this point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E")

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B6")

    ChrTalk(    #2
        0x104,
        (
            "#032FHardly. If anything, I find it likely at\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E")

    label("loc_7B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_810")

    ChrTalk(    #3
        0x106,
        (
            "#057FNo, I'd put money on those idiots\x01",
            "being the cause of all this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E")

    label("loc_810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85E")

    ChrTalk(    #4
        0x105,
        (
            "#043FIt does seem likely that they're\x01",
            "the culprits, yes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E7")

    ChrTalk(    #5
        0x107,
        (
            "#561FA coma Father Divine doesn't understand...\x02\x03",

            "#062FI guess that's kind of an incredible 'phenomenon,'\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_8E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A4")

    ChrTalk(    #6
        0x105,
        (
            "#047FA deep, sudden coma that the local church\x01",
            "head can do nothing about...\x02\x03",

            "#042FThat certainly seems like the sort of\x01",
            "incredible 'phenomenon' we were\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_9A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A40")

    ChrTalk(    #7
        0x106,
        (
            "#053FMysterious comas that your local father\x01",
            "can't even begin to explain?\x02\x03",

            "#057FYeah, sounds incredible enough to\x01",
            "be them, all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B32")

    ChrTalk(    #8
        0x104,
        (
            "#035FPeople asleep as if they were on death's door,\x01",
            "a shepherd unable to rouse his flock no matter\x01",
            "his efforts or prayers...\x02\x03",

            "#032FIt certainly strikes me as the sort of\x01",
            "terror which seems to be Ouroboros'\x01",
            "stock and trade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32")


    ChrTalk(    #9
        0x101,
        (
            "#1007F#6PThanks, guys. I was hoping I was just\x01",
            "being paranoid.\x02\x03",

            "#1002FBut then, I have to wonder...\x01",
            "Has anyone received a 'message'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#026F#6PThat's...a good question.\x02\x03",

            "#022FYou did write down the full list of people\x01",
            "who've fallen comatose, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1004F#6POh, one sec!\x02",
    )

    CloseMessageWindow()
    OP_AD(0x240116, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #12
        0x103,
        (
            "#022FWe can begin by asking the family, friends\x01",
            "and associates of those four about anything\x01",
            "suspicious.\x02\x03",

            "We can return to the guildhouse once we've\x01",
            "done so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1812)
    OP_28(0x90, 0x4, 0x2)
    OP_28(0x90, 0x4, 0x8)
    OP_28(0x90, 0x1, 0x1)
    OP_28(0x90, 0x1, 0x2)
    OP_28(0x90, 0x1, 0x8)
    OP_28(0x90, 0x1, 0x20)
    OP_28(0x90, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_5BE end

    def Function_4_D4F(): pass

    label("Function_4_D4F")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11CE2, 0x0, 0x9934, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_D4F end

    def Function_5_D7F(): pass

    label("Function_5_D7F")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12110, 0x0, 0x951A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_D7F end

    def Function_6_DAF(): pass

    label("Function_6_DAF")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x118BE, 0x0, 0x94CA, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_DAF end

    def Function_7_DDF(): pass

    label("Function_7_DDF")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_72(0xE, 0x800)
    OP_6F(0xE, 59)
    OP_70(0xE, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xE)
    OP_71(0xE, 0x800)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x11DFA, 0x0, 0x90BA, 0x7D0, 0x0)
    Return()

    # Function_7_DDF end

    def Function_8_E3E(): pass

    label("Function_8_E3E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1044")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E99")

    ChrTalk(    #14
        0x108,
        "#070FCome on. Let's get back to the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F6C")

    label("loc_E99")


    ChrTalk(    #15
        0x108,
        (
            "#070FA dark, foggy night on the road, huh?\x02\x03",

            "Perfect for some training, but...no, this\x01",
            "is hardly the time to think about that!\x02\x03",

            "We've finished our questioning, so we\x01",
            "really need to get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F6C")

    Jump("loc_1041")

    label("loc_F6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F85")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_F8C")

    label("loc_F85")

    TurnDirection(0x103, 0x0, 400)

    label("loc_F8C")


    ChrTalk(    #16
        0x103,
        (
            "#020FIt would be dangerous to go out on\x01",
            "the roads at night with fog this thick.\x02\x03",

            "We've finished our questioning, so we\x01",
            "should really get back to the guild\x01",
            "and give our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041")

    Jump("loc_10FE")

    label("loc_1044")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1094")

    ChrTalk(    #17
        0x108,
        (
            "#070FIt's late, Estelle. We need to finish\x01",
            "our questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FE")

    label("loc_1094")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AA")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_10B1")

    label("loc_10AA")

    TurnDirection(0x103, 0x0, 400)

    label("loc_10B1")


    ChrTalk(    #18
        0x103,
        (
            "#020FWe should finish our questioning\x01",
            "before it gets too late, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FE")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_E3E end

    def Function_9_111A(): pass

    label("Function_9_111A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1320")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1175")

    ChrTalk(    #19
        0x108,
        "#070FCome on. Let's get back to the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1248")

    label("loc_1175")


    ChrTalk(    #20
        0x108,
        (
            "#070FA dark, foggy night on the road, huh?\x02\x03",

            "Perfect for some training, but...no, this\x01",
            "is hardly the time to think about that!\x02\x03",

            "We've finished our questioning, so we\x01",
            "really need to get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1248")

    Jump("loc_131D")

    label("loc_124B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1268")

    label("loc_1261")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1268")


    ChrTalk(    #21
        0x103,
        (
            "#020FIt would be dangerous to go out on\x01",
            "the roads at night with fog this thick.\x02\x03",

            "We've finished our questioning, so we\x01",
            "should really get back to the guild\x01",
            "and give our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131D")

    Jump("loc_13DA")

    label("loc_1320")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(    #22
        0x108,
        (
            "#070FIt's late, Estelle. We need to finish\x01",
            "our questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_1370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1386")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_138D")

    label("loc_1386")

    TurnDirection(0x103, 0x0, 400)

    label("loc_138D")


    ChrTalk(    #23
        0x103,
        (
            "#020FWe should finish our questioning\x01",
            "before it gets too late, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DA")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_111A end

    def Function_10_13F6(): pass

    label("Function_10_13F6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1451")

    ChrTalk(    #24
        0x108,
        "#070FCome on. Let's get back to the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1524")

    label("loc_1451")


    ChrTalk(    #25
        0x108,
        (
            "#070FA dark, foggy night on the road, huh?\x02\x03",

            "Perfect for some training, but...no, this\x01",
            "is hardly the time to think about that!\x02\x03",

            "We've finished our questioning, so we\x01",
            "really need to get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1524")

    Jump("loc_15F9")

    label("loc_1527")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1544")

    label("loc_153D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1544")


    ChrTalk(    #26
        0x103,
        (
            "#020FIt would be dangerous to go out on\x01",
            "the roads at night with fog this thick.\x02\x03",

            "We've finished our questioning, so we\x01",
            "should really get back to the guild\x01",
            "and give our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F9")

    Jump("loc_16B6")

    label("loc_15FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164C")

    ChrTalk(    #27
        0x108,
        (
            "#070FIt's late, Estelle. We need to finish\x01",
            "our questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_164C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1662")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1669")

    label("loc_1662")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1669")


    ChrTalk(    #28
        0x103,
        (
            "#020FWe should finish our questioning\x01",
            "before it gets too late, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B6")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_10_13F6 end

    def Function_11_16D2(): pass

    label("Function_11_16D2")

    EventBegin(0x0)
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 55680, 250, 28860, 270)
    SetChrPos(0x8, 56680, 250, 28860, 270)
    SetChrPos(0x9, 57680, 250, 28860, 270)
    SetChrPos(0xA, 58680, 250, 28860, 270)
    SetChrPos(0xB, 60680, 250, 28860, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_43(0x8, 0x1, 0x0, 0xD)
    OP_43(0x9, 0x1, 0x0, 0xE)
    OP_43(0xA, 0x1, 0x0, 0xF)
    OP_43(0xB, 0x1, 0x0, 0x10)
    Sleep(2000)

    def lambda_17C8():
        OP_6D(50370, 0, 29350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17C8)

    def lambda_17E0():
        OP_67(0, 8830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17E0)

    def lambda_17F8():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17F8)

    def lambda_1808():
        OP_6E(272, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1808)
    WaitChrThread(0xB, 0x1)
    Sleep(500)

    ChrTalk(    #29
        0xB,
        (
            "#030FAh! The high moon weaves gossamer threads\x01",
            "through the mist! We should rest soon.\x02\x03",

            "#031FWell, then, Estelle! Lead on to your home!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18AE():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18AE)
    Sleep(50)

    def lambda_18C1():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18C1)
    Sleep(50)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #30
        0x101,
        (
            "#1019F#5PEr. Why exactly are you coming\x01",
            "with US, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#031FHa-ha-ha! Fear not, my sweet!\x02\x03",

            "Olivier Lenheim is a perfect gentleman who would\x01",
            "never overstep his bounds. Especially in a\x01",
            "gathering of lovely ladies such as this!\x02\x03",

            "#037FNay, my purpose is merely to...protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        "#065FUmmmmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#045F#6PUm, Olivier, I think we'll...be all right.\x01",
            "Really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#5POh, we'll be protected, all right.\x01",
            "Once I tie you to a mattress and throw\x01",
            "you in the river, that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(200)
    SetChrPos(0xC, 55680, 250, 28860, 270)
    ClearChrFlags(0xC, 0x80)

    def lambda_1AF0():
        OP_8E(0xC, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1AF0)
    Sleep(500)

    def lambda_1B10():
        OP_6D(51570, 0, 29500, 1500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B10)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x0)

    ChrTalk(    #35
        0xC,
        (
            "#555FHey. Idiot. What the hell are you doing\x01",
            "out here?\x02\x03",

            "We need to figure out who'll be on\x01",
            "patrol and when.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 400)

    ChrTalk(    #36
        0xB,
        (
            "#033F#6PWhat...?\x02\x03",

            "#031FHa-ha-ha! Oh, Agate!\x01",
            "The muse of comedy touches you!\x02\x03",

            "Did you not say that you and Zin\x01",
            "would handle the patrol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "#050FUh. No? I said 'leave it to us guys.'\x01",
            "Last I checked, that includes you.\x02\x03",

            "But I could be wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#033F#6PErm.\x02",
    )

    CloseMessageWindow()
    OP_8E(0xC, 0xCC4C, 0x82, 0x70BC, 0x7D0, 0x0)

    ChrTalk(    #39
        0xC,
        "#054FC'mon, get inside!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #40
        0xB,
        (
            "#036F#6PAgate, wait a moment!\x02\x03",

            "Do you not realize that a...gathering,\x01",
            "such as this, is no common occurrence?\x02\x03",

            "I'll enjoy it enough for the both of us!\x01",
            "Just let me go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        "#053FYeah, you get inside. C'mon.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x20)
    OP_8C(0xB, 270, 800)

    def lambda_1DD4():
        OP_90(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DD4)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 7)
    OP_63(0xB)

    def lambda_1E01():
        OP_91(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E01)
    WaitChrThread(0xB, 0x1)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0xA, 0x800)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_1EA5():
        OP_6D(50370, 0, 29350, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EA5)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        (
            "#1007F#5PWelllll...that's probably the best way\x01",
            "to domesticate Olivier. On the whole.\x02\x03",

            "#1019FHow the heck can he not show any, like,\x01",
            "tension or anything in our predicament,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F7C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F7C)
    Sleep(50)

    def lambda_1F8F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F8F)
    Sleep(50)

    def lambda_1FA2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FA2)
    WaitChrThread(0xA, 0x1)
    Sleep(400)

    ChrTalk(    #43
        0xA,
        (
            "#045F#4PHaha... It's hard to tell, sometimes,\x01",
            "whether he's joking or really serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1015F#5PI'm pretty sure he was 100% serious.\x02\x03",

            "#1006FOne way or another, though, he's, uh...\x01",
            "a bad influence on Tita! Yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "#067F#2PWell, um, I kind of feel sorry\x01",
            "for Olivier, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#524F#6PHmm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1015F#5PSchera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#027F#6PIt's nothing.\x02\x03",

            "As much as I despair to borrow his\x01",
            "words, he did have a point. We should\x01",
            "call it a night soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1006F#5PYeah, that's true.\x02\x03",

            "Okay, Tita, Kloe, follow me.\x01",
            "I'll show you guys the way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_16D2 end

    def Function_12_21FF(): pass

    label("Function_12_21FF")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_21FF end

    def Function_13_222F(): pass

    label("Function_13_222F")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_13_222F end

    def Function_14_225F(): pass

    label("Function_14_225F")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_225F end

    def Function_15_228F(): pass

    label("Function_15_228F")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF768, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_15_228F end

    def Function_16_22B8(): pass

    label("Function_16_22B8")

    OP_8E(0xFE, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_8C(0xFE, 270, 400)
    OP_71(0xA, 0x800)
    OP_90(0xFE, 0xFFFFFB32, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_16_22B8 end

    def Function_17_2317(): pass

    label("Function_17_2317")

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
        (0, "loc_2393"),
        (1, "loc_2399"),
        (SWITCH_DEFAULT, "loc_239F"),
    )


    label("loc_2393")

    OP_A2(0x1200)
    Jump("loc_239F")

    label("loc_2399")

    OP_A2(0x1201)
    Jump("loc_239F")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_23AD")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_23B1")

    label("loc_23AD")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_23B1")

    Return()

    # Function_17_2317 end

    def Function_18_23B2(): pass

    label("Function_18_23B2")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_18_23B2 end

    def Function_19_2404(): pass

    label("Function_19_2404")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x05《Septian Calendar 1075》\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x05《Septian Calendar 1192》\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #52
        (
            "\x07\x05《Septian Calendar 1197》\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_19_2404 end

    def Function_20_2579(): pass

    label("Function_20_2579")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #53
        "\x07\x05West: Malga Trail Exit\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_2579 end

    def Function_21_25C2(): pass

    label("Function_21_25C2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        "\x07\x05North: Rolent Landing Port\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_25C2 end

    def Function_22_260F(): pass

    label("Function_22_260F")

    SetPlaceName(0x4)
    Return()

    # Function_22_260F end

    def Function_23_2613(): pass

    label("Function_23_2613")

    SetPlaceName(0x2)
    Return()

    # Function_23_2613 end

    def Function_24_2617(): pass

    label("Function_24_2617")

    SetPlaceName(0x6)
    Return()

    # Function_24_2617 end

    def Function_25_261B(): pass

    label("Function_25_261B")

    SetPlaceName(0x5)
    Return()

    # Function_25_261B end

    def Function_26_261F(): pass

    label("Function_26_261F")

    SetPlaceName(0x7)
    Return()

    # Function_26_261F end

    def Function_27_2623(): pass

    label("Function_27_2623")

    SetPlaceName(0x8)
    Return()

    # Function_27_2623 end

    def Function_28_2627(): pass

    label("Function_28_2627")

    SetPlaceName(0x3)
    Return()

    # Function_28_2627 end

    def Function_29_262B(): pass

    label("Function_29_262B")

    SetPlaceName(0xA)
    Return()

    # Function_29_262B end

    SaveToFile()

Try(main)
