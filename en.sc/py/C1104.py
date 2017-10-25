from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1104   ._SN',
        MapName             = 'Bose',
        Location            = 'C1104.x',
        MapIndex            = 49,
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
        'Campanella',                           # 9
        'Kevin',                                # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03095 ._CH',             # 02
        'ED6_DT07/CH00120 ._CH',             # 03
        'ED6_DT07/CH00121 ._CH',             # 04
        'ED6_DT07/CH00122 ._CH',             # 05
        'ED6_DT07/CH00124 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT07/CH00152 ._CH',             # 09
        'ED6_DT07/CH00154 ._CH',             # 0A
        'ED6_DT07/CH00420 ._CH',             # 0B
        'ED6_DT07/CH00421 ._CH',             # 0C
        'ED6_DT07/CH00424 ._CH',             # 0D
        'ED6_DT06/CH20042 ._CH',             # 0E
        'ED6_DT26/CH20299 ._CH',             # 0F
        'ED6_DT26/CH20300 ._CH',             # 10
        'ED6_DT07/CH00340 ._CH',             # 11
        'ED6_DT07/CH00440 ._CH',             # 12
        'ED6_DT07/CH00341 ._CH',             # 13
        'ED6_DT07/CH00441 ._CH',             # 14
        'ED6_DT07/CH00123 ._CH',             # 15
        'ED6_DT07/CH00153 ._CH',             # 16
        'ED6_DT07/CH00423 ._CH',             # 17
        'ED6_DT07/CH00055 ._CH',             # 18
        'ED6_DT07/CH00025 ._CH',             # 19
        'ED6_DT26/CH20298 ._CH',             # 1A
        'ED6_DT26/CH20305 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03095P._CP',             # 02
        'ED6_DT07/CH00120P._CP',             # 03
        'ED6_DT07/CH00121P._CP',             # 04
        'ED6_DT07/CH00122P._CP',             # 05
        'ED6_DT07/CH00124P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT07/CH00152P._CP',             # 09
        'ED6_DT07/CH00154P._CP',             # 0A
        'ED6_DT07/CH00420P._CP',             # 0B
        'ED6_DT07/CH00421P._CP',             # 0C
        'ED6_DT07/CH00424P._CP',             # 0D
        'ED6_DT06/CH20042P._CP',             # 0E
        'ED6_DT26/CH20299P._CP',             # 0F
        'ED6_DT26/CH20300P._CP',             # 10
        'ED6_DT07/CH00340P._CP',             # 11
        'ED6_DT07/CH00440P._CP',             # 12
        'ED6_DT07/CH00341P._CP',             # 13
        'ED6_DT07/CH00441P._CP',             # 14
        'ED6_DT07/CH00123P._CP',             # 15
        'ED6_DT07/CH00153P._CP',             # 16
        'ED6_DT07/CH00423P._CP',             # 17
        'ED6_DT07/CH00055P._CP',             # 18
        'ED6_DT07/CH00025P._CP',             # 19
        'ED6_DT26/CH20298P._CP',             # 1A
        'ED6_DT26/CH20305P._CP',             # 1B
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_25E",          # 01, 1
        "Function_2_264",          # 02, 2
        "Function_3_27A",          # 03, 3
        "Function_4_20A8",         # 04, 4
        "Function_5_503A",         # 05, 5
        "Function_6_504F",         # 06, 6
        "Function_7_5078",         # 07, 7
        "Function_8_50B6",         # 08, 8
        "Function_9_50FE",         # 09, 9
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_25D")

    Return()

    # Function_0_24A end

    def Function_1_25E(): pass

    label("Function_1_25E")

    OP_22(0x10E, 0x1, 0x5A)
    Return()

    # Function_1_25E end

    def Function_2_264(): pass

    label("Function_2_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_279")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_264")

    label("loc_279")

    Return()

    # Function_2_264 end

    def Function_3_27A(): pass

    label("Function_3_27A")

    EventBegin(0x0)
    OP_DB()
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_291")
    ClearParty()
    AddParty(0x5, 0xF6, 0xFF)
    Jump("loc_296")

    label("loc_291")

    ClearParty()
    AddParty(0x2, 0xF6, 0xFF)

    label("loc_296")

    AddParty(0x9, 0xF7, 0xFF)
    OP_6D(-330, 0, 3610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(547, 0)
    SetChrPos(0xF6, 4590, 0, -23390, 333)
    SetChrPos(0x10A, 3790, 50, -24060, 333)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_309():
        OP_6D(3640, 130, -22260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_309)

    def lambda_321():
        OP_67(0, 10920, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_321)

    def lambda_339():
        OP_6B(2240, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_339)

    def lambda_349():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_349)
    OP_6C(3000, 8000)
    Sleep(500)
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4A0")

    ChrTalk(    #0
        0x106,
        (
            "#552F#2PThat's weird.\x01",
            "This is definitely their hideout...\x02\x03",

            "...but where the hell is everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10A,
        (
            "#1317FYeah, we totally tracked them here.\x02\x03",

            "So where'd all those Intelligence\x01",
            "weirdos go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        (
            "#053F#2PHrmm. They mighta figured out we were\x01",
            "on to 'em, but...\x02\x03",

            "#050FAh, screw it. Let's have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB")

    label("loc_4A0")


    ChrTalk(    #3
        0x103,
        (
            "#022F#2PThat's odd. This IS where they've been\x01",
            "hiding, as we thought.\x02\x03",

            "But I don't see any trace of...anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        (
            "#1317FYeah, we totally tracked them here.\x02\x03",

            "So where'd all those Intelligence\x01",
            "weirdos go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x103,
        (
            "#026F#2PDid they...notice us? I didn't think we...\x02\x03",

            "#027FWell, let's have a look around anyway,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0xF6, 1180, 0, -470, 90)
    SetChrPos(0x10A, -6500, 0, 5600, 180)
    OP_6D(-2610, 0, -760, 0)
    OP_67(0, 9420, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(45000, 0)
    OP_6E(449, 0)
    FadeToBright(1000, 0)

    def lambda_659():
        OP_6B(1400, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_659)

    def lambda_669():
        OP_8F(0xFE, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_669)
    Sleep(1500)
    OP_8C(0xF6, 270, 400)

    def lambda_690():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xFFFFFB46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_690)
    WaitChrThread(0x10A, 0x0)
    OP_8C(0x10A, 90, 400)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0x10A, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_12AA")

    ChrTalk(    #6
        0x10A,
        (
            "#1316F#6PNo good. This place is an empty shell.\x02\x03",

            "#818FDo you see anything, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#555FNot a friggin' thing.\x02\x03",

            "Can't even tell if they're just\x01",
            "out or if they ditched the place\x01",
            "or what.\x02\x03",

            "Not even any clues as to where\x01",
            "they went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#810F#6PUm, about that, I didn't find any\x01",
            "mention of where they were going...\x02\x03",

            "...but I did find this over in that tent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        "#052FOh, hey, let me have a look.\x02",
    )

    CloseMessageWindow()
    OP_92(0x10A, 0xF6, 0x320, 0x5DC, 0x0)
    Sleep(500)
    OP_8F(0x10A, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240112, 0xBE, 0x96, 0x1F4)
    Sleep(3000)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1500)

    ChrTalk(    #10
        0x106,
        (
            "#555FThe hell is...?\x01",
            "These are blueprints of some kind.\x02\x03",

            "Looks like it's for something called\x01",
            "the 'Orgueille'...\x02\x03",

            "It kinda looks like a vehicle of some\x01",
            "sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        (
            "#810F#6POooo, 'Orgueille.' That sounds cool!\x02\x03",

            "What is it, some kind of airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#053FI can't really tell...\x01",
            "Seems a bit small for one.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #13
        0x106,
        "#052F...What the?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#814F#6PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#555FThere's some kinda note in between\x01",
            "the pages.\x02\x03",

            " 'I've sent out the invitations.'\x02\x03",

            " 'I've got the table and chairs ready.'\x02\x03",

            " 'Everything's ready for the tea party.'\x02\x03",

            " 'Now all I need is to bake some crumpets\x01",
            "and wait for the guests to arrive!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        (
            "#1310F#6PAwww! A tea party! That's really cute.\x02\x03",

            "#811FIt's like something out of a storybook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#053FHmph. Some kind of code, I guess.\x02\x03",

            "#552FThe hell does it mean, though?\x01",
            "'Tea party'... Gotta be some kinda...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x106,
        "#054F#4SSCATTER!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#814F#6PAaah!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x106, 7)
    SetChrChipByIndex(0x10A, 11)

    def lambda_D30():
        OP_96(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFA06, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_D30)

    def lambda_D4E():
        OP_96(0xFE, 0xFFFFEE30, 0x0, 0xFFFFFB28, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_D4E)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_DB0():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_DB0)

    def lambda_DBE():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_DBE)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -11440, 0, -1180, 90)
    SetChrPos(0xB, 7610, 0, -2040, 270)
    SetChrPos(0xC, -3650, 0, -10100, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)

    def lambda_EAF():
        OP_6D(-3470, 0, -1890, 3000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_EAF)

    def lambda_EC7():
        OP_67(0, 8380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_EC7)

    def lambda_EDF():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_EDF)

    def lambda_EEF():
        OP_6E(501, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_EEF)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)
    OP_8C(0x106, 90, 400)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #20
        0x10A,
        "#1317F#6PNo way... How'd they sneak up on us?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#051F#7PHeh. Those are some serious\x01",
            "stealth skills, guys.\x02\x03",

            "That another trick you learn from\x01",
            "Lieutenant Red?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "#1K#2P...\x02",
    )


    ChrTalk(    #23
        0xB,
        "#1K#6P...\x02",
    )


    ChrTalk(    #24
        0xC,
        "#1K#1P...\x02",
    )

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_1003():
        OP_8F(0xFE, 0xFFFFD71A, 0x0, 0xFFFFFBF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1003)

    def lambda_101E():
        OP_8E(0xFE, 0x15A4, 0x0, 0xFFFFF77C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_101E)

    def lambda_1039():
        OP_8E(0xFE, 0xFFFFF11E, 0x0, 0xFFFFDCC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1039)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_43(0x10A, 0x0, 0x0, 0x6)

    def lambda_106C():
        OP_6D(-2240, 0, -1410, 3000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_106C)

    def lambda_1084():
        OP_67(0, 7870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1084)

    def lambda_109C():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_109C)
    Sleep(250)

    def lambda_10B1():
        OP_8F(0xFE, 0xFFFFDB84, 0x0, 0xFFFFFBD2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10B1)

    def lambda_10CC():
        OP_8E(0xFE, 0x1266, 0x0, 0xFFFFF768, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10CC)

    def lambda_10E7():
        OP_8E(0xFE, 0xFFFFF178, 0x0, 0xFFFFE0A3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10E7)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x10A, 0x0)
    Sleep(250)

    def lambda_111C():
        OP_8F(0xFE, 0xFFFFE142, 0x0, 0xFFFFFAA6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_111C)

    def lambda_1137():
        OP_8E(0xFE, 0xEB0, 0x0, 0xFFFFF75E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1137)

    def lambda_1152():
        OP_8E(0xFE, 0xFFFFF204, 0x0, 0xFFFFE48A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1152)
    OP_43(0x10A, 0x0, 0x0, 0x6)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)

    ChrTalk(    #25
        0x10A,
        "#812F#6P(Umm, Agate...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#053F#7P(Yeah, I see it.\x01",
            "There's something wrong here.)\x02\x03",

            "#050F(Okay. Feint to a side, crush\x01",
            "one corner of the triangle, then\x01",
            "we'll take out the rest.)\x02\x03",

            "(You ready?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        "#816F#6P(Leave it to me!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#054F#7PGO!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        "#815F#6POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_12AA")


    ChrTalk(    #30
        0x10A,
        (
            "#1316F#6PNo good. This place is an empty shell.\x02\x03",

            "#818FDo you see anything, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#025FI'm drawing a blank.\x02\x03",

            "#522FThey were here...but it's impossible\x01",
            "to tell if they're just out, or if they\x01",
            "abandoned this base.\x02\x03",

            "I don't even see any clue as to where\x01",
            "they might have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#810F#6PUm, about that, I didn't find any mention\x01",
            "of where they were going...\x02\x03",

            "...but I did find this over in that tent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        "#023FReally? Mind if I take a look?\x02",
    )

    CloseMessageWindow()
    OP_92(0x10A, 0xF6, 0x320, 0x5DC, 0x0)
    Sleep(500)
    OP_8F(0x10A, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240112, 0xBE, 0x96, 0x1F4)
    Sleep(3000)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1500)

    ChrTalk(    #34
        0x103,
        (
            "#022FHmmmm. These are blueprints of some sort.\x02\x03",

            "Looks like it's for something named\x01",
            "the 'Orgueille'...\x02\x03",

            "Unless I'm totally illiterate, these are\x01",
            "plans for a vehicle of some sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10A,
        (
            "#810F#6POooo, 'Orgueille.' That sounds cool!\x02\x03",

            "What is it, some kind of airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#025FWell, I'm not exactly an engineer,\x01",
            "but I don't think so... Those look like--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #37
        0x103,
        "#023FHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        "#814F#6PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        (
            "#022FThere's a note in between the pages.\x02\x03",

            " 'I've sent out the invitations.'\x02\x03",

            " 'I've got the table and chairs ready.'\x02\x03",

            " 'Everything's ready for the tea party.'\x02\x03",

            " 'Now all I need is to bake some crumpets\x01",
            "and wait for the guests to arrive!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1310F#6PAwww! A tea party! That's really cute.\x02\x03",

            "#811FIt's like something out of a storybook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        (
            "#026FYes...which must mean it's a cipher of\x01",
            "some sort.\x02\x03",

            "#522FWhat do they mean by 'tea party,'\x01",
            "I wonder...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x103,
        "#024F#4SWatch out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#814F#6PAaah!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1947():
        OP_96(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFA06, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1947)

    def lambda_1965():
        OP_96(0xFE, 0xFFFFEE30, 0x0, 0xFFFFFB28, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1965)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x103, 3)
    SetChrChipByIndex(0x10A, 11)

    def lambda_19D1():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19D1)

    def lambda_19DF():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_19DF)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -11440, 0, -1180, 90)
    SetChrPos(0xB, 7610, 0, -2040, 270)
    SetChrPos(0xC, -3650, 0, -10100, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)

    def lambda_1AD0():
        OP_6D(-3470, 0, -1890, 3000)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1AD0)

    def lambda_1AE8():
        OP_67(0, 8380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AE8)

    def lambda_1B00():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B00)

    def lambda_1B10():
        OP_6E(501, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1B10)
    WaitChrThread(0x103, 0x0)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)
    OP_8C(0x103, 90, 400)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #44
        0x10A,
        (
            "#1317F#6PNo way... \x01",
            "How'd they sneak up on us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        (
            "#027F#7PGoodness. That was a fair bit\x01",
            "of sneaking, friends.\x02\x03",

            "I take it that's another trick our\x01",
            "good friend Lorence taught you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        "#1K#2P...\x02",
    )


    ChrTalk(    #47
        0xB,
        "#1K#6P...\x02",
    )


    ChrTalk(    #48
        0xC,
        "#1K#1P...\x02",
    )

    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_1C33():
        OP_8F(0xFE, 0xFFFFD71A, 0x0, 0xFFFFFBF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C33)

    def lambda_1C4E():
        OP_8E(0xFE, 0x15A4, 0x0, 0xFFFFF77C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C4E)

    def lambda_1C69():
        OP_8E(0xFE, 0xFFFFF11E, 0x0, 0xFFFFDCC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C69)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_43(0x10A, 0x0, 0x0, 0x6)

    def lambda_1C9C():
        OP_6D(-2240, 0, -1410, 3000)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C9C)

    def lambda_1CB4():
        OP_67(0, 7870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CB4)

    def lambda_1CCC():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CCC)
    Sleep(250)

    def lambda_1CE1():
        OP_8F(0xFE, 0xFFFFDB84, 0x0, 0xFFFFFBD2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CE1)

    def lambda_1CFC():
        OP_8E(0xFE, 0x1266, 0x0, 0xFFFFF768, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CFC)

    def lambda_1D17():
        OP_8E(0xFE, 0xFFFFF178, 0x0, 0xFFFFE0A3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D17)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x10A, 0x0)
    Sleep(250)

    def lambda_1D4C():
        OP_8F(0xFE, 0xFFFFE142, 0x0, 0xFFFFFAA6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D4C)

    def lambda_1D67():
        OP_8E(0xFE, 0xEB0, 0x0, 0xFFFFF75E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D67)

    def lambda_1D82():
        OP_8E(0xFE, 0xFFFFF204, 0x0, 0xFFFFE48A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D82)
    OP_43(0x10A, 0x0, 0x0, 0x6)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    WaitChrThread(0x103, 0x0)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)

    ChrTalk(    #49
        0x10A,
        "#812F#6P(Umm, Schera...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#026F#7P(I know. Something here isn't right.)\x02\x03",

            "#020F(All right. We'll feint to one side,\x01",
            "break one corner of the triangle,\x01",
            "and clean up the rest.)\x02\x03",

            "(Can you do it?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#816F#6P(Just say when!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#024F#7PAll right! GO! GO!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        "#815F#6PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_1EE7")

    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_1EFC():
        OP_8E(0xFE, 0xFFFFEF48, 0x0, 0xFFFFFA42, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1EFC)

    def lambda_1F17():
        OP_8E(0xFE, 0x28, 0x0, 0xFFFFFA7E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F17)

    def lambda_1F32():
        OP_8E(0xFE, 0xFFFFF4D4, 0x0, 0xFFFFF13C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1F32)

    def lambda_1F4D():
        OP_6B(1300, 500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_1F4D)
    WaitChrThread(0x10A, 0x3)
    OP_D6(0x0)
    OP_3E(0x1F6, 4)
    OP_3E(0x1FC, 2)
    OP_3E(0x1FB, 4)
    OP_31(0x9, 0x0, 0x35)
    OP_31(0x9, 0xFE, 0x0)
    OP_31(0x9, 0x5, 0x41)
    OP_41(0x9, 0xCF, 0xFF)
    OP_41(0x9, 0x101, 0xFF)
    OP_41(0x9, 0x121, 0xFF)
    OP_41(0x9, 0x2C2, 0x0)
    OP_41(0x9, 0x2C9, 0x1)
    OP_41(0x9, 0x262, 0x2)
    OP_41(0x9, 0x291, 0x3)
    OP_41(0x9, 0x265, 0x4)
    OP_41(0x9, 0x259, 0x5)
    OP_41(0x9, 0x0, 0x3)
    OP_41(0x9, 0x0, 0x4)
    OP_35(0x9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2012")
    OP_31(0x2, 0x0, 0x37)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x2, 0x5, 0x41)
    OP_41(0x2, 0x45, 0xFF)
    OP_41(0x2, 0x101, 0xFF)
    OP_41(0x2, 0x121, 0xFF)
    OP_41(0x2, 0x45, 0x0)
    OP_41(0x2, 0x26F, 0x0)
    OP_41(0x2, 0x265, 0x1)
    OP_41(0x2, 0x25C, 0x2)
    OP_41(0x2, 0x280, 0x4)
    OP_41(0x2, 0x25F, 0x5)
    OP_41(0x2, 0x0, 0x3)
    OP_41(0x2, 0x0, 0x4)
    OP_35(0x2, 0x0)
    Jump("loc_2066")

    label("loc_2012")

    OP_31(0x5, 0x0, 0x37)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x5, 0x5, 0x41)
    OP_41(0x5, 0xA0, 0xFF)
    OP_41(0x5, 0x101, 0xFF)
    OP_41(0x5, 0x121, 0xFF)
    OP_41(0x5, 0x260, 0x0)
    OP_41(0x5, 0x271, 0x1)
    OP_41(0x5, 0x268, 0x2)
    OP_41(0x5, 0x283, 0x5)
    OP_41(0x5, 0x262, 0x6)
    OP_41(0x5, 0x0, 0x3)
    OP_41(0x5, 0x0, 0x4)
    OP_35(0x5, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2066")
    OP_BB(0x5, 0x6, 0x100)

    label("loc_2066")

    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x7A0, 0x0, 0x1, 0x0, 0xFF)
    OP_D6(0x1)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 4)
    Return()

    # Function_3_27A end

    def Function_4_20A8(): pass

    label("Function_4_20A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrChipByIndex(0xA, 14)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 3)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 2)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF6, 65535)
    ClearChrFlags(0xF6, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrPos(0xF6, -3000, 0, -2660, 270)
    SetChrPos(0x10A, -2930, 0, -3910, 270)
    SetChrPos(0xA, -6360, 0, -3390, 90)
    SetChrPos(0xB, -7770, 0, -4330, 270)
    SetChrPos(0xC, -7530, 0, -2270, 90)
    SetChrPos(0x8, 6360, 0, -3740, 270)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-4000, 0, -2190, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(45000, 0)
    OP_6E(464, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_38A2")

    ChrTalk(    #54
        0x106,
        (
            "#057F#6PWhat's with these guys?\x02\x03",

            "I mean, we beat them, so whatever,\x01",
            "but...that was a strange fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10A,
        (
            "#812F#4PDo you think they were on drugs or\x01",
            "something?\x02\x03",

            "I remember hearing they used\x01",
            "something like that to control some\x01",
            "thugs in...Ruan, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        (
            "#552F#6PNah, that was different. This...\x02\x03",

            "This was like...hacking at a stone,\x01",
            "or...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #57
        0x8,
        "Boy's Voice",
        "#3PHa-HA! What great fun!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #58
        0x8,
        "Boy's Voice",
        (
            "#3PYou two aren't half bad, are you?\x01",
            "What a treat.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_21()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_59()
    OP_1D(0x6F)
    Sleep(1000)

    def lambda_240D():
        OP_6D(-130, 0, -2660, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_240D)

    def lambda_2425():
        OP_67(0, 7230, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2425)

    def lambda_243D():
        OP_6B(2009, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_243D)

    def lambda_244D():
        OP_8E(0xFE, 0xD20, 0x0, 0xFFFFF164, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_244D)

    def lambda_2468():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2468)
    TurnDirection(0x10A, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #59
        0x106,
        "#052F#1PYou...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x8,
        "Strange Boy",
        "#853FHaha...\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS118._CH")
    OP_C6(0x0, 0x0, 150000, 60000, 0)
    OP_C6(0x0, 0x0, 175000, 60000, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Strange Boy")

    AnonymousTalk(    #61
        (
            "#850FI am Enforcer No. 0, Campanella the Fool.\x02\x03",

            "I am but one hand of the Society of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x10A,
        "#1317F#5PO-Ouro...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x106,
        (
            "#057F#1PFinally decided to show your face,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 7)
    SetChrSubChip(0x106, 0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Sleep(500)

    ChrTalk(    #64
        0x106,
        (
            "#057F#1PJust what's your scheme, anyway?\x02\x03",

            "What the hell are you planning on doing\x01",
            "with what's left of the Intelligence idiots?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#853FHaha, I'm sorry. I'm afraid I'm little more\x01",
            "than an observer this time.\x02\x03",

            "You're asking the wrong person if you\x01",
            "want details about the plan.\x02\x03",

            "In fact, I barely know them myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        "#555F#1PAn 'observer'? The hell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#850FAnyway, if you want to attend that tea\x01",
            "party, you'd better hurry.\x02\x03",

            "I'm not quite sure where it's being held,\x01",
            "but it isn't here.\x02\x03",

            "#851FOr shall we share some coffee instead,\x01",
            "and enjoy the dawn together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x106,
        "#057F#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10A,
        (
            "#813F#5PUm, kid?\x02\x03",

            "You look pretty young.\x01",
            "Are you really part of the society?\x02\x03",

            "#812FI don't mean to be insulting or anything,\x01",
            "but you might want to get away from them.\x01",
            "They're bad people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#853FYou're very kind, miss.\x02\x03",

            "But you know...it's okay to laugh at a fool.\x01",
            "That's what he's there for.\x02\x03",

            "#854FBut worrying about the Fool?\x01",
            "Now that's quite rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        "#814F#5PHuh...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)

    def lambda_2A4A():
        OP_6D(-2000, 0, -2270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A4A)
    Fade(1000)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    OP_8C(0xA, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_0D()
    WaitChrThread(0x8, 0x1)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2ADD():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2ADD)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #72
        0x10A,
        "#1317FWh-Wha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#055F#6PHow the hell...?\x01",
            "We beat them senseless!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#854F#8PAh, you bracers really are naive.\x02\x03",

            "If you really want to defeat someone...\x01",
            "you have to break them into pieces.\x01",
            "Like...so.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "monster\\msc0100.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    LoadEffect(0x2, "map\\mp047_00.eff")
    PlayEffect(0x2, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x5, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x6, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Fade(500)

    def lambda_2D7B():
        OP_6D(-130, 0, -2660, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D7B)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrChipByIndex(0xB, 15)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrPos(0xA, -5990, 0, -2060, 0)
    SetChrPos(0xC, -7310, 0, -5200, 0)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 3)
    SetChrPos(0xD, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x106, 22)
    SetChrChipByIndex(0x10A, 23)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x10A, 0)

    def lambda_2E3B():
        OP_96(0xFE, 0xFFFFF948, 0x0, 0xFFFFF75E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2E3B)

    def lambda_2E59():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2E59)

    def lambda_2E73():
        OP_96(0xFE, 0xFFFFF876, 0x0, 0xFFFFF06A, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2E73)

    def lambda_2E91():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_2E91)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x106, 270, 0)
    OP_8C(0x10A, 270, 0)
    SetChrChipByIndex(0x106, 10)
    SetChrChipByIndex(0x10A, 13)
    SetChrSubChip(0x106, 3)
    SetChrSubChip(0x10A, 3)

    ChrTalk(    #75 op#A op#5
        0x106,
        "#056F#10A#1PSHIT!\x05\x02",
    )


    ChrTalk(    #76 op#A op#5
        0x10A,
        "#1312F#1P#10A#2PAIEEEE...!\x05\x02",
    )

    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_9E(0x106, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(500)

    ChrTalk(    #77
        0x106,
        "#550F#5PYou little...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10A,
        (
            "#1317FYou... You... That's...\x01",
            "How could you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#851FHaha! Did I surprise you?\x02\x03",

            "It's so easy to break even a\x01",
            "well-made toy, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x2, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #80
        0x8,
        (
            "#854FBut I'm afraid that's the end of the\x01",
            "Fool's show for tonight.\x02",
        )
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x3E8)

    ChrTalk(    #81
        0x8,
        (
            "#854FFarewell! Hopefully I can give you\x01",
            "an encore someday.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30F8():

        label("loc_30F8")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_30F8")

    QueueWorkItem2(0x106, 3, lambda_30F8)
    Sleep(500)
    OP_99(0x106, 0x3, 0x0, 0x5DC)
    OP_44(0x106, 0x3)
    SetChrChipByIndex(0x106, 7)
    SetChrSubChip(0x106, 0)
    Sleep(300)
    OP_8C(0x106, 90, 600)

    ChrTalk(    #82
        0x106,
        "#054F#3SGET BACK HERE!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 0)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 8)

    def lambda_316A():
        OP_6D(2500, 0, -2270, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_316A)

    def lambda_3182():
        OP_8F(0xFE, 0x1F4, 0x0, 0xFFFFF380, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3182)

    def lambda_319D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_319D)
    WaitChrThread(0x106, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x106, 9)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x20)
    OP_82(0x1, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x8)

    def lambda_31D2():
        OP_94(0x1, 0xFE, 0x0, 0x9C4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_31D2)

    def lambda_31E8():
        OP_99(0xFE, 0x0, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_31E8)
    Sleep(300)
    OP_22(0x208, 0x0, 0x64)
    OP_20(0x7D0)
    WaitChrThread(0x106, 0x2)
    OP_44(0x106, 0x1)
    Sleep(2000)
    OP_99(0x106, 0x7, 0x0, 0x5DC)
    ClearChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x20)
    SetChrFlags(0x8, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #83
        0x106,
        "#057F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_3244():

        label("loc_3244")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3244")

    QueueWorkItem2(0x10A, 3, lambda_3244)
    Sleep(500)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_44(0x10A, 0x3)
    Fade(250)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #84
        0x10A,
        (
            "#813F#1P...\x02\x03",

            "A-Agate... Umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#053F#6PI... I know.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x106, 270, 400)
    Sleep(500)

    def lambda_32F5():

        label("loc_32F5")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_32F5")

    QueueWorkItem2(0x10A, 1, lambda_32F5)

    def lambda_3306():
        OP_6D(-2500, 0, -3390, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3306)
    OP_8E(0x106, 0xFFFFF7EA, 0x0, 0xFFFFF56A, 0x5DC, 0x0)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #86
        0x106,
        (
            "#552F#4PThey weren't guilty of any crime\x01",
            "so bad they deserved to die like\x01",
            "this.\x02\x03",

            "We can't leave 'em...here.\x01",
            "Just layin' around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #87
        0x106,
        (
            "#556FHey. Go kill some time somewhere,\x01",
            "all right?\x02\x03",

            "Kid like you doesn't need to deal\x01",
            "with this. I'll take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10A,
        "#1317F#4PBut, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0x10A, 0x1)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #89
        0x10A,
        "#814F...What?\x02",
    )

    CloseMessageWindow()

    def lambda_3497():

        label("loc_3497")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_3497")

    QueueWorkItem2(0x106, 1, lambda_3497)

    def lambda_34A8():
        OP_8E(0xFE, 0xFFFFF150, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_34A8)
    WaitChrThread(0x10A, 0x1)
    Fade(250)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 2)
    SetChrSubChip(0x10A, 7)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x10A, 16)
    SetChrSubChip(0x10A, 7)
    OP_0D()

    ChrTalk(    #90
        0x106,
        "#055FThe hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#1317F#5PUm, Agate?\x02\x03",

            "I think this arm is...fake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x106,
        "#052FYou're kidding...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_44(0x106, 0x1)
    OP_8C(0x106, 270, 400)

    def lambda_3572():
        OP_6D(-4620, 0, -2840, 1500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3572)
    OP_8E(0x106, 0xFFFFEDAE, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 7)
    OP_0D()
    Sleep(500)
    OP_62(0x106, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #93
        0x106,
        (
            "#057F#6PGears, springs, quartz fragments...\x02\x03",

            "These things're--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -9770, 0, 5880, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrName("Man's Voice")

    NpcTalk(    #94
        0x9,
        "Man's Voice",
        (
            "#4P--archaisms. Orbal machines capable\x01",
            "of independent action.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_44(0x10A, 0xFF)
    OP_8C(0x106, 340, 0)
    OP_8C(0x10A, 340, 0)

    def lambda_3767():
        OP_8E(0xFE, 0xFFFFE5AC, 0x0, 0x528, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3767)

    def lambda_3782():
        OP_6D(-5810, 0, 150, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3782)
    OP_0D()
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #95
        0x10A,
        "#814F#2PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x106,
        "#057F#2PAnd who're you?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #97
        0x9,
        (
            "#1065F#6PDon't worry, I'm no enemy.\x01",
            "I'm Kevin Graham of the Septian Church.\x02\x03",

            "#1060FYou're Agate Crosner and Anelace Elfead,\x01",
            "right?\x02\x03",

            "I don't suppose you'd be up for\x01",
            "swapping some stories, would you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500B")

    label("loc_38A2")


    ChrTalk(    #98
        0x103,
        (
            "#022F#6PThat was...\x02\x03",

            "We may have defeated them, but\x01",
            "something is terribly wrong here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10A,
        (
            "#812F#4PDo you think they were on drugs\x01",
            "or something?\x02\x03",

            "I remember hearing they used\x01",
            "something like that to control some\x01",
            "thugs in...Ruan, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#020F#6PYes, that was one of the cases\x01",
            "Estelle solved.\x02\x03",

            "#522FBut this wasn't like what she described.\x02\x03",

            "This was like...trying to whip a tree...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #101
        0x8,
        "Boy's Voice",
        "#3PHa-HA! What great fun!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #102
        0x8,
        "Boy's Voice",
        (
            "#3PYou two aren't half bad, are you?\x01",
            "What a treat.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_21()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_59()
    OP_1D(0x6F)
    Sleep(1000)

    def lambda_3AE0():
        OP_6D(-130, 0, -2660, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3AE0)

    def lambda_3AF8():
        OP_67(0, 7230, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3AF8)

    def lambda_3B10():
        OP_6B(2009, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3B10)

    def lambda_3B20():
        OP_8E(0xFE, 0xD20, 0x0, 0xFFFFF164, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3B20)

    def lambda_3B3B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B3B)
    TurnDirection(0x10A, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #103
        0x103,
        "#023F#1PYou...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #104
        0x8,
        "Strange Boy",
        "#853FHaha...\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS118._CH")
    OP_C6(0x0, 0x0, 150000, 60000, 0)
    OP_C6(0x0, 0x0, 175000, 60000, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Strange Boy")

    AnonymousTalk(    #105
        (
            "#850FI am Enforcer No. 0, Campanella the Fool.\x02\x03",

            "I am but one hand of the Society of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_1D(0x6F)
    Sleep(1000)

    ChrTalk(    #106
        0x10A,
        "#1317F#5PO-Ouro...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#022F#1PFinally decided to step out of\x01",
            "the shadows, have we?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 3)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Sleep(500)

    ChrTalk(    #108
        0x103,
        (
            "#022F#1PWhat exactly are you plotting\x01",
            "here, boy?\x02\x03",

            "Where have the former Intelligence\x01",
            "men gone? Answer me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "#853FHaha, I'm sorry. I'm afraid I'm little\x01",
            "more than an observer this time.\x02\x03",

            "You're asking the wrong person if you\x01",
            "want details about the plan.\x02\x03",

            "In fact, I barely know them myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        "#023F#1PAn 'observer'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#850FAnyway, if you want to attend that tea\x01",
            "party, you'd better hurry.\x02\x03",

            "I'm not quite sure where it's being held,\x01",
            "but it isn't here.\x02\x03",

            "#851FOr shall we share some coffee instead,\x01",
            "and enjoy the dawn together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#022F#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10A,
        (
            "#813F#5PUm, kid?\x02\x03",

            "You look pretty young.\x01",
            "Are you really part of the society?\x02\x03",

            "#812FI don't mean to be insulting or anything,\x01",
            "but you might want to get away from them.\x01",
            "They're bad people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#853FYou're very kind, miss.\x02\x03",

            "But you know...it's okay to laugh at a fool.\x01",
            "That's what he's there for.\x02\x03",

            "#854FBut worrying about the Fool?\x01",
            "Now that's quite rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10A,
        "#814F#5PHuh...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)

    def lambda_410A():
        OP_6D(-2000, 0, -2270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_410A)
    Fade(1000)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    OP_8C(0xA, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_0D()
    WaitChrThread(0x8, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_419D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_419D)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #116
        0x10A,
        "#1317FWh-Wha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        "#024F#6PHow...? But they were unconscious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#854F#8PAh, you bracers really are naive.\x02\x03",

            "If you really want to defeat someone...\x01",
            "you have to break them into pieces.\x01",
            "Like...so.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "monster\\msc0100.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    LoadEffect(0x2, "map\\mp047_00.eff")
    PlayEffect(0x2, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x5, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x6, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Fade(500)

    def lambda_4435():
        OP_6D(-130, 0, -2660, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4435)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrChipByIndex(0xB, 15)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrPos(0xA, -5990, 0, -2060, 0)
    SetChrPos(0xC, -7310, 0, -5200, 0)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 3)
    SetChrPos(0xD, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x103, 21)
    SetChrChipByIndex(0x10A, 23)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x10A, 0)

    def lambda_44F5():
        OP_96(0xFE, 0xFFFFF948, 0x0, 0xFFFFF75E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44F5)

    def lambda_4513():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4513)

    def lambda_452D():
        OP_96(0xFE, 0xFFFFF876, 0x0, 0xFFFFF06A, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_452D)

    def lambda_454B():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_454B)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x103, 270, 0)
    OP_8C(0x10A, 270, 0)
    SetChrChipByIndex(0x103, 6)
    SetChrChipByIndex(0x10A, 13)
    SetChrSubChip(0x103, 3)
    SetChrSubChip(0x10A, 3)

    ChrTalk(    #119 op#A op#5
        0x103,
        "#523F#10A#1PWHAT THE HELL?!\x05\x02",
    )


    ChrTalk(    #120 op#A op#5
        0x10A,
        "#1312F#1P#10A#2PAIEEEE...!\x05\x02",
    )

    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_9E(0x103, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(500)

    ChrTalk(    #121
        0x103,
        "#522F#5PWhat...? What have you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10A,
        (
            "#1317FYou... You... That's...\x01",
            "How could you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#851FHaha! Did I surprise you?\x02\x03",

            "It's so easy to break even a\x01",
            "well-made toy, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x2, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #124
        0x8,
        (
            "#854FBut I'm afraid that's the end of the\x01",
            "Fool's show for tonight.\x02",
        )
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x3E8)

    ChrTalk(    #125
        0x8,
        (
            "#854FFarewell! Hopefully I can give you\x01",
            "an encore someday.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47C8():

        label("loc_47C8")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_47C8")

    QueueWorkItem2(0x103, 3, lambda_47C8)
    Sleep(500)
    OP_99(0x103, 0x3, 0x0, 0x5DC)
    OP_44(0x103, 0x3)
    SetChrChipByIndex(0x103, 3)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    OP_8C(0x103, 90, 600)

    ChrTalk(    #126
        0x103,
        "#024F#3SWAIT! GET...back...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 4)

    def lambda_483F():
        OP_6D(2500, 0, -2270, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_483F)

    def lambda_4857():
        OP_8F(0xFE, 0x5DC, 0x0, 0xFFFFF380, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4857)

    def lambda_4872():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4872)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 5)
    SetChrSubChip(0x103, 0)
    OP_82(0x1, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x8)

    def lambda_489D():
        OP_99(0xFE, 0x0, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_489D)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(300)
    OP_22(0x208, 0x0, 0x64)
    OP_20(0x7D0)
    WaitChrThread(0x103, 0x3)
    ClearChrFlags(0x103, 0x1000)
    SetChrFlags(0x8, 0x80)
    Sleep(1500)

    ChrTalk(    #127
        0x103,
        "#022F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_48E6():

        label("loc_48E6")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_48E6")

    QueueWorkItem2(0x10A, 3, lambda_48E6)
    Sleep(500)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_44(0x10A, 0x3)
    Fade(250)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #128
        0x10A,
        (
            "#813F#1P...\x02\x03",

            "Sch-Sch-Schera... Umm... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        "#026F#5PI know, honey...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x103, 270, 400)
    Sleep(500)

    def lambda_49A7():

        label("loc_49A7")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_49A7")

    QueueWorkItem2(0x10A, 1, lambda_49A7)

    def lambda_49B8():
        OP_6D(-2500, 0, -3390, 2000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49B8)
    OP_8E(0x103, 0xFFFFF7EA, 0x0, 0xFFFFF56A, 0x5DC, 0x0)
    WaitChrThread(0x103, 0x1)
    Sleep(500)

    ChrTalk(    #130
        0x103,
        (
            "#522FAt least it was...a quick death.\x01",
            "I hope they didn't feel anything.\x02\x03",

            "We still can't simply leave them like this,\x01",
            "though. It'd be barbaric...even more so\x01",
            "than what just happened.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #131
        0x103,
        (
            "#524FAnelace...try to find some sheets,\x01",
            "all right? I'll...handle the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10A,
        "#812F#4PR-Right...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0x10A, 0x1)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #133
        0x10A,
        "#814F...Wha...?\x02",
    )

    CloseMessageWindow()

    def lambda_4B55():

        label("loc_4B55")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_4B55")

    QueueWorkItem2(0x103, 1, lambda_4B55)

    def lambda_4B66():
        OP_8E(0xFE, 0xFFFFF150, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4B66)
    WaitChrThread(0x10A, 0x1)
    Fade(250)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 2)
    SetChrSubChip(0x10A, 7)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x10A, 16)
    SetChrSubChip(0x10A, 7)
    OP_0D()

    ChrTalk(    #134
        0x103,
        "#023FWhat...on...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10A,
        (
            "#1317F#5PUm, Schera?\x02\x03",

            "I think this arm is...fake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        "#023FBut that...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_44(0x103, 0x1)
    OP_8C(0x103, 270, 400)

    def lambda_4C2F():
        OP_6D(-4620, 0, -2840, 1500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C2F)
    OP_8E(0x103, 0xFFFFEDAE, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 25)
    SetChrSubChip(0x103, 7)
    OP_0D()
    Sleep(500)
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x103)
    Sleep(500)

    ChrTalk(    #137
        0x103,
        (
            "#022F#6PHmm... Gears, springs, and what\x01",
            "look like quartz fragments.\x02\x03",

            "I can hardly believe it, but these are--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -9770, 0, 5880, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrName("Man's Voice")

    NpcTalk(    #138
        0x9,
        "Man's Voice",
        (
            "#4P--archaisms. Orbal machines capable\x01",
            "of independent action.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_44(0x10A, 0xFF)
    OP_8C(0x103, 340, 0)
    OP_8C(0x10A, 340, 0)

    def lambda_4E32():
        OP_8E(0xFE, 0xFFFFE5AC, 0x0, 0x528, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E32)

    def lambda_4E4D():
        OP_6D(-5810, 0, 150, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4E4D)
    OP_0D()
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #139
        0x10A,
        "#814F#2PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        "#023F#2PFather Kevin! What are you doing here?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #141
        0x9,
        (
            "#1062F#6PShe remembers me!\x01",
            "There's hope for my love life yet!\x02\x03",

            "#1065FAh, but since the little lady over there\x01",
            "doesn't know me... I'm Kevin Graham\x01",
            "of the Septian Church.\x02\x03",

            "#1060FAnyway, you're Scherazard Harvey, if I\x01",
            "remember right, and with you is Anelace\x01",
            "Elfead, yeah?\x02\x03",

            "I don't suppose you'd be up for\x01",
            "swapping some stories, would you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500B")

    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_23(0x10E)
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_20A8 end

    def Function_5_503A(): pass

    label("Function_5_503A")

    OP_8F(0xFE, 0xFFFFF84E, 0x0, 0xFFFFFA6A, 0x3E8, 0x0)
    Return()

    # Function_5_503A end

    def Function_6_504F(): pass

    label("Function_6_504F")

    SetChrChipByIndex(0x10A, 12)
    SetChrSubChip(0x10A, 0)
    OP_8F(0xFE, 0xFFFFF434, 0x0, 0xFFFFFA56, 0x3E8, 0x0)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Return()

    # Function_6_504F end

    def Function_7_5078(): pass

    label("Function_7_5078")

    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Return()

    # Function_7_5078 end

    def Function_8_50B6(): pass

    label("Function_8_50B6")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_8_50B6 end

    def Function_9_50FE(): pass

    label("Function_9_50FE")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_5177"),
        (1, "loc_517D"),
        (SWITCH_DEFAULT, "loc_5183"),
    )


    label("loc_5177")

    OP_A2(0x1200)
    Jump("loc_5183")

    label("loc_517D")

    OP_A2(0x1201)
    Jump("loc_5183")

    label("loc_5183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5191")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5195")

    label("loc_5191")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5195")

    Return()

    # Function_9_50FE end

    SaveToFile()

Try(main)
